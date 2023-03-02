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
        "first_name": "",
        "last_name": "",
        "address": "",
        "previous_address": "",
        "phone_number": None,
    }


def test_update_profile(client, django_user_model):
    user = django_user_model.objects.create_user(username="user1", password="bar")
    client.force_login(user)

    response = client.put(
        "/accounts/profile/",
        data=json.dumps(
            {
                "first_name": "new_name",
                "last_name": "last_name",
                "address": "123 Street",
                "previous_address": "456 Avenue",
            }
        ),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.json() == {
        "first_name": "new_name",
        "last_name": "last_name",
        "address": "123 Street",
        "previous_address": "456 Avenue",
        "phone_number": None,
    }


def test_delete_profile(client, django_user_model):
    user = django_user_model.objects.create_user(username="user1", password="bar")
    client.force_login(user)

    response = client.delete("/accounts/profile/")

    assert response.status_code == 204
