import pytest
from utils_methods import UtilsMethods


@pytest.fixture
def courier():
    courier = UtilsMethods()
    payload = courier.generate_random_data_user_json()
    yield payload

    if "login" in payload and "password" in payload:
        courier.delete_courier(courier.login_courier_and_return_id(payload["login"], payload["password"]))
    else:
        pass
