from api_methods import ApiMethod
import data
import allure
import pytest


class TestCreateCourier:

    @allure.title('Проверяем создание курьера')
    @allure.description('Отправляем запрос на создание курьера. Проверяем что при создании курьера получаем код ответа 200 и запись что курьер создан')
    def test_create_courier_one_courier_courier_create(self, courier):
        response = ApiMethod.api_method_creat_courier(courier)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Проверяем ошибку о не возможности создания двух курьеров с одинаковы логином')
    @allure.description('Отправляем запрос на создание курьера, потом отправляем запрос на создание еще одного курьера с таким же логином. Проверяем что при создании курьера с одинаковы логином получаем код ответа 409 и запись что логин уже занят')
    def test_create_two_courier_two_same_login_error_create(self, courier):
        response = ApiMethod.api_method_creat_courier(courier)
        response = ApiMethod.api_method_creat_courier(courier)
        assert response.status_code == 409
        assert response.json()['message'] == data.ERROR_MESSEGE_CREATE_COURIER_LOGIN_DUPLICATE

    @allure.title('Проверяем создание курьера без логина')
    @allure.description('Отправляем запрос на создание курьера не указав логин. Проверяем что при создании курьера получаем код ответа 400 и текст ответа ошибки соовтетвует документации')
    @pytest.mark.parametrize("no_data_for_create", [
                                    {"login": "", "password": "test_password", "firstName": "test_name"},
                                    {"login": "test_login", "password": "", "firstName": "test_name"}])
    def test_create_courier_no_login_error_create(self, no_data_for_create):

        response = ApiMethod.api_method_creat_courier(no_data_for_create)
        assert response.status_code == 400
        assert response.json()['message'] == data.ERROR_MESSEGE_CREATE_COURIER_NO_DATA




