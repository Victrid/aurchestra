from Database import engine
from Database.model import Base


def init_db():
    """
    Initialize the database
    """
    Base.metadata.create_all(engine)