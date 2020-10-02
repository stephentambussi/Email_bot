import yagmail
import os
state = True
i = 0
while (state):
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, "message"+str(i)+".txt")
    try:
        f = open(filename, "r")
        alias = f.readline().strip() #get alias
        print(alias)
        message = f.readlines() #get message
        message.pop(0) #remove alias from message
        yag = yagmail.SMTP({'stevetambussi@gmail.com':alias}, '$unny@1999')
        yag.send('Jason.RSR@gmail.com', 'Test bot', message)
        f.close()
        i += 1
    except FileNotFoundError:
        print('File does not exist')
        state = False

