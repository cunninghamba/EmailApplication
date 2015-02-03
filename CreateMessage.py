__author__ = 'richard'

import _mysql

db =_mysql.connect(host="localhost",user="root",
                      passwd="password1",db="emailapp")

def createMessage(username):

    print ('')

    print ('Enter the recipient of your message')
    recipient = raw_input()
    print ('Enter the body of your message')
    body = raw_input()

    print ('')

    statement = "insert into Messages values( 0, '" + recipient + "', '" + username + "', '" + body + "', NOW())"
    print (statement)
    db.query(statement)


    return
