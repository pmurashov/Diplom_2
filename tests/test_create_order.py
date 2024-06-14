import allure
from helpers import *


class TestCreateOrder:
    @allure.title('Успешное создание заказа авторизованного пользователя c ингредиентами')
    def test_create_order_success_true(self):
        payload = {
            'ingredients': get_ingredient_data()
        }
        response_post = requests.post(CREATE_ORDER, data=payload)
        assert response_post.status_code == 200 and '"success":true' in response_post.text

    @allure.title('Неуспешное создание заказа авторизованного пользователя c неверным хешем ингредиентов')
    def test_create_order_false_hash(self):
        payload = {
            'ingredients': [f'{generate_number()}']
        }
        response_post = requests.post(CREATE_ORDER, data=payload, headers={'Authorization': f'{get_token()}'})
        assert response_post.status_code == 500, f'Заказ создан с неверным хэшем\n{response_post.json()}'

    @allure.title('Неуспешное создание заказа авторизованного пользователя без ингредиентов')
    def test_create_order_not_ingredient(self):
        payload = {
            'ingredients': []
        }
        response_post = requests.post(CREATE_ORDER, data=payload, headers={'Authorization': f'{get_token()}'})
        assert (response_post.status_code == 400 and
                response_post.json()['message'] == 'Ingredient ids must be provided' and
                '"success":false' in response_post.text)

    @allure.title('Неуспешное создание заказа неавторизованного пользователя c неверным хешем ингредиентов')
    def test_create_order_not_user_false_hash(self):
        payload = {
            'ingredients': [f'{generate_number()}']
        }
        response_post = requests.post(CREATE_ORDER, data=payload)
        assert response_post.status_code == 500, 'Internal Server Error'

    @allure.title('Неуспешное создание заказа неавторизованного пользователя без ингредиентов')
    def test_create_order_not_user_not_ingredient(self):
        payload = {
            'ingredients': []
        }
        response_post = requests.post(CREATE_ORDER, data=payload)
        assert (response_post.status_code == 400 and
                response_post.json()['message'] == 'Ingredient ids must be provided' and
                '"success":false' in response_post.text)
