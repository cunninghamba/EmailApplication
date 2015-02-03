__author__ = 'brandon'

import Login
import ViewInbox
import ViewOutbox
import ViewDrafts
import CreateMessage
import CreateDraft
import Logout


def menu():

    print ('1. Create New Message')
    print ('2. View Inbox')
    print ('3. View Outbox')
    print ('4. View Drafts')
    print ('5. Create Draft')
    print ('6. Logout')

    choice=raw_input("What would you like to do? ")
    if choice=="1":
      print("\n You selected Create New Message")
      CreateMessage.createMessage(session_username)
    elif choice=="2":
      print("\n You selected View Inbox")
      ViewInbox.viewInbox(session_username)
    elif choice=="3":
      print("\n You selected View Outbox")
      ViewOutbox.viewOutbox(session_username)
    elif choice=="4":
      print("\n You selected View Drafts")
      ViewDrafts.viewDrafts(session_username)
    elif choice=="5":
      print("\n You selected Create Draft")
      CreateDraft.createDraft(session_username)
    elif choice=="6":
      print("\n You selected Logout")
      Logout.logout()
    elif choice !="":
      print("\n Not Valid Choice Try again")
      menu()
    menu()

print ('Welcome to the AB Emailing Service')
print ('To save money, we made this')
print ('')

session_username = Login.login()

print (session_username)

menu()