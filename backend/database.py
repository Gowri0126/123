import sqlite3

DB = "logs.db"


def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        app TEXT,
        webcam INTEGER,
        mic INTEGER,
        status TEXT,
        time TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_log(app, webcam, mic, status, time):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    INSERT INTO logs (app, webcam, mic, status, time)
    VALUES (?, ?, ?, ?, ?)
    """, (app, webcam, mic, status, time))

    conn.commit()
    conn.close()


def fetch_logs():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    rows = c.execute("""
    SELECT app, webcam, mic, status, time
    FROM logs
    ORDER BY id DESC
    LIMIT 50
    """).fetchall()

    conn.close()

    logs = []

    for row in rows:
        logs.append({
            "app_name": row[0],
            "webcam": row[1],
            "mic": row[2],
            "status": row[3],
            "timestamp": row[4]
        })

    return logs