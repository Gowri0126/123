from flask import Flask, jsonify, request
from flask_cors import CORS
import time, threading

from detector import scan_processes, detect_device_usage
from blocker import block_app, enforce_block, reset_blocks
from database import init_db, insert_log, fetch_logs

app = Flask(__name__)
CORS(app)

init_db()


@app.route("/")
def home():
    return "Backend running..."


@app.route("/scan")
def scan():
    results = []

    processes = scan_processes()

    # Return empty list if no monitored apps are running
    if not processes:
        return jsonify([])

    for app_ in processes:
        usage = detect_device_usage(app_["name"])

        results.append({
            "name": app_["name"],
            "pid": app_["pid"],
            "webcam": usage["webcam"],
            "mic": usage["mic"]
        })

    return jsonify(results)


@app.route("/block", methods=["POST"])
def block():
    d = request.json

    ok = block_app(d["pid"], d["name"])

    # No score anymore
    insert_log(
        d["name"],
        d["webcam"],
        d["mic"],
        "blocked",
        time.strftime("%H:%M:%S")
    )

    return jsonify({"status": ok})


@app.route("/reset", methods=["POST"])
def reset():
    import sqlite3

    conn = sqlite3.connect("logs.db")
    c = conn.cursor()

    c.execute("DELETE FROM logs")

    conn.commit()
    conn.close()

    reset_blocks()

    return {"status": "reset done"}


@app.route("/logs")
def logs():
    return jsonify(fetch_logs())


def run_blocker():
    while True:
        enforce_block()
        time.sleep(2)


threading.Thread(target=run_blocker, daemon=True).start()


if __name__ == "__main__":
    app.run(debug=True)