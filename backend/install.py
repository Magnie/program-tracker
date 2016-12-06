from constants import *

try:
    import pip
except:
    print "Missing pip! Please install it before installing the Program Tracker."
    exit()

def check_dependencies():
    print "Checking dependencies..."
    to_install = []

    try:
        import pymongo
    except:
        to_install.append('pymongo')

    try:
        import bottle
    except:
        to_install.append('bottle')
    
    return to_install

def install(package):
    pip.main(['install', package])

def install_dependencies(to_install):
    print "Installing dependencies..."
    for dependency in to_install:
        print "Installing {0}...".format(dependency)
        install(dependency)
    
    print "Dependencies have been installed."

def setup_database():
    from pymongo import MongoClient
    from pymongo import DESCENDING
    client = MongoClient()
    db_name = raw_input("Database Name: ")
    database = client[db_name]
    
    if database.members.find().count() > 0:
        print "Accounts already exist for this setup! Exiting.."
        exit()
    
    print "Now to set up the database."
    
    name = raw_input("Enter the admin name: ")
    username = raw_input("Enter the admin username: ")
    password = hash_password(raw_input("Enter the admin password: "))
    print "Creating admin account..."
    
    member = {
        'name': name,
        'username': username,
        'password': password,
        'access_level': LEVEL_ADMIN,
        'programs': [],
        'current_program': None,
        'earned': [],
    }
    database.members.insert(member)
    
    print "Admin account created!"

def main():
    to_install = check_dependencies()
    if to_install:
        install_dependencies(to_install)
    else:
        print "No dependencies to install!"
    
    global pymongo
    import pymongo
    
    setup_database()
    
    print "Setup is complete! Please login to the Admin Account to add programs and groups."
    
if __name__ == '__main__':
    main()
