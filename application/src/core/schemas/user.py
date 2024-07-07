import pydantic
import uuid
from pydantic import BaseModel
from typing import Optional

class UserSession(BaseModel):
    client: str
    user_full_name: str
    user_id: int
    user_role_name: str
    access_token: str
    views_control_access: list[str]
    institutions: Optional[list[str]] = None

class UserRole(pydantic.BaseModel):
    id: uuid.UUID

    class Config:
        from_attributes = True

class UserProfile(pydantic.BaseModel):
    full_name: str
    e_mail: str

    class Config:
        from_attributes = True

class UserAccount(pydantic.BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True

class User(pydantic.BaseModel):
    account: UserAccount
    profile: UserProfile
    role: UserRole

    class Config:
        from_attributes = True


class CreateUser(User):
    pass
