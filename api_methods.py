import requests
import curl
import allure

class ApiMethod:

    @staticmethod
    @allure.step('Выполняем запрос создания курьера')
    def api_method_creat_courier(payload):
        return requests.post(f'{curl.CREATE_COURIER}', data=payload)

    @staticmethod
    @allure.step('Выполняем запрос на удаление курьера')
    def api_method_delete_courier(id):
        return requests.delete(f'{curl.DELETE_COURIER}{id}')

    @staticmethod
    def api_method_login_courier(login, password):
        return requests.post(f'{curl.LOGIN_COURIER}', json={'login': login, 'password': password})

    @staticmethod
    @allure.step('Выполняем запрос на логин курьера')
    def api_method_order_create(order):
        return requests.post(f'{curl.CREATE_ORDER}', json=order)

    @staticmethod
    @allure.step('Выполняем запрос на получение списка заказов')
    def api_method_get_order():
        return requests.get(f'{curl.GET_ORDER}')

