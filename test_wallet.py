

import pytest
from wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    """
    Return wallet isntance with a zero balance
    """
    return Wallet()


@pytest.fixture
def wallet():
    """
    Return a Wallet instance with a balance of 20
    """
    return Wallet(30)


@pytest.fixture
def my_wallet():
    """
    Return a wallet isntance with a zero balance
    """
    return Wallet()


@pytest.mark.parametrize("earned, spent, expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected


def test_default_initial_amount(wallet):
    assert wallet.balance == 30


def test_setting_initial_amount(wallet):
    assert wallet.balance == 30


def test_wallet_add_cash(wallet):
    wallet.add_cash(60)
    assert wallet.balance == 90


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 20


def test_wallet_spend_cash__on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(9)
