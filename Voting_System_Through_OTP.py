import datetime # To vote at a certain time
import random as r #To create random otp importing rand
import smtplib # To send mail importing smtplib 

print("Welcome to Voting Centere")
print("You can cast vote from Morning 9:00 AM to Evening 6:00PM")
list = ["Manish", "Mukesh", "Amit", "Suresh"] # persons standing for voting
print("You need to verify OTP to vote")
now = datetime.datetime.now().time().hour # taking hours hand to vote from 9am to 6pm
if now >= 0 and now <= 23.59: # if user votes from 9am to 6pm
    user = input("Enter Your Name : ")  # Enter name
    email = input("Enter Your Email : ") # Enter email to verify and vote
    otp = "" # Declaring empty string to store otp
    for i in range(6): # for loop for creating a 6 digit otp 
        otp += str(r.randint(1, 9)) # pushing randing number 1 to 9 in string otp
    text = (f"Dear {user}, Your OTP for casting a vote is {otp}")# text that will be displayed to user in mail
    subject = "Verify OTP to vote" # subject for the mail
    message = 'subject : {}\n\n{}'.format(subject, text) 
    s = smtplib.SMTP('smtp.gmail.com', 587) # created a session encapsulate an SMTP connection, port 587 (port number for gmail)
    s.starttls() #TLS (Transport Layer Security) encrypts all the SMTP commands when started on s
    s.login("sahiramdukiya76@gmail.com", "gimbpbwnslqckjew")# Login with official account to mail the otp
    s.sendmail('&&&&&&&&&&&', email, message)# Sending mail to user that contains msg with otp
    print("Otp Sent!")
    otpverify = input("Enter OTP : ") # enter otp to verify
    count = 0 # declared count to take input 3 times only
    for i in range(2):
        if otpverify != otp: # if wrong OTP entered
            print("Invalid OTP")
            otp = ""
            for i in range(6): # for loop for generating otp
                otp += str(r.randint(1, 9)) # generating randon otp again
            text = (f"Dear {user}, Your OTP for casting a vote is {otp}")
            message = 'subject : {}\n\n{}'.format(subject, text)
            s.sendmail('&&&&&&&&&&&', email, message)
            print("New OTP Sent")
            otpverify = input("Enter New OTP : ")
        if otpverify == otp: # if correct otp entered 
            count = 1
            print("OTP Verified")
            break
    if count == 0:
        print("You have entered wrong OTP 3 times now you may try to vote tomorrow")
    elif count == 1:
        i = 1
        for cnadidate in list: # printing name of contesting persons iterating through loop
            print(str(i)+" : "+cnadidate+" ")
            i += 1
        CastedVote = int(input("Enter the persons serial number whom you want to vote : "))
        print("Your Vote Is casted Sucessfully")
        print("Vote Details : ")
        print(f"Casted by : {user}\nCasted to : {list[CastedVote-1]}")
        ifyes = input("You want to have Your vote detais through mail (Enter Yes/No) : ")
        ifyes = ifyes.upper() # updating if yes to upper case
        print("Thanks For Casting Your Valuable Vote")
        if ifyes == "YES": # if user desiers to get vote details through mail
            text = (
                f"Vote Details : \nCasted by : {user}\nCasted to : {list[CastedVote-1]}")
            subject = "Details of your vote"
            message = 'subject : {}\n\n{}'.format(subject, text)
            s.sendmail('&&&&&&&&&&&', email, message)
            print("Mail Sent Sucessfully")
else: # if voting time is over
    print("The Voting time is over Please cast your vote tomorrow")
