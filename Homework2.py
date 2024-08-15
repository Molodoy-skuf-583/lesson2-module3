def send_email(message, recipient, sender='university.help.gmail.com'):
    if '@' not in (recipient or sender) or not sender.endswith(('.com', '.ru', '.net')):
        print(f'Unable to send email from {sender} to {recipient}')
    elif sender == recipient:
        print('You can not send a letter to yourself')
    elif sender == 'university.help.gmail.com':
        print(f'The letter was successfully sent from {sender} to {recipient}.')
    elif sender != 'university.help@gmail.com':
        print(f'NON-STANDARD SENDER! Message sent from {sender} to {recipient}.')


send_email('Good morning student', 'pedro123@gmail.com')
send_email('We invite you to spend your time productively', 'urban.fan.@mail.ru',
           sender='urban.info.@gmail.com')
send_email('Please, correct the task', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Hello me', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
