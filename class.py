class Budget: 
    
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment

    def deposit(self):
        funds = input('kindly enter your budget\n')
        print ('your curent baalnce='+  funds)

    def withdraw(self):
        spend = input('how much will you like to take out?\n')
        print('your funds has been withdrawn')
    def transfer(self):
            trans = input('how much do you want to transfer?\n')
            print('your transfer was succesful')
        
food = Budget(1000, 2000, 3000 )
clothing= Budget(4000, 5000, 6000)
entertainment = Budget(7000, 5000, 6000)

print(food.deposit())