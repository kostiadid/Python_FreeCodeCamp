class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.budget = 0

    def deposit(self, amount, description=''):
        self.budget += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True
        else:
            return False

    def get_balance(self):
        return self.budget

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def transfer(self, amount, another_category):
        if self.check_funds(amount):
            self.budget -= amount
            self.ledger.append(
                {'amount': -amount, 'description': f'Transfer to {another_category.category}'})
            another_category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    def __str__(self):
        string_output = ''
        title = self.category.center(30, '*')
        string_output += title
        string_output += '\n'

        for item in self.ledger:
            description = item["description"]
            amount = item["amount"]
            string_output += f'{description[0:23]:23}{amount:7.2f}'
            string_output += '\n'
        string_output += 'Total: '
        string_output += format(self.budget, '.2f')


        return string_output


food = Category("Food")
clothing = Category("Clothing")
auto = Category('Auto')

food.deposit(1000, "deposit")
food.withdraw(600, "groceries")
food.withdraw(165.60, "books")
food.withdraw(175.10, "books")

clothing.deposit(1000, "deposit")
clothing.withdraw(200, "groceries")

auto.deposit(1000, "deposit")
auto.withdraw(100, "groceries")

print(food)
print(clothing)
print(auto)

def create_spend_chart(categories):
    max_len = 0
    percentage = []

    for Cat in categories:
        percent = 0
        max_len = max(max_len, len(Cat.category))
        for item in Cat.ledger:
            if item["amount"] >=0:
                percent += item["amount"]
        if percent != 0:
            percent = (percent - Cat.budget)*100/percent
        percentage.append(int(percent))


    judul = 'Percentage spent by category  '
    str_output = judul
    space = ' '
    for i in range(10, -1, -1):
        space = '' if i == 10 else ' '
        if i == 0:
            space = '  '
        str_ = ''
        for num in range(len(percentage)):
            str_ += 'o  ' if i*10 <= percentage[num] else '   '
        str_output += f'\n{space}{i*10}| {str_}'
    str_output += f'\n    -{"-"*3*len(percentage)}'
    for num in range(max_len):
        str_cat = ''
        for i in range(len(categories)):
            str_cat += f'{categories[i].category[num]}  ' if num < len(categories[i].category) else '   '
        str_output += f'\n     {str_cat}'

    print(str_output)



create_spend_chart([food, clothing, auto])
