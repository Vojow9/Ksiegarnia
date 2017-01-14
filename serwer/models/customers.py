from models.model import Model
from passlib.hash import pbkdf2_sha256
import json

class Customers(Model):

    collection = Model.db.customers

    def isValidUserForm(user):
        try:
            user = json.loads(str(user,'utf8'))
            for o in (user["username"], user["username"],
             user["password"], user["first_name"], user["email"]):
                if not Model.properLenOfObject(o):
                    print(o)
                    assert False
            if not Model.properLenOfObject(user["address"], max_len = 60):
                assert False
            if not '@' in user["email"]:
                assert False
            if (not 'Female' in user["gender"]) and (not "Male" in user["gender"]):
                assert False
            return True
        except:
            return False

    def usernameIsUsed(username):
        if Customers.collection.find_one({'username':username}) is not None:
            return True
        else:
            return False

    def createCustomer(new_user):
        if not Customers.isValidUserForm(new_user):
            return 400
        new_user = json.loads(str(new_user,'utf8'))
        if Customers.usernameIsUsed(new_user['username']):
            return 409
        new_user['password'] = pbkdf2_sha256.hash(new_user['password'])
        new_user['canAddBooks'] = False
        Customers.collection.insert_one(new_user)
        return 201
