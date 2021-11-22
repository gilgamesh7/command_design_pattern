import logging
# import logging.config

from banking.bank import Bank


def main()-> None:
    # create logger
    # logging.config.fileConfig('logger.conf')
    # logger = logging.getLogger("BankingApp")
    logging.basicConfig(level=logging.INFO,  format="{asctime} - {name} - {levelname} - {message}",  style='{')
    logger = logging.getLogger("BANKING")
    logger.info("Banking App Started")

    
    # create a bank
    bank = Bank()

    # create some accounts
    account_amy = bank.create_account("Amy Farafowler")
    account_sheldon = bank.create_account("Sheldon Cooper")
    account_raj = bank.create_account("Rajesh Koothrapalli")

    # deposit money
    account_amy.deposit(4300)
    account_sheldon.deposit(129)
    account_raj.deposit(499)

    # withdraw money
    account_amy.withdraw(100)
    account_sheldon.withdraw(29)
    account_raj.withdraw(99)

    logger.info(bank)
if __name__ == "__main__":
    main()