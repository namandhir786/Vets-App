from customer import Customer
from mongo import MongoDBHelper
from bson.objectid import ObjectId

def main():
    db = MongoDBHelper()

    message = """
    1.Insert Data in database
    2.Delete Data in database
    3.Fetch all data from database
    """
    print(message)
    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        customer = Customer()
        customer.read_customer_data()

        document = vars(customer)
        db.insert(document)
        print("Database Inserted Successfully")
    elif choice == 2:
        query = {'phone': '+917684525487'}
        db.delete(query)
        print("Database deleted")
    elif choice == 3:
        #query = {'phone': '+918287657820'}

        query = {'_id': ObjectId('64c406b9ac00b4277c899385')}

        db.fetch(query=query)
        print("All databases fetched")
    elif choice == 4:
        query = {'phone': '+918287657820'}
        db.fetch(query=query)
        document_data_to_update = {'name': 'Sham', 'age': 38}
        db.update(document_data_to_update, query)
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()