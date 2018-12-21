import os
import click
from flask.cli import with_appcontext
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database


DB_HOST = "sqlite:///foo.sqlite".format(  # TODO: change this to a proper DB
    user=os.environ.get("USER"),
    password=os.environ.get("PASSWORD"),
    db=os.environ.get("DB"),
    host=os.environ.get("HOST")
)


engine = create_engine(DB_HOST, convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
Base = declarative_base()
Base.query = session.query_property()


@click.command('init-db')
@with_appcontext
def init():
    """ Init the database, drops then creates all tables.
    """
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def insert(to_insert):
    """ Insert documents into database, using a session.

    Args:
        to_insert: either an object or a list of object to insert in DB
    """
    if isinstance(to_insert, list):
        session.bulk_save_objects(to_insert)
    else:
        session.add(to_insert)

    return session.commit()
