from bottle import request, response
from bottle import post, get, put, delete
from bson.json_util import dumps

import pymongo
from pymongo import MongoClient
from pymongo import DESCENDING
client = MongoClient()
db_name = 'fig'
database = client[db_name]

from models.members import MemberManager
MemberManager.database = database
member_manager = MemberManager()

# Home Page and Login
@get('/')
def index():
    logged_in = member_manager.check_login('josepha', 'awdsx123.')
    user = member_manager.get_member_by_username('josepha')
    
    response = {
        'logged_in': logged_in,
        'user': user,
    }
    return dumps(response)

@post('/auth/login')
def login():
    data = request.json
    logged_in = member_manager.check_login(data.username, data.password)
    
    response = {
        'logged_in': logged_in,
    }
    return dumps(response)

# Program APIs
@get('/programs/list')
def get_programs():
    pass

@get('/programs/get/<program_id>')
def get_program(program_id):
    pass

@put('/programs/create')
def create_program():
    pass

@delete('/programs/delete/<program_id>')
def delete_program(program_id):
    pass

@post('/programs/update/<program_id>')
def update_program():
    pass

# Group APIs
@get('/groups/list')
def get_groups():
    pass

@get('/groups/members/<group_id>')
def get_group_members(group_id):
    pass

@get('/groups/get/<group_id>')
def get_group(group_id):
    pass

@put('/groups/create')
def create_group():
    pass

@delete('/groups/delete/<group_id>')
def delete_group(group_id):
    pass

@post('/groups/update/<group_id>')
def update_group(group_id):
    pass

# Member APIs
@get('/members/list/<offset>')
def get_members(offset):
    pass

@get('/members/get/<member_id>')
def get_member(member_id):
    pass

@put('/members/create')
def create_member():
    pass

@delete('/members/delete/<member_id>')
def delete_member(member_id):
    pass

@post('/members/update/<member_id>')
def update_member(member_id):
    pass

# Requirements APIs
@get('/requirements/<program_id>/list')
def get_requirements(program_id):
    pass

@get('/requirements/get/<requirement_id>')
def get_requirement(requirement_id):
    pass
