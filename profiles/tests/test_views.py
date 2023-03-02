import json


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_profile_unathorized(client):
    response = client.get("/accounts/profile/")
    assert response.status_code == 401


def test_get_profile(client, django_user_model):
    username = "user1"

    user = django_user_model.objects.create_user(username=username, password="bar")
    client.force_login(user)

    response = client.get("/accounts/profile/")
    assert response.status_code == 200
    assert response.json() == {
        "username": username,
        "email": "",
        "first_name": "",
        "last_name": "",
    }


def test_update_profile(client, django_user_model):
    user = django_user_model.objects.create_user(username="user1", password="bar")
    client.force_login(user)

    response = client.put(
        "/accounts/profile/",
        data=json.dumps({"username": "new_name"}),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json() == {
        "username": "new_name",
        "email": "",
        "first_name": "",
        "last_name": "",
    }
