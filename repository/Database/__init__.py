import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from multiprocessing import Lock

db_conn = os.getenv('AURCHESTRA_DB_CONNECTION', "sqlite:///test_local.db")

engine = create_engine(db_conn)

DBSession = sessionmaker(bind=engine)

Base = declarative_base()

lock = Lock()

def init_db():
    with lock:
        Base.metadata.create_all(engine)
