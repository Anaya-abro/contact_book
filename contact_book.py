
contacts = []
def add_contact():
    name = input('Enter the name:')
    number = input('Enter the phone number:')
    contacts.append({'Name': name,'Number': number})
    print('contact added!')


def view_contacts():
    for c in contacts:
        print(c['Name'],':',c['Number'])

def search_contacts():
    found = False
    find_contact = input('Which contact do you want to find:')
    for c in contacts:
        if c['Name'] == find_contact:
            print(c['Name'],':',c['Number'])
            found = True

    if found == False:
        print('Contact not found')
              



def delete_contacts():
    remove = input('What do you want to delete')
    for c in contacts:
        if c['Name'] == remove:
            contacts.remove(c)  
            print('Contact deleted')
            break
    else:
        print('contact not found')

while True:
  print('1, Add contacts')
  print('2, View contacts')
  print('3, Search contacts')
  print('4, Delete contacts')

  user = input('What do you want to do:') 
  if user == '1':
      add_contact() 

  elif  user == '2':
      view_contacts()


  elif user == '3':
      search_contacts()

  elif user == '4':
      delete_contacts()

  else:
      print('Invalid Text')   

  play_again = input('Do you want to play again:(yes/no)').lower()
  if play_again == 'no':
      print('Thank you')
      break























































































































































