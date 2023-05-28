# class Category:
#     def __init__(self, name):
#         self.name = name
#         self.ledger = []

#     def deposit(self, amount, description=""):
#         self.ledger.append({"amount": amount, "description": description})

#     def withdraw(self, amount, description=""):
#         if self.check_funds(amount):
#             self.ledger.append({"amount": -amount, "description": description})
#             return True
#         return False

#     def get_balance(self):
#         balance = 0
#         for item in self.ledger:
#             balance += item["amount"]
#         return balance

#     def transfer(self, amount, category):
#         if self.check_funds(amount):
#             self.withdraw(amount, f"Transfer to {category.name}")
#             category.deposit(amount, f"Transfer from {self.name}")
#             return True
#         return False

#     def check_funds(self, amount):
#         return amount <= self.get_balance()

#     def __str__(self):
#         title = f"{self.name:*^30}\n"
#         items = ""
#         total = 0
#         for item in self.ledger:
#             items += f"{item['description'][:23]:23}" + f"{item['amount']:7.2f}" + "\n"
#             total += item["amount"]
#         output = title + items + "Total: " + str(total)
#         return output


# def create_spend_chart(categories):
#     # Calculate the spent percentage for each category
#     spent_percentages = []
#     total_withdrawals = 0

#     for category in categories:
#         withdrawals = 0
#         for item in category.ledger:
#             if item["amount"] < 0:
#                 withdrawals -= item["amount"]
#         spent_percent = (withdrawals / category.get_balance()) * 100
#         spent_percentages.append(spent_percent)
#         total_withdrawals += withdrawals

#     # Create the spending chart
#     chart = "Percentage spent by category\n"
#     for i in range(100, -10, -10):
#         chart += f"{i:3d}| "
#         for spent_percent in spent_percentages:
#             if spent_percent >= i:
#                 chart += "o  "
#             else:
#                 chart += "   "
#         chart += "\n"

#     # Create the horizontal line and category names
#     chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

#     max_len = max(len(category.name) for category in categories)
#     for i in range(max_len):
#         chart += "     "
#         for category in categories:
#             if i < len(category.name):
#                 chart += category.name[i] + "  "
#             else:
#                 chart += "   "
#         chart += "\n"

#     return chart

# food = Category("Food")
# clothing = Category("Clothing")
# auto = Category("Auto")

# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food")
# food.transfer(50, clothing)

# clothing.withdraw(25.55)
# clothing.withdraw(100)

# auto.deposit(1000)
# auto.withdraw(15)

# print(food)
# print(clothing)
# print(auto)

# print(create_spend_chart([food, clothing, auto]))





class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for transaction in self.ledger:
            items += f"{transaction['description'][:23]:23}" + f"{transaction['amount']:7.2f}" + "\n"
            total += transaction["amount"]
        output = title + items + "Total: " + str(total)
        return output


def create_spend_chart(categories):
    total_withdrawals = 0
    category_names = []
    spent_percentages = []

    for category in categories:
        withdrawals = 0
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                withdrawals += transaction["amount"]
        total_withdrawals += withdrawals
        category_names.append(category.name)
        spent_percentages.append(withdrawals)

    spent_percentages = [int((percent / total_withdrawals) * 10) * 10 for percent in spent_percentages]

    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3d}| "
        for percent in spent_percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_len = max(len(name) for name in category_names)
    for i in range(max_len):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")
food.transfer(50, clothing)

clothing.withdraw(25.55)
clothing.withdraw(100)

auto.deposit(1000)
auto.withdraw(15)

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))
