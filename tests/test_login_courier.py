from api_methods import ApiMethod
import data
import allure
import pytest


class TestLoginCourier:

    @allure.title('Проверяем что при логировании возвращаетс id курьера')
    @allure.description('Отправляем запрос на создание и логирование созданного курьера. Проверяем что при логировании код ответа 200 и ответ содержит id курьера')
    def test_login_courier_login_and_password_return_id(self, courier):
        ApiMethod.api_method_creat_courier(courier)
        response_login = ApiMethod.api_method_login_courier(courier["login"], courier["password"])
        assert response_login.status_code == 200
        assert 'id' in response_login.json()

    @allure.title('Проверяем получение ошибки при невреном пароле курьера и текст данной ошибки')
    @allure.description('Отправляем запрос который содержит не верный пароль, но верный логин. Проверяем что код ответа 404 и текст овтета ошибки соответсвует документации')
    def test_login_courier_no_correct_password_return_error(self, courier):
        ApiMethod.api_method_creat_courier(courier)
        response_login = ApiMethod.api_method_login_courier(courier["login"], courier["password"][:5])
        assert response_login.status_code == 404
        assert response_login.json()['message'] == data.ERROR_MESSEGE_NO_CORRECT_PASSWORD


    @allure.title('Проверяем получение ошибки при невреном логине курьера и текст данной ошибки')
    @allure.description('Отправляем запрос который содержит не верный логин, но верный пароль. Проверяем что код ответа 404 и текст овтета ошибки соответсвует документации')
    def test_login_courier_no_correct_login_return_error(self, courier):
        ApiMethod.api_method_creat_courier(courier)
        response_login = ApiMethod.api_method_login_courier(courier["login"][:5], courier["password"])
        assert response_login.status_code == 404
        assert response_login.json()['message'] == data.ERROR_MESSEGE_NO_CORRECT_LOGIN


    @allure.title('Проверяем получение ошибки если логин курьера не введен и текст данной ошибки')
    @allure.description('Отправляем запрос который  не содержит логин, но содержит верный пароль. Проверяем что код ответа 400 и текст овтета ошибки соответсвует документации')
    @pytest.mark.parametrize("login, password", [("", "test_password"), ("test_login", "")])
    def test_login_courier_no_login_return_error(self, login, password):
        response_login = ApiMethod.api_method_login_courier(login, password)
        assert response_login.status_code == 400
        assert response_login.json()['message'] == data.ERROR_MESSEGE_NO_DATA
