import allure
from helpers import *


class TestChangeUserData:
    @allure.title('Успешное обновление данных авторизованного пользователя')
    def test_change_user_data_success_true(self):
        payload = {
            'email': fake.email(),
            'name': fake.first_name()
        }
        response = requests.patch(GET_USER_DATA, headers={'Authorization': f'{get_token()}'}, data=payload)
        assert response.status_code == 200 and '"success":true' in response.text

    @allure.title('Обновление данных неавторизованного пользователя')
    def test_change_user_data_success_false(self):
        updated_profile = {
            'email': fake.email(),
            'name': fake.first_name()
        }
        response_patch = requests.patch(GET_USER_DATA, data=updated_profile)
        assert (response_patch.status_code == 401 and
                '"success":false' in response_patch.text and
                response_patch.json()['message'] == 'You should be authorised')
