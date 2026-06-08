import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "logs.db")

def view_logs():
    if not os.path.exists(DB_PATH):
        print("❌ logs.db not found. Run backend first.")
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM logs")
        rows = cursor.fetchall()

        if not rows:
            print("⚠ No logs found")
        else:
            print("\n📜 SMART PRIVACY GUARD LOGS\n")
            print("-" * 60)

            for row in rows:
                print(f"App: {row[1]}")
                print(f"Webcam: {row[2]} | Mic: {row[3]}")
                print(f"Score: {row[4]}")
                print(f"Status: {row[5]}")
                print(f"Time: {row[6]}")
                print("-" * 60)

        conn.close()

    except Exception as e:
        print("❌ Error reading database:", e)


if __name__ == "__main__":
    view_logs()