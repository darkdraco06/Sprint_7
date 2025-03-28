import requests
from utils_methods import UtilsMethods
import curl
from api_methods import ApiMethod
import data
import allure


class TestOrderList:
    @allure.title('Проверяем успешное получение списка заказов без указания парамтеров')
    @allure.description('Отправляем запрос на получение текущего списка заказов без парамтеров. Првоеряем что код ответа 200 и список заказов не пустой')
    def test_get_order_list_no_params_list_order_received(self):
        response_order_list = ApiMethod.api_method_get_order()
        order_list = response_order_list.json()
        assert response_order_list.status_code == 200
        assert order_list["orders"][0] != None