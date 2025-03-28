import requests
from utils_methods import UtilsMethods
import curl
from api_methods import ApiMethod
import data
import allure


class TestLoginCourier:

    @allure.title('Проверяем что при логировании возвращаетс id курьера')
    @allure.description('Отправляем запрос на создание и логирование созданного курьера. Проверяем что при логировании код ответа 200 и ответ содержит id курьера')
    def test_login_courier_login_and_password_return_id(self):
        courier = UtilsMethods()
        payload = courier.generate_random_data_user_json()
        response_create = ApiMethod.api_method_creat_courier(payload)
        response_login = ApiMethod.api_method_login_courier(payload["login"], payload["password"])
        assert response_login.status_code == 200
        assert 'id' in response_login.json()
        courier.delete_courier(courier.login_courier_and_return_id(payload["login"], payload["password"]))

    @allure.title('Проверяем получение ошибки при невреном пароле курьера и текст данной ошибки')
    @allure.description('Отправляем запрос который содержит не верный пароль, но верный логин. Проверяем что код ответа 404 и текст овтета ошибки соответсвует документации')
    def test_login_courier_no_correct_password_return_error(self):
        courier = UtilsMethods()
        payload = courier.generate_random_data_user_json()
        response_create = ApiMethod.api_method_creat_courier(payload)
        response_login = ApiMethod.api_method_login_courier(payload["login"], payload["password"][:5])
        assert response_login.status_code == 404
        assert response_login.json()['message'] == data.ERROR_MESSEGE_NO_CORRECT_PASSWORD
        courier.delete_courier(courier.login_courier_and_return_id(payload["login"], payload["password"]))

    @allure.title('Проверяем получение ошибки при невреном логине курьера и текст данной ошибки')
    @allure.description('Отправляем запрос который содержит не верный логин, но верный пароль. Проверяем что код ответа 404 и текст овтета ошибки соответсвует документации')
    def test_login_courier_no_correct_login_return_error(self):
        courier = UtilsMethods()
        payload = courier.generate_random_data_user_json()
        response_create = ApiMethod.api_method_creat_courier(payload)
        response_login = ApiMethod.api_method_login_courier(payload["login"][:5], payload["password"])
        assert response_login.status_code == 404
        assert response_login.json()['message'] == data.ERROR_MESSEGE_NO_CORRECT_LOGIN
        courier.delete_courier(courier.login_courier_and_return_id(payload["login"], payload["password"]))

    @allure.title('Проверяем получение ошибки если логин курьера не введен и текст данной ошибки')
    @allure.description('Отправляем запрос который  не содержит логин, но содержит верный пароль. Проверяем что код ответа 400 и текст овтета ошибки соответсвует документации')
    def test_login_courier_no_login_return_error(self):
        courier = UtilsMethods()
        payload = courier.generate_random_data_user_json()
        response_create = ApiMethod.api_method_creat_courier(payload)
        response_login = ApiMethod.api_method_login_courier(payload["login"][:0], payload["password"])
        assert response_login.status_code == 400
        assert response_login.json()['message'] == data.ERROR_MESSEGE_NO_LOGIN
        courier.delete_courier(courier.login_courier_and_return_id(payload["login"], payload["password"]))

    @allure.title('Проверяем получение ошибки если пароль курьера не введен и текст данной ошибки')
    @allure.description('Отправляем запрос который не содержит пароль, но содержит логин. Проверяем что код ответа 400 и текст овтета ошибки соответсвует документации')
    def test_login_courier_no_password_return_error(self):
        courier = UtilsMethods()
        payload = courier.generate_random_data_user_json()
        response_create = ApiMethod.api_method_creat_courier(payload)
        response_login = ApiMethod.api_method_login_courier(payload["login"], payload["password"][:0])
        assert response_login.status_code == 400
        assert response_login.json()['message'] == data.ERROR_MESSEGE_NO_PASSWORD
        courier.delete_courier(courier.login_courier_and_return_id(payload["login"], payload["password"]))