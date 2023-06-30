import pytest
from flask import Flask
from controllers.light_controller import light_controller
from services.light_service import LightService
from services.error_service import CustomError

def create_app():
    app = Flask(__name__)
    app.register_blueprint(light_controller)
    return app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_create_lights(mocker):
    return mocker.patch.object(LightService, "create_lights")

def test_control_lights_no_json(client, mock_create_lights):
    mock_create_lights.return_value = ['light1', 'light2', 'light3']
    response = client.post('/lights')
    assert response.status_code == 400
    assert response.get_json() == {'error': 'No JSON data provided.', 'error_code': 2001}

def test_control_lights_no_light_id(client, mock_create_lights):
    mock_create_lights.return_value = ['light1', 'light2', 'light3']
    response = client.post('/lights', json={})
    assert response.status_code == 400
    assert response.get_json() == {'error': "No 'light_id' field provided in the data.", 'error_code': 2002}

def test_control_lights_success(client, mock_create_lights):
    mock_create_lights.return_value = ['light1', 'light2', 'light3']
    response = client.post('/lights', json={'light_id': '1'})
    assert response.status_code == 200
    assert response.get_data() == b'OK'
