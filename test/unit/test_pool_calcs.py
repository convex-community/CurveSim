import boa

from curvesim.pool import Pool


def _calc_virtual_price(D, total_supply):
    return D * 10**18 // total_supply


def test_get_D_against_prod(vyper_pool, sample_pool_state):
    """Test boa value against live contract."""

    D = vyper_pool.get_D(
        sample_pool_state["balances"], sample_pool_state["A"]
    )
    virtual_price = _calc_virtual_price(D, sample_pool_state["total_supply"])

    # Compare against virtual price since that's exposed externally
    # while `get_D` is internal in the contract.
    assert virtual_price == sample_pool_state["expected_virtual_price"]


def test_get_D(vyper_pool, sample_pool_state):
    """Test D calculation against vyper implementation."""

    virtual_balances = [
        sample_pool_state["balances"][0],
        sample_pool_state["balances"][1] * 10**12, 
        sample_pool_state["balances"][2] * 10**12
    ]
    
    # get vyper implementation calcs:
    expected_D = vyper_pool.get_D(
        virtual_balances, 
        sample_pool_state["A"]
    )
    
    # get python implementation calcs:
    pool = Pool(
        sample_pool_state["A"], 
        D=sample_pool_state["balances"], 
        n=3, 
        p=[10**18, 10**30, 10**30]
    )
    D = pool.D()
    
    assert expected_D == D
