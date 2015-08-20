from pymongo import MongoClient

conn = MongoClient()
db = conn.client
data = db.client_data
def get_user():
    user = data.find({},{'user_id':1,'name':1,'_id':0})
    #for u in user:
    #    print u
    return user

def user_detail(u):
    user = data.find({'user_id':u},{'user_id':1,'name':1,'email':1,'phone_num':1,'_id':0})
    #for u in user:
    #    print u
    return user

def post_user(user,password):
    result = data.find({'user_id':user,'password':password},{'user_id':1,'name':1,'email':1,'phone_num':1,'_id':0}).count()
    #print result
    if result==1:
        return "True"
    else:
        return "False"
    
    #for u in user:
    #    print u
    #return user

def authenticate(user):
    result = data.find({'user_id':user}).count()
    #print result
    if result==1:
        return True
    else:
        return False
