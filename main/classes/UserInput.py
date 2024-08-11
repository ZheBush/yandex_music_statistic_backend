from pydantic import BaseModel


class UserInput(BaseModel):
    user_token: str