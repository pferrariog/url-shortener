def test_create_url(client) -> None:
    """Url creation endpoint test"""
    response = client.post("/api/", json={"original_url": "https://dev.to/", "reference_code": "endpointtest"})

    assert response.status_code == 201
    assert "original_url" in response.json()
    assert "reference_code" in response.json()
    assert "creation_date" in response.json()
