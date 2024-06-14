import allure
import pytest
from helpers import *


class GetOrders:

    @allure.step('Передача хеша ингредиентов и создание заказа')
    def post_order(self):
        payload = {
            'ingredients': get_ingredient_data()
        }
        response = requests.post(CREATE_ORDER, data=payload)
        if response.status_code == 200:
            return response
        else:
            pytest.xfail(reason=f"Не удалось создать заказ\n{response.json()}")
