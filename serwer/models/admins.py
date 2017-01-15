from models.model import Model
from passlib.hash import pbkdf2_sha256
import json
from bson.json_util import dumps

class Admins(Model):

    collection = Model.db.admins

    def isCredentialsValid(login, password):
        try:
            hash = Admins.collection.find_one({'login':login})['password']
            return pbkdf2_sha256.verify(password,hash)
        except:
            return False
