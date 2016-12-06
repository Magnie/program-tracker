import hashlib

LEVEL_DEV = -1 # Can do more than Admin
LEVEL_ADMIN = 0 # Can do anything
LEVEL_SUPERLEADER = 1 # Can create groups and leader accounts
LEVEL_LEADER = 2 # Can create member accounts
LEVEL_MEMBER = 3 # Can fill out requirements completed

def hash_password(password):
    new_hash = hashlib.sha512()
    new_hash.update('03835323330363334363133') # pre-salt
    new_hash.update(password)
    new_hash.update('43536353936393136373735') # post-salt
    return new_hash.hexdigest()
