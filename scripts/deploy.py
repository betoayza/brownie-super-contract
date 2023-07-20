from brownie import accounts, config, SuperContract, network


def deploy_super_contract():
    # account = accounts.load("nueva_cuenta_prueba") # PARA PRODUCCIÓN (ACTIVOS REALES)
    # account = accounts.add(os.getenv("PRIVATE_KEY")) # SOLO PARA DESARROLLO
    account = get_account()
    # SEGUNDA FORMA PARA DESARROLLO
    super_contract = SuperContract.deploy(
        {"from": account}
    )  # se especifica cuenta, porque es una transaccion que afecta la blockchain

    # Interactuando con el contracto (Blockchain)
    stored_number = (
        super_contract.getNumber()
    )  # transaccion tipo 'call' --> no hace falta especificar la cuenta
    print("Primer estado del valor almacenado:", stored_number)

    # cambiar valor almacenado
    txn_2 = super_contract.registerNumber(
        123, {"from": account}
    )  # se especfica cuenta, porque es una transaccion que afecta la blockchain

    txn_2.wait(
        1
    )  # Esperar a que la transaccion se completa para continuar (tanto para tesnets o mainnet)

    updated_number = super_contract.getNumber()
    print("El valor actualizado es:", updated_number)


def get_account():
    if network.show_active() == "development":
       return accounts[0] # la cuenta de desarrollo de Ganache
    else:
       return accounts.add(config["wallets"]["from_key"]) # usar cuenta real

def main():
    deploy_super_contract()
