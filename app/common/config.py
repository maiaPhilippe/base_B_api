import os

db_url = os.getenv("MONGODB_URL")
username = os.getenv("MONGODB_USER", False)
password = os.getenv("MONGODB_PASS", False)
db_name = os.getenv("DB_NAME")
auth_mechanism = os.getenv("AUTH_MECHANISM")
host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", 5000)

