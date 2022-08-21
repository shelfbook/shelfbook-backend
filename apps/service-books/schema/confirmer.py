from pydantic import BaseModel


class ConfirmerSchema(BaseModel):
    confirm: bool
