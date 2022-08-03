
def test_ping(test_app):
    response = test_app.get("/api")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}