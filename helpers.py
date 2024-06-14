import allure
import pytest
import random
import requests
from faker import Faker

from urls import *

fake = Faker(locale="ru_RU")


@allure.step("Регистрация пользователя и получение данных для входа")
def register_new_user_and_get_credentials() -> list:
    login_pass = []
    payload = {
        'email': fake.email(),
        'password': fake.password(length=10),
        'name': fake.first_name()
    }
    response = requests.post(URL_REGISTER_PAGE, data=payload)
    if response.status_code == 200:
        login_pass.append(payload['email'])
        login_pass.append(payload['password'])
        login_pass.append(payload['name'])
    return login_pass


@allure.step("Получение токена")
def get_token():
    data = register_new_user_and_get_credentials()
    payload = {
        'email': data[0],
        'password': data[1]}
    response_post = requests.post(USER_LOGIN, data=payload)
    if response_post.status_code == 200:
        return response_post.json()['accessToken']
    else:
        pytest.xfail(reason=f'Не удалось получить токен\n{response_post.json()}')


@allure.step("Получение данных ингредиентов")
def get_ingredient_data():
    hash_ingredients = []
    response_get = requests.get(GET_INGREDIENTS_DATA, headers={'Authorization': f'{get_token()}'})
    if response_get.status_code == 200:
        hash_ingredients.append(f'{response_get.json()["data"][0]["_id"]}')
        hash_ingredients.append(f'{response_get.json()["data"][1]["_id"]}')
    return hash_ingredients


@allure.step("Генерация произвольного номера")
def generate_number():
    ramdom_number = ''
    for x in range(8):
        ramdom_number = ramdom_number + random.choice(list('123456789'))
    return ramdom_number
