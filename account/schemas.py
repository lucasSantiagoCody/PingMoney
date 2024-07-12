from ninja import Schema


class UserSchema(Schema):
    full_name: str
    email: str 
    cpf_cnpj: str 
    password: str


class TypeUserSchema(Schema):
    user: UserSchema
    type_user: str