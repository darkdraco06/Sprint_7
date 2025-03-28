import requests
import random
import string
import curl
from api_methods import ApiMethod
import allure


class UtilsMethods:

    @allure.step('Создаем курьера со случайыми: Логином, Паролем, Именем')
    def generate_random_data_user_json(self):

        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
        "login": login,
        "password": password,
        "firstName": first_name
        }
        return payload

    @allure.step('Логинемся под курьером и получаем его ID')
    def login_courier_and_return_id(self, login, password):
        response = ApiMethod.api_method_login_courier(login, password)
        return response.json()['id']

    @allure.step('Удаляем курьера')
    def delete_courier(self, id):
        response = ApiMethod.api_method_delete_courier(id)






