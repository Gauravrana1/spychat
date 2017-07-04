import chat
while 1==1:
    print"###WELCOME BACK TO SPYCHAT###"
    print"SELECT OPTION"
    print"\t1.LOG IN:\n\t2.SIGN UP:"
    choose = raw_input("")
    if choose == "2" or choose == "2":
        i = False
        while i != True:
            spy_name = {
                'Name': '',
                'Salutation': '',
                'Age': 0,
                'Rating': 0.0
            }
            spy_name['name'] = raw_input("SPECIMEN REQUIRED\nEnter your  name: ")
            spy_name['salutation'] = raw_input("Mr/Mrs?: ")
            spy_name['name'] = spy_name['salutation'] + " " + spy_name['name']
            spy_name['age'] = int(raw_input("Age?"))
            spy_name['rating'] = float(raw_input("Spy rating?"))
            if len(spy_name['name']) > 0 and spy_name['age'] > 18 and spy_name["rating"] > 3:
                print"congratulation you in"

            else:
                print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
            spy_name = raw_input("create a username:")
            spy_password = raw_input("create a passoword:")
            print "running..."
            fob = open("spy.txt", 'a')
            fob.write("\n")
            fob.write(spy_name)

            fob.write("\n")
            fob.write(spy_password)
            fob.close()
            break;
    else:
        while 1==1:
            print "\nreading the line file once"
            fob = open("spy.txt",'r')
            fob.read()
            raw_input("Enter your user name:"),fob.read()
            raw_input("Enter you password:"),fob.read()
            fob.read()
            fob.close()
            break;


    chat.msg_check()

