from typing import Annotated

from pydantic import BaseModel
from readyapi import Form, ReadyAPI

app = ReadyAPI()


class FormData(BaseModel):
    username: str
    password: str

    class Config:
        extra = "forbid"


@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data