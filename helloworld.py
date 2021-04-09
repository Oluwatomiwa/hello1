name = input("What is your name?\n")
allowedusers = ['toms','obi','kate']
allowedpassword = ['passwordtoms','passwordobi','passwordkate']

if (name in allowedusers):
    password = input(" enter your password\n")
    userid = allowedusers.index(name)
    if (password == allowedpassword[userid]):
        print('welcome %s' %name)
        print('these are the options available:')
        print('1.Withdrawal')
        print('2.Deprosit')
        print('3.COMPLAINTS')


        Selectedoption = int(input('please select an option:'))

           
        if Selectedoption == 1:
            print('you selected %s' %Selectedoption)
           
        elif ('Selectedoption == 2'):
            print('you selected %s' %Selectedoption)
            
        elif ('Selectedoption == 3'):
            print('you selected %s' %Selectedoption)
            
        else:
            print('invalid option selected, pls try again')
    else:
            print('incorrect password')

else:
    print('Name not found pls try again')



