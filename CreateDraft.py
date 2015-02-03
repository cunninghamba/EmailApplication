__author__ = 'rashawn'

import _mysql

db =_mysql.connect(host="localhost",user="root",
                      passwd="password1",db="emailapp")

def createDraft(username):

    print ('')

    print ('Enter the body of your message')
    body = raw_input()

    print ('')

    statement = "insert into Drafts values( 0, '" + username + "', '" + body + "', NOW())"

    #print (statement)

    db.query(statement)

    return
