import allure
import requests
import pytest
from base.create_user import CreateUser
from urls import *


class TestCreateUser:
    create_user = CreateUser()

    @allure.title('Успешное создание пользователя')
    def test_create_user_success(self):
        create_user = CreateUser()
        payload = create_user.data_login_success()
        response_post = requests.post(CREATE_USER, data=payload)
        assert response_post.status_code == 200 and '"success":true' in response_post.text

    @allure.title('Неуспешное создание двух одинаковых пользователей')
    def test_create_two_same_users_returns_false(self):
        create_user = CreateUser()
        payload = create_user.login_courier_success()
        response_post = requests.post(CREATE_USER, data=payload)
        assert (response_post.status_code == 403 and
                '"success":false' in response_post.text and
                response_post.json()['message'] == 'User already exists')

    @allure.title('Проверка обязательных полей для создания пользователя')
    @pytest.mark.parametrize('payload', [create_user.data_without_password(),
                                         create_user.data_without_login(),
                                         create_user.data_without_name()])
    def test_create_user_without_password_or_login_or_name(self, payload):
        response_post = requests.post(CREATE_USER, data=payload)
        assert (response_post.status_code == 403 and
                '"success":false' in response_post.text and
                response_post.json()['message'] == 'Email, password and name are required fields')
