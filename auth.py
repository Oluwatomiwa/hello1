#register
#username and password, email
#genarate user id
#login
#account number and password

#bank operations

database = {} #dictionary
import random
def init():

    print('welcome to bank t')

    haveaccount = int(input('do you have an account with us? 1=yes 0=no\n'))

    if(haveaccount == 1):
            
            login()
    elif(haveaccount == 0):
           
            print(register())
    else:
          print('you have selected invalid option')
          
def login():
    print('login into your account')
    accountnumberfromuser = int(input('what is your account number\n'))
    password = input('what is your password\n')

    for accountnumber,userdetails in database.items():
        if(accountnumber == accountnumberfromuser):
            if(userdetails[3]== password):
                bankoperation(userdetails)
        else:
            print('invalid account number or password')
            login()
    
def register():
    print('Kindly register your account')
    email = input('what is your email\n')
    first_name = input('whats is your first name\n')
    last_name = input('what is your last name\n')
    password = input('kindly create your password\n')

    accountnumber = generateaccountnumber()

    database[accountnumber] =[first_name, last_name, email, password]
    print('your account has been created')
    print('==============================')
    print('your account number is %d' %accountnumber)
    print('Make sure you keep it safe')
    login()
def bankoperation(user):
    print('welcome %s %s' %(user[0], user[1]))

   
    selectedoption = int(input('what would you like to do? (1)withdrawal (2)deposit (3) logout\n'))

    if (selectedoption == 1):
        withdrawal(user)
    elif (selectedoption == 2):
        depositoperation(user)
    elif (selectedoption == 3):
         
        logout()
    elif (selectedoption == 4):
         
        exit()
    else:
            print('invalid option selected')
def withdrawal(user):
    withdraw = int(input("how much will you like to withdraw?\n"))
    print('pls take your cash %s' %user[0])

def depositoperation(user):
    deps = input('how much will you like to deposit? \n')
    print('your current balance is=' + deps)


def generateaccountnumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()



## banking system

init()
