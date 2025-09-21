

def test_createuser_endpoint(client):
    res = client.post("/create-user", json={"username": "prueba1",
                      "password": "secret_password", "email": "prueba1@hotmail.com"})
    assert res.status_code in [200]


def test_login_endpoint(client):
    res = client.post(
        "/login", json={"username": "prueba1", "password": "secret_password"})
    print(f"test_login:{res.json}")
    assert res.status_code in [200]


def test_login_failed_endpoint(client):
    res = client.post(
        "/login", json={"username": "pr", "password": "secret_password"})
    print(f"test_login_failed:{res.json}")
    assert res.status_code in [400]


def test_createuser_failed_endpoint(client):
    res = client.post(
        "/create-user", json={"email": "asd", "username": 12, "password": "secret_password"})
    print(f"test_login_failed:{res.json}")
    assert res.status_code in [400]
