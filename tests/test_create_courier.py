import requests
from utils_methods import UtilsMethods
import curl
from api_methods import ApiMethod
import data
import allure


class TestCreateCourier:

    @allure.title('Проверяем создание курьера')
    @allure.description('Отправляем запрос на создание курьера. Проверяем что при создании курьера получаем код ответа 200 и запись что курьер создан')
    def test_create_courier_one_courier_courier_create(self):
        courier = UtilsMethods()
        payload = courier.generate_random_data_user_json()
        response = ApiMethod.api_method_creat_courier(payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        courier.delete_courier(courier.login_courier_and_return_id(payload["login"], payload["password"]))

    @allure.title('Проверяем ошибку о не возможности создания двух курьеров с одинаковы логином')
    @allure.description('Отправляем запрос на создание курьера, потом отправляем запрос на создание еще одного курьера с таким же логином. Проверяем что при создании курьера с одинаковы логином получаем код ответа 409 и запись что логин уже занят')
    def test_create_two_courier_two_same_login_error_create(self):
        courier = UtilsMethods()
        payload = courier.generate_random_data_user_json()
        response = ApiMethod.api_method_creat_courier(payload)
        response = ApiMethod.api_method_creat_courier(payload)
        assert response.status_code == 409
        assert response.json()['message'] == data.ERROR_MESSEGE_CREATE_COURIER_LOGIN_DUPLICATE
        courier.delete_courier(courier.login_courier_and_return_id(payload["login"], payload["password"]))

    @allure.title('Проверяем создание курьера без логина')
    @allure.description('Отправляем запрос на создание курьера не указав логин. Проверяем что при создании курьера получаем код ответа 400 и текст ответа ошибки соовтетвует документации')
    def test_create_courier_no_login_error_create(self):
        courier = UtilsMethods()
        payload = courier.generate_random_data_user_json()
        payload.pop("login")
        response = ApiMethod.api_method_creat_courier(payload)
        assert response.status_code == 400
        assert response.json()['message'] == data.ERROR_MESSEGE_CREATE_COURIER_NO_LOGIN

    @allure.title('Проверяем создание курьера без пароля')
    @allure.description('Отправляем запрос на создание курьера не указав пароль. Проверяем что при создании курьера получаем код ответа 400 и текст ответа ошибки соовтетвует документации')
    def test_create_courier_no_password_error_create(self):
        courier = UtilsMethods()
        payload = courier.generate_random_data_user_json()
        payload.pop("password")
        response = ApiMethod.api_method_creat_courier(payload)
        assert response.status_code == 400
        assert response.json()['message'] == data.ERROR_MESSEGE_CREATE_COURIER_NO_PASSWORD



