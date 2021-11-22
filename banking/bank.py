from dataclasses import dataclass, field

from string import digits
from random import choices

from banking.account import Account

@dataclass
class Bank:
    accounts: dict[str,Account] = field(default_factory=dict)

    def create_account(self, name:str)-> Account:
        # number = "".join([choice(ascii_lowercase+ascii_uppercase+punctuation+digits) for _ in range(0,10)])
        number = "".join(choices(digits, k=12))
        account = Account(name, number)

        self.accounts[number] = account

        return account

    def get_account(self, account_number:str)-> Account:
        return self.accounts[account_number]
        
