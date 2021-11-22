import logging

from banking.bank import Bank
from banking.controller import BankController
from banking.commands import Deposit,Withdrawal,Transfer, Batch

# create logger
try:
    logging.basicConfig(level=logging.INFO,  format="{asctime} - {name} - {levelname} - {message}",  style='{')
    logger = logging.getLogger("BANKING")
except Exception as error:
    print(f"{error}")

def main()-> None:
    logger.info("Banking App Started")

    try:
    
        # create a bank
        bank = Bank()

        # create a controller
        controller = BankController()

        # create some accounts
        account_amy = bank.create_account("Amy Farafowler")
        account_sheldon = bank.create_account("Sheldon Cooper")
        account_raj = bank.create_account("Rajesh Koothrapalli")

        # Deposit Money
        controller.execute(Deposit(account_amy, 100000))
        controller.execute(Deposit(account_sheldon, 100000))
        controller.execute(Deposit(account_raj, 100000))

        # TransferMoney
        controller.execute(Transfer(from_account=account_sheldon, to_account=account_amy, amount=50000))

        # Withdraw Money
        controller.execute(Withdrawal(account=account_raj,amount=2000))
        logger.info(bank)

        # undo last withdrawal
        controller.undo()
        logger.info(bank)

        # deposit , undo and redo
        controller.execute(Deposit(account=account_raj, amount=2100))
        logger.info(bank)
        controller.undo()
        logger.info(bank)
        controller.redo()
        logger.info(bank)

        # Batch commands
        controller.execute(Batch(commands=[Deposit(account=account_raj, amount=2100), Withdrawal(account=account_raj,amount=200), Transfer(from_account=account_sheldon, to_account=account_amy, amount=500)]))
        logger.info(bank)

        controller.undo()
        logger.info(bank)
    except Exception as error:
        logger.error(f"{error}")
        raise error

   
if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        logger.error(f"{error}")