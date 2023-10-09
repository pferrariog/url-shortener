from sqlalchemy import select
from url_shortener.extensions.database import UrlModel


def test_create_url(session, url):
    url_object = session.scalar(select(UrlModel).where(UrlModel.reference_code == "teste"))

    assert url_object.reference_code == "teste"
