from steganography.steganography import Steganography
from datetime import datetime

list_friend=[]
old_status = ["blind", "love", "sick"]
text =[]
current_status = None
lol = None
def msg_check():
    print"Starting hike chating"
    while 1 == 1:

        print"\t1.friend list\n\t2.Status update\n\t3.Inbox\n\t4.Back"
        choice = int(raw_input())
        if choice == 1:
            print"Opening firend list"

            while 1 == 1:
                print"\t1.Add-friend\n\t2.select friend\n\t3.back"
                option = int(raw_input())
                if option == 1:
                    new_friend = {
                        'name': '',
                        'salutation': '',
                        'age': 0,
                        'rating': 0.0,
                        'chat':[]
                    }
                    new_friend['name'] = raw_input("Enter your friend name: ")
                    new_friend['salutation'] = raw_input("Mr/Mrs?: ")
                    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
                    new_friend['age'] = int(raw_input("Age?"))
                    new_friend['rating'] = float(raw_input("Spy rating?"))
                    if len(new_friend['name']) > 0 and new_friend['age'] > 18 and new_friend['rating'] > 3:
                       list_friend.append(new_friend)

                       print "adding..."
                       print "your added to my friend list", '-' + new_friend['name']
                       print list_friend

                    else:
                        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
                        return [len(new_friend)]

                elif option == 2:
                    print "select a friend"
                    item_number = 1
                    for new_friend in list_friend:
                        print "%d.%s" % (item_number,new_friend['name'])
                        item_number = item_number + 1
                    friend_choice = raw_input("choose from your friends")

                    friend_choice_position=int(friend_choice)-1
                    print "selected friend %s" \
                          % list_friend[friend_choice_position]['name']
                elif option == 3:
                    print "starting hike chating"
                    print choice
                    break;
        elif choice == 2:
            while 1==1:
                print"Opening status update"
                print"\t1.update\n\t2.Old-status\n\t3.back"
                choose = int(raw_input())
                if choose == 1:
                    print"loading..."
                    new_message = raw_input("Enter new status:-")
                    old_status.append(new_message)
                    print"updating....", (new_message)
                    current_status = new_message
                    print "your current status:-" + current_status
                if choose == 2:
                    print old_status
                    print"select an old-status"
                    item = 1
                    for temp in old_status:
                        print "%d. %s" % (item, temp)
                        item = item + 1
                    spam = int(raw_input("Enter your choice:"))
                    new_message = old_status[spam - 1]
                    old_status.append(new_message)
                    print "Old-status updating... " + new_message
                    current_status = current_status
                    print "your current status:" + current_status
                    break;

                if choose ==3:
                    print "start hike chating"
                    print choice

        elif choice == 3:
            while 1==1:
                print "opening chat message"
                print "\t1. Sending message\n\t2. Read message\n\t3.Chat history\n\t4.back"
                select= int(raw_input())
                if select== 1:
                    item_number = 1
                    for new_friend in list_friend:
                        print "%d.%s" % (item_number, new_friend['name'])
                        item_number = item_number + 1
                    friend_choice = raw_input("choose from your friends")

                    friend_choice_position = int(friend_choice)
                    friend_choice_position = friend_choice_position -1
                    print "selected friend %s" \
                          % list_friend[friend_choice_position]['name']
                    original_image = raw_input("What is the name of the image?")
                    output_path = raw_input('output.jpg:')
                    text = raw_input("What do you want to say?")
                    Steganography.encode(original_image, output_path, text)
                    new_chat = {
                        "message": text,
                        "time": datetime.now(),
                        "delivered": True
                    }
                    list_friend[friend_choice_position]['chat'].append(new_chat)

                elif select== 2:

                    item_number = 1
                    for new_friend in list_friend:
                        print "%d.%s" % (item_number, new_friend['name'])
                        item_number = item_number + 1
                    friend_choice = raw_input("choose from your friends")

                    friend_choice_position = int(friend_choice)
                    friend_choice_position = friend_choice_position -1
                    output_path= raw_input("path of the output.jpg:")
                    text = Steganography.decode(output_path)
                    print "Decoded message :%s" % text
                    new_chat = {
                        "message": text,
                        "time": datetime.now(),
                        "delivered": True
                    }

                    list_friend[friend_choice_position]['chat'].append(new_chat)
                elif select==3:
                    #item = 1
                    print ("opening chat history")
                    item_number = 1
                    for new_friend in list_friend:
                        print "%d.%s" % (item_number, new_friend['name'])
                        item_number = item_number + 1
                    friend_choice = int(raw_input("choose from your friends"))
                    friend_choice = friend_choice - 2
                    for temp in list_friend[friend_choice]['chat']:
                        #
                        print "[%s] Message:%s" % (temp['time'],temp['message'])


                elif select==4:
                    print"start hike chating"
                    print choice
                    break;
        elif choice == 4:
            print choice
            break;

































