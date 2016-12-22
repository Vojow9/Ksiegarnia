from bson import ObjectId

class DBItemIdParser():

    #changes {'_id': ObjectId('5836047157aac220c4c87380'), 'name': 'Joanne Rowling', 'description': 'harrego pottera napisala'},
    #to {"id": "5836047157aac220c4c87380", "name": "Joanne Rowling","description": "harrego pottera napisala"}
    def ObjectIdToStr(collection):
        try:
            collection['id']=str(collection['_id'])
            del collection['_id']
        except KeyError:
            pass
        return collection

    #convert default DBobject with strange id representation to nice id representation
    def prettyIdRepresentation(collection):
        if isinstance(collection,list):
            return [DBItemIdParser.prettyIdRepresentation(item) for item in collection] # tu mamy liste
        elif isinstance(collection,dict):
            collection = DBItemIdParser.ObjectIdToStr(collection)
            for i in collection:
                if isinstance(collection[i],list):
                    if ObjectId in [type(j) for j in collection[i]]: # for example [ObjectId('5836047157aac220c4c87380'), ObjectId('5836047157aac220c4c87380')] -can be list of authors
                        collection[i] = [str(a) for a in collection[i]]
                    elif '_id' in collection[i]: #just normal item id within, for example {'_id': ObjectId('5836047157aac220c4c87380'), 'name': 'Joanne Rowling', 'description': 'harrego pottera napisala'},
                        collection[i] = [DBItemIdParser.prettyIdRepresentation(item) for item in collection]
            return collection
