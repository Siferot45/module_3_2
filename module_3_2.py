
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Checking for  email recipient correctness 
    if not ('@' in recipient and (recipient.endswith('.com') 
            or recipient.endswith('.ru') or recipient.endswith('.net'))):
        print(f"It is not possible to send an email from the address {sender} to the address {recipient}")
        return
    # Checking for  email sender correctness 
    if not ('@' in sender and (sender.endswith('.com') 
            or sender.endswith('.ru') or sender.endswith('.net'))):
        print(f"It is not possible to send an email from the address {sender} to the address {recipient}")
        return

    # Checking for sending to yourself
    if recipient == sender:
        print("You can't send a letter to yourself!")
        return

    # Checking for the sender by default
    if sender == "university.help@gmail.com":
        print(f"The email was successfully sent from the {sender} address to the {recipient} address")
    else:
        print(f"A NON-STANDARD SENDER! The email was sent from {sender} to {recipient}")
        

send_email('This is a communication verification message', 'vasyok1337@gmail.com')

send_email('You see this message as the best student of the course!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Please correct the assignment', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('I remind myself about the webinar', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
