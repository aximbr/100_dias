import requests
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/0ae3ba4e02da96577e65ec9931229be4/flightDeals/users"


class UserManager:

    def __init__(self):
        self.user_data = {}
        self.last_object_id = 0
        
    def get_destination_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.user_data = data["users"]
        self.last_object_id = data["users"][-1]["id"]
        #print(self.user_data)
        #print(self.last_object_id)
        return self.user_data

    def add_user(self,name_first, name_last, email_user):
        next_object_id = self.last_object_id + 1
        new_user = {
                "user": {
                    "firstName": name_first,
                    "lastName" : name_last,
                    "email" : email_user
                }
            }
        response = requests.post(
                url=f"{SHEETY_USERS_ENDPOINT}/",
                json=new_user
            )
        if response.ok :
            self.last_object_id = next_object_id
      
        
    
    # def update_destination_codes(self):
    #     for user in self.user_data:
    #         new_data = {
    #             "user": {
    #                 "firstName": user["First Name"],
    #                 "lastName" : user["Last Name"],
    #                 "email" : user["Email"]
    #             }
    #         }
    #         response = requests.put(
    #             url=f"{SHEETY_USERS_ENDPOINT}/{city['id']}",
    #             json=new_data
    #         )
    #         print(response.text)
#main()

usermanager = UserManager()
data_user = usermanager.get_destination_data()
usermanager.add_user("Pedro", "Da Silva", "t5678@domain.com")
data_user = usermanager.get_destination_data()
