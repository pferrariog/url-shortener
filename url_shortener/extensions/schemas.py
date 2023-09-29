from datetime import date
from pydantic import BaseModel


class UrlSchema(BaseModel):
    """"""
    url: str

class UrlInfo(UrlSchema):
    """"""
    original_url: str
    clicks: int
    creation_date: date
