import os
import tempfile
import pytest
from main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        yield client

    os.close(db_fd)
