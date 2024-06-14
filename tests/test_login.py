import allure
import requests
from base.login_user import LoginUser
from urls import *


class TestLogin:
    @allure.title('Успешная авторизация пользователя')
    def test_login_user_success_true(self):
        login_user = LoginUser()
        payload = login_user.login_user()
        response_post = requests.post(USER_LOGIN, data=payload)
        assert (response_post.status_code == 200 and
                '"success":true', '"accessToken": "Bearer"', '"refreshToken": ""',
                '"user": {"email": "", "name": ""}' in response_post.text)

    @allure.title('Неуспешная авторизация под несуществующим пользователем')
    def test_login_and_password_user_false(self):
        login_user = LoginUser()
        payload = login_user.random_login_user()
        response_post = requests.post(USER_LOGIN, data=payload)
        assert response_post.status_code == 401 and response_post.json()['message'] == 'email or password are incorrect'
