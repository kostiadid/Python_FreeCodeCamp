class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self,amount , description=""):
        self.ledger.append({'amount':amount, 'description':description})
    
    def get_balance(self):
        total = 0
        for item in  self.ledger:
            total+= item['amount']
        return(total)


    def withdraw(self, amount, description=""):
        balance = self.get_balance()
        if  balance >= amount:
            self.ledger.append({'amount':-amount, 'description':description})
            return True  
        return False
    
    def transfer(self,amount, reciever):
        self.withdraw(amount,f'Transfer to {reciever.name}')
        reciever.deposit(amount,f'Transfer from {self.name}')
        return True

def create_spend_chart(categories):
    pass


    
