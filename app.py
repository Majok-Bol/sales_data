import pandas as pd 
import numpy as np 
#reproducible dataset
np.random.seed(42)
users_data = {
    "user_id": [1,2,3,4,5,6,7,8,9,10],
    "name": [
        "John Doe","Jane Smith","Mike Brown","Alice Johnson","Robert Lee",
        "Linda Kim","David Miller","Sarah Wilson","Chris Evans","Emily Davis"
    ],
    "email": [
        "john.doe@gmail.com","jane_smith@yahoo.com",None,"alice@gmail.com",
        "robert.lee@outlook.com","linda.kim@gmail.com","david@gmail.com",
        "sarah@yahoo.com","chris@gmail.com","emily@gmail.com"
    ],
    "country": [
        "Kenya","USA","UK","Kenya","Canada",
        "South Korea","USA","UK","Kenya","USA"
    ],
    "signup_date": [
        "2024-01-05","2024-01-12","2024-02-01","2024-02-15","2024-03-01",
        "2024-03-05","2024-03-10","2024-03-15",None,"2024-03-25"
    ]
}
#convert to 2 dimensional table with rows and columns
users_data_df=pd.DataFrame(users_data)
#orders dataset
orders_data = {
    "order_id": [101,102,103,104,105,106,107,108,109,110],
    "user_id": [1,2,3,4,5,1,7,8,11,9],
    "order_date": [
        "2024-03-01","2024-03-02","2024-03-05","2024-03-07","2024-03-08",
        "2024-03-10","2024-03-12","2024-03-15","2024-03-18","2024-03-20"
    ],
    "order_status": [
        "Completed","Completed","Cancelled","Completed","Pending",
        "Completed","Completed","Completed","Completed","Completed"
    ]
}
#convert to 2 dimensional table with rows and columns
orders_df = pd.DataFrame(orders_data)
#order items dataset
order_items_data = {
    "item_id": [1,2,3,4,5,6,7,8,9,10],
    "order_id": [101,101,102,103,104,105,106,107,108,110],
    "product": [
        "Laptop","Mouse","Phone","Tablet","Laptop",
        "Keyboard","Monitor","Phone","Mouse","Laptop"
    ],
    "quantity": [1,2,1,1,1,1,2,1,1,1],
    "unit_price": [800,20,500,300,820,50,200,480,25,810]
}
#convert to 2 dimensional table with rows and columns
order_items_df = pd.DataFrame(order_items_data)
#payments dataset
payments_data = {
    "payment_id": [201,202,203,204,205,206,207],
    "order_id": [101,102,104,105,106,108,110],
    "payment_method": [
        "Credit Card","PayPal","Credit Card","Mpesa",
        "Credit Card","PayPal","Credit Card"
    ],
    "amount_paid": [840,500,820,50,400,25,None],
    "payment_status": [
        "Success","Success","Success","Failed",
        "Success","Success","Success"
    ]
}
#convert to 2 dimensional table with rows and columns
payments_df = pd.DataFrame(payments_data)

#convert to csv file
users_data_df.to_csv("users.csv",index=False)
orders_df.to_csv("orders.csv",index=False)
order_items_df.to_csv("order_items.csv",index=False)
payments_df.to_csv("payments.csv",index=False)
print("\nFile saved as users.csv\n")
print("\nFile saved as orders.csv\n")
print("\nFile saved as order_items.csv\n")
print("\nFile saved as payments.csv\n")