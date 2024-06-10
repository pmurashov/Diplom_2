import allure
from base.get_orders import GetOrders
from helpers import *


class TestGetOrders:
    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_orders_success_true(self):
        get_orders = GetOrders()
        post_order = get_orders.post_order()
        payload = post_order.json()["order"]
        response_get = requests.get(GET_ORDERS, data=payload, headers={'Authorization': f'{get_token()}'})
        assert response_get.status_code == 200 and '"success":true' in response_get.text

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_orders_success_false(self):
        response_get = requests.get(GET_ORDERS)
        assert (response_get.status_code == 401 and
                '"success":false' in response_get.text and
                response_get.json()['message'] == 'You should be authorised')
