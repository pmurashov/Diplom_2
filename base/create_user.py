import allure
from helpers import *


class CreateUser:
    @staticmethod
    @allure.step('Передача данных без пароля')
    def data_without_password():
        payload = {
            'email': fake.email(),
            'password': [],
            'name': fake.first_name()
        }
        return payload

    @staticmethod
    @allure.step('Передача данных без поля Email')
    def data_without_login():
        payload = {
            'email': [],
            'password': fake.password(length=10),
            'name': fake.first_name()
        }
        return payload

    @staticmethod
    @allure.step('Передача данных без имени')
    def data_without_name():
        payload = {
            'email': fake.email(),
            'password': fake.password(length=10),
            'name': []
        }
        return payload

    @allure.step('Передача данных с уникальными значениями во всех полях')
    def data_login_success(self):
        payload = {
            'email': fake.email(),
            'password': fake.password(length=10),
            'name': fake.first_name()
        }
        return payload

    @allure.step('Создаем курьера. И запоминаем данные')
    def login_courier_success(self):
        data = register_new_user_and_get_credentials()
        payload = {
            'email': data[0],
            'password': data[1],
            'name': data[2]
        }
        return payload
