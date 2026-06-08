import psutil

BLOCKED = set()

def block_app(pid, name):
    try:
        psutil.Process(pid).terminate()
        BLOCKED.add(name.lower())
        return True
    except:
        return False


def enforce_block():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            name = (proc.info['name'] or "").lower()
            if name in BLOCKED:
                proc.terminate()
        except:
            pass


def reset_blocks():
    BLOCKED.clear()