from flask import Flask, Response, send_from_directory
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
app = Flask(__name__, static_folder=str(STATIC_DIR), static_url_path="/static")

@app.get("/")
def home():
    response = send_from_directory(STATIC_DIR, "index.html", max_age=0)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response

@app.get("/healthz")
def health():
    return {"status": "ok", "app": "ZAD OSINT MUSIC"}, 200

@app.get("/favicon.ico")
def favicon():
    return Response(status=204)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= int(__import__("os").environ.get("PORT", "5000")))
