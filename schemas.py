from pydantic import BaseModel, EmailStr


class message(BaseModel):
    message: str


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserPublicSchema(BaseModel):
    id: int
    name: str
    email: EmailStr


class UserDBSchema(UserSchema):
    id: int


class UserListSchema(BaseModel):
    users: list[UserPublicSchema]
