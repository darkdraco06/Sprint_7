from api_methods import ApiMethod
import pytest
import data
import allure


class TestCreateOrder:
    @allure.title('Проверяем успешное создание заказа с набором парамтеров "Цвет самоката"')
    @allure.description('Отправляем запрос на создание заказа со всеми параметрами, кроме цвета самокат.Првоеряем что код ответа 201 и заказ создан')
    @pytest.mark.parametrize(
        'color',
        [
            [],
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"]
        ]
    )
    def test_create_order_four_color_order_create(self, color):
        data.ORDER_JSON_NO_COLOR['color'] = color
        response_order = ApiMethod.api_method_order_create(data.ORDER_JSON_NO_COLOR)
        assert response_order.status_code == 201
        assert 'track' in response_order.json()
