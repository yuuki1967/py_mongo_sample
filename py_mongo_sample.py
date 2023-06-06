import pymongo

myclent = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclent["mydatabase"]
mycol = mydb["customers"]
print(mydb.list_collection_names())
if "customers" in mydb.list_collection_names():
    print("The collection exists.") 
    for x in mycol.find():
        print(x.get("name"), x.get("email"), x.get("phone"), x.get("credit"))
else:
    print("The collection does not exists.")
    mydict = { "name": "Yuki Endo", "email": "yuuki1967@hoge.com", "phone": "090-1234-5679", "credit": "1111-2222-3333-4444" }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    
