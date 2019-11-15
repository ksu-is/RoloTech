print('|-----Welcome to Diego\'s Address Book-------|')
print('|--------------------------------------|')
print('|Please choice from the following:-----|')
print('|----------1: Find Contacts------------|')
print('|----------2: Add Contacts-------------|')
print('|----------3: Delete Contacts----------|')
print('|----------4: Quit Address Book--------|')


phone = {'Thomas Dominic':"846-354-8654",'Diego Fajardo':"404-336-8594",'Pamela Whitten':"156-351-5356"}
ig_username= {'Thomas Dominic':"Thomas_llamas",'Diego Fajardo':"diego_lden",'Pamela Whitten':"pam_fam"}
twitter_user= {'Thomas Dominic':"tom_and_jerry","Diego Fajardo": "Go_Diego_Go", 'Pamela Whitten': "writ_by_whit"}
while 1:
    i = int(input('Can I help you?'))
    if i == 1:
        x=input('What\'s his/her name?')
        if x in phone:
            print("phone number: ", phone[x])
        if x in ig_username:
            print("instagram username: ", ig_username[x])
        if x in twitter_user:
            print("twitter username: ", twitter_user[x])
        else:
            print('Contact does not exist!')

    if i == 2:
        x = (input('New Contact name?'))
        if x in phone:
            z = str(input('Contact'+x+' with phone number: '+str(phone[x])+ 'and instagram username: '+str(ig_username[x])+' and twitter username: '+str(twitter_user[x])+'already existed, do you want to override?(Yes/No)'))
            if z.lower() == 'yes':
                phone[x] = input('New number?')
            if z.lower() == 'yes':
                ig_username[x] = input('New instagram username?')
            if z.lower() == 'yes':
                twitter_user[x] = input('New twitter username?')
            elif z.lower() == 'no':
                continue
            else:
                print('Please choose yes or no')
        else:
            phone[x] = input('New number?')
            ig_username[x] = input('New instagram username?')
            twitter_user[x] = input('New twitter username?')

    if i == 3:
        z = input('Who do you want to delete?')
        if z in phone:
            del phone[z]
            del ig_username[z]
            del twitter_user[z]
        else:
            print('Contact does not exist!')

    if i == 4:
        print("Goodbye!")
        break
