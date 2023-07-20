from brownie import SuperContract, accounts


def test_deploy():
    # 1) Arrange -> organizar
    account = accounts[0]
    # 2) Act -> hacer algo
    super_contract = SuperContract.deploy({"from": account})
    starting_value = super_contract.getNumber()
    expected = 0
    # 3) Assert -> validar que sea cierto
    assert starting_value == expected


def test_update_number():
    # 1) Arrange
    account = accounts[0]
    # 2) Act
    super_contract = SuperContract.deploy({"from": account})
    txn = super_contract.registerNumber(123, {"from": account})
    txn.wait(1)
    expected = 123
    # 3) Assert
    assert super_contract.getNumber() == expected
