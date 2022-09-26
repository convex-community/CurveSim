import boa
import pytest


@pytest.fixture(scope="module")
def vyper_pool():
    return boa.load("contracts/PoolCalcs.vy")


@pytest.fixture()
def sample_pool_state():
    return {
        "A": 2000,
        "balances": [
            295949605740077243186725223,
            284320067518878 * 10**12,
            288200854907854 * 10**12,
        ],
        "balances_no_precision": [
            295949605740077243186725223,
            284320067518878,
            288200854907854,
        ],
        "total_supply": 849743149250065202008212976,
        "expected_virtual_price": 1022038799187029697
    }
