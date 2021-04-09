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

        print('invalid account or password')
        login()
    
def register():
    print('register')
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
    print('===============================')
    login()
def bankoperation(user):
    print('welcome %s %s' %(user[0], user[1]))

   
    selectedoption = int(input('what would you like to do? (1)withdrawal (2)deposit (3) logout\n'))

    if (selectedoption == 1):
         
        depositoperation()
    elif (selectedoption == 2):
          
        withdrawal()
    elif (selectedoption == 3):
         
        logout()
    elif (selectedoption == 4):
         
        exit()
    else:
            print('invalid option selected')
def withdrawal():
    print('withdrawal')


def depositoperation():
    print('deposit operation')


def generateaccountnumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()



## banking system

init()
