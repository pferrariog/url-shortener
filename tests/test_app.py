from url_shortener.extensions.schemas import UrlSchema
from url_shortener.extensions.services import insert_url_into_db


def test_create_url(client) -> None:
    """Url creation endpoint test"""
    response = client.post("/api/", json={"original_url": "https://dev.to/", "reference_code": "endpointtest"})

    assert response.status_code == 201
    assert "original_url" in response.json()
    assert "reference_code" in response.json()
    assert "creation_date" in response.json()


def test_wrong_reference_code_should_return_404(client) -> None:
    """404 return test"""
    response = client.get("/api/teste")

    assert response.status_code == 404
    assert response.json() == {"detail": "URL teste not found"}


def test_url_already_exists_and_return_url(client, session) -> None:
    """Test code already exists and return the object"""
    url = insert_url_into_db(session, UrlSchema(original_url="http://teste.com/"))
    response = client.post("/api/", json={"original_url": "http://teste.com/"})
    expected_response = {
        "original_url": "http://teste.com/",
        "reference_code": url.reference_code,
        "creation_date": url.creation_date.isoformat(),
        "message": "Url register already exists!",
    }
    assert response.json() == expected_response


def test_given_reference_code_already_exists(url, client) -> None:
    """Test code already exists and return the object"""
    response = client.post("/api/", json={"original_url": "https://dev.to/", "reference_code": "teste"})

    assert response.status_code == 400
    assert response.json() == {"detail": "Url alias already exists, try another!"}
