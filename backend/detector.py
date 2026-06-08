import psutil

WATCH_APPS = ["chrome.exe", "zoom.exe", "teams.exe"]

def scan_processes():
    apps = []

    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            name = proc.info.get('name')
            status = proc.info.get('status')

            if not name:
                continue

            name = name.lower()

            if name in WATCH_APPS and status == psutil.STATUS_RUNNING:
                apps.append({
                    "pid": proc.info['pid'],
                    "name": name
                })

        except:
            pass

    return apps


def detect_device_usage(name):
    name = name.lower()

    webcam = 0
    mic = 0

    if "zoom" in name or "teams" in name:
        webcam = 1
        mic = 1

    elif "chrome" in name:
        mic = 1

    return {
        "webcam": webcam,
        "mic": mic
    }