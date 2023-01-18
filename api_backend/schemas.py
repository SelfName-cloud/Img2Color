from pydantic import BaseModel


class UploadImage(BaseModel):
    desc: str
    face: bool
    natural: bool


class User(BaseModel):
    id: int
    name: str


class GetImage(BaseModel):
    user: User
    image: UploadImage



