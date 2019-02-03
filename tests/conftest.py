import pytest
from application import create_app
from application.db import init_db

@pytest.fixture
def app():
    app = create_app()

    with app.app_context():
        init_db()

    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()