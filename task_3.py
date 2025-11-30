
import configparser
import json
import sqlite3
from fastapi import FastAPI, HTTPException # pyright: ignore[reportMissingImports]
import uvicorn # type: ignore

app = FastAPI()
DB = "config.db"

# -----------------------------
# Database Setup
# -----------------------------
def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS configurations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            json_data TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# Parse Config File
# -----------------------------
def parse_config(file_path):
    config = configparser.ConfigParser()

    try:
        if not config.read(file_path):
            print("Error: File not found or unreadable.")
            return None

        output = {section: dict(config.items(section)) for section in config.sections()}
        return output

    except Exception as e:
        print("Error reading config file:", e)
        return None

# -----------------------------
# Save JSON to Database
# -----------------------------
def save_to_db(data):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO configurations (json_data) VALUES (?)",
        (json.dumps(data),)
    )
    conn.commit()
    conn.close()

# -----------------------------
# GET API Endpoint
# -----------------------------
@app.get("/get-config")
def get_config():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT json_data FROM configurations ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()

    conn.close()

    if row:
        return json.loads(row[0])
    else:
        raise HTTPException(status_code=404, detail="No data found")

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    parsed = parse_config("config.ini")

    if parsed:
        print("Configuration File Parser Results:")
        print(json.dumps(parsed, indent=4))
        save_to_db(parsed)
        uvicorn.run(app, host="0.0.0.0", port=8000)