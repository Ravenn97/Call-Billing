from apps import create_app
import os

app = create_app()
host = os.getenv("FLASK_HOST", "0.0.0.0")
port = os.getenv("FLASK_PORT", 5000)

if __name__ == "__main__":
    app.run(host=host, port=port)
