import uvicorn
from get_caged.api import app
from get_caged.db import initialize_db


if __name__ == "__main__":
    initialize_db()
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
