from ninja.schema import Schema


class GamesOut(Schema):
    id: int
    name: str
    price: str
    picture: str
    page: str