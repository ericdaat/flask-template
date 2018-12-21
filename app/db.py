import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


DB_HOST = "sqlite:///foo.db".format(  # TODO: change this to a proper DB
    user=os.environ.get("USER"),
    password=os.environ.get("PASSWORD"),
    db=os.environ.get("DB"),
    host=os.environ.get("HOST")
)

engine = create_engine(DB_HOST, convert_unicode=True)
session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=engine)

Base = declarative_base()
Base.query = session.query_property()


def init(db_host):
    """ Init the database, drops then creates all tables.

    Args:
        db_host (str): database hostname

    Returns:

    """
    engine = create_engine(db_host)
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def insert(to_insert, session):
    """ Insert documents into database, using a session.

    Args:
        to_insert: either an object or a list of object to insert in DB
        session: sqlalchemy session object

    Returns:

    """
    sess = session()

    if isinstance(to_insert, list):
        sess.bulk_save_objects(to_insert)
    else:
        sess.add(to_insert)

    return sess.commit()
