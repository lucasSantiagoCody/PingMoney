# PingMoney

<div>
    <p>
        The technical challenge proposed for the Back-end position involves the development of an application that simulates a simplified money transfer system between two types of users: commum and retailer.
    </p>
</div>

## 🚀 First steps

#### Clone this repository to your computer
```
https://github.com/lucasSantiagoCody/PingMoney.git
```
#### Open the terminal

##### Windows
###### Creating a development environment 
```
python -m venv venv
```
###### Installing dependencies
```
pip install -r requirements.txt
```
###### Creating migration files
```
python manage.py makemigrations
```
###### Push migrations to save the changes made on models 
```
python manage.py migrate
```
##### Linux
###### Creating a development environment
```
python3 -m venv venv
```
###### Installing dependencies
```
pip3 install -r requirements.txt
```
###### Creating migration files
```
python3 manage.py makemigrations
```
###### Push migrations to save the changes made on models
```
python3 manage.py migrate
```
### Starting developemnt server
#### Windows
```
python manage.py runserver
```
#### Linux
```
python3 manage.py runserver
```

### ⚠️ Create .env file end follow all steps on .env-example file

## Using Docker
```
    docker compose up
```
## Features
### # Use  postam to test this api rest
### App user
#### register api view
#####  endpoint:
```
    localhost:8000/user/register/
```
##### body:
```
{
    "user":{
        "full_name": "your_full_name",
        "email": "your_email",
        "cpf_cnpj": "valid_cpf_or_cnpj",
        "password": "your_password"
        },
    "type_user": "choose_a_user_type"
}
```

Replace this "choose_a_user_type" to storekeeper(lojistas) or commun(usuários comuns)


### App payment

#### transfer api view
##### endpoint:
```
    localhost:8000/payment/transfer/
```
##### body:
```
{
    "amount": 10,
    "payer": 2,
    "payee": 3
}
```

#### Deposit api view
##### endpoint:

```
    localhost:8000/payment/deposit/
```
#### body:
```
    {
        "depositor": 2,
        "amount": 10
    }
```

## Running tests

### running all tests
##### Windows
```
    python manage.py test
```
##### Linux
```
    python3 manage.py test
```
### Partially running the tests (recommended)
##### Windows
```
    python manage.py test app_name
```
##### Liux
```
    python3 manage.py test app_name
```

Replace this "app_name" with user or payment