__author__ = 'alex'

import _mysql

db =_mysql.connect(host="localhost",user="root",
                      passwd="password1",db="emailapp")

def viewOutbox(username):

    statement = 'select * from Messages where sender = '+"'"+ username + "';"
    db.query(statement)

    #print (statement)

    r = db.store_result()
    switch = 1
    while switch == 1:
        try:
            print r.fetch_row()[0]
        except:
            switch = 0

    return
