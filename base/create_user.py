import allure

from helpers import *


class CreateUser:
    @staticmethod
    @allure.step("Передача данных пользователя")
    def generate_user_data(email=fake.email(), password=fake.password(length=10), name=fake.first_name()):
        payload = {
            'email': email,
            'password': password,
            'name': name
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
