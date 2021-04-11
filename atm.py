
name = input("What is your name?\n")
allowedusers = ['toms','obi','kate']
allowedpassword = ['passwordtoms','passwordobi','passwordkate']

if (name in allowedusers):
    password = input(" enter your password\n")
    userid = allowedusers.index(name)
    if (password == allowedpassword[userid]):
        import datetime
        x = datetime.datetime.now()
        print(x)

        print('welcome %s' %name)
        print('these are the options available:')
        print('1.withdrawal')
        print('2.deposit')
        print('3.COMPLAINTS')


        Selectedoption = int(input('please select an option:'))

           
        if Selectedoption == 1:
            wish = int(input("how much do you want to withdraw"))
            print('take your cash %s' %name)   
        elif Selectedoption == 2:
            deps = input("how much would you like to deposit?")
            print('current balance=' + deps)
        elif Selectedoption == 3:
            comps = input('what will you like to report?')
            print('thank you for contacting us') 
        else:
            print('invalid option selected, pls try again')
    else:
            print('incorrect password')

else:
    print('Name not found pls try again')

