"""
Member Model
"""

from bson.objectid import ObjectId
from models.tools import *
from constants import *

class Member(object):
    versions = {
        1: {
            "version": int,
            "name": str,
            "access_level": int,
            "username": str,
            "password": str,
            "leader_of": list,
            "programs": list,
            "current_program": ObjectId,
            "earned": [
                {
                    "program": ObjectId,
                    "category": ObjectId,
                    "requirement": ObjectId,
                    "description": str,
                    "date_completed": str,
                    "verified_by": ObjectId,
                },
            ],
        },
    }
    
    version_scripts = {}
    
    version = 1
    structure = versions[version]
    raw_structure = dict((key, None) for key in structure)
    
    def __init__(self, data={}):
        # If the data has a version number, make sure it's the latest.
        if 'version' in data and data['version'] != self.version:
            self.data = self.update_latest(data)
        
        # Otherwise assume it is the latest.
        else:
            self.data = raw_structure.copy()
            self.data.update(data)
    
    def update_latest(data):
        if 'version' not in data:
            raise InvalidData("A current version must be provided.")
        
        version = data['version']
        for v in xrange(version + 1, self.version + 1):
            if v in self.version_scripts:
                data = self.version_scripts[v](data)
        
        return data
    
    def update_1(input_data):
        version = self.versions[1]
        
        data = {}
        for key in version:
            data[key] = None
        data.update(input_data)
        
        return data
    version_scripts[1] = update_1


class MemberManager(object):
    
    database = None
    structure = Member.structure
    
    def __init__(self):
        if not self.database:
            raise NoDatabaseSelected("No client was selected for Mongo.")
        
        self.collection = self.database.members
    
    def get_member_by_username(self, username):
        if type_valid(username, str):
            return self.collection.find_one({'username': username})
        
        raise InvalidData("")
    
    def get_member_by_id(self, member_id):
        if type_valid(member_id, str):
            data = self.collection.find_one({'_id': ObjectId(member_id)})
            member_data = self.check_member(data)
            return member_data
        
        raise InvalidData("")
    
    def check_login(self, username, password):
        if type_valid(username, str) and type_valid(password, str):
            conditions = {'username': username, 'password': hash_password(password)}
            if self.collection.find_one(conditions):
                return True
        
        return False
    
    def check_member(self, data):
        "Checks if the member is up to date. If not, update the database."
        member_data = Member.update_latest(data)
        if data != member_data:
            self.update_member(data['_id'], member_data)
        
        return member_data
    
    def create_member(self, data):
        if len(is_valid(data, self.structure)['errors']):
            raise InvalidData("")
        
        return self.collection.insert_one(data)
    
    def update_member(self, member_id, data):
        if 'version' in data and data['version'] != self.version:
            raise InvalidVersion("Member data is out of date.")
            data = self.check_player(data)
        
        if not is_valid(data, self.structure):
            raise InvalidData()
        
        if not type_valid(data['member_id'], str):
            raise InvalidData()
        
        self.collection.update(
            {'_id': ObjectId(member_id)},
            {'$set': data}
        )
    
    def delete_player(self, member_id):
        pass
