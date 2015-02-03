__author__ = 'brandon'

import _mysql
import sys

db =_mysql.connect(host="localhost",user="root",
                      passwd="password1",db="emailapp")

def login():

    username = raw_input('Enter your username: ')

    print(username)

    print ('')

    password = raw_input('Enter your password: ')

    print(password)

    statement = 'select * from Accounts where username = '+"'"+ username + "' and login_password = '"+ password + "';"

    db.query(statement)

    r = db.store_result()
    try:
        print r.fetch_row()[0]
    except:
        print ('Incorrect Login Validation')
        sys.exit(0)

    return username