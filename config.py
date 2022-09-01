import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(ROOT_DIR, "employees.json")


class Config:
    MONGODB_NAME = os.getenv("MONGODB_NAME", "test")
    MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "users")
    MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://docker:mongopw@localhost:49154")
