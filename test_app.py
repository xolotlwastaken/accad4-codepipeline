from app import app
def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

def test_about():
    with app.test_client() as client:
        response = client.get('/about')
        assert response.status_code == 200
