# user.py

class User:
    def __init__(self, userId, name, email, mobile_number):
        self.userId = userId
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.total_owe_amount = 0
        self.owe_dict = {}
        self.total_spend_amount = 0
        self.spend_dict = {}

    def put_owe(self, uid, amount):
        self.owe_dict[uid] = amount
        self.total_owe_amount += amount
    
    def remove_owe(self, uid, amount):
        self.total_owe_amount -= amount
        self.owe_dict[uid] -= amount
        if(self.owe_dict[uid] == 0):
            del self.owe_dict[uid]

    def put_spend(self, uid, amount):
        self.spend_dict[uid] = amount
        self.total_spend_amount += amount
    
    def remove_spend(self, uid, amount):
        self.total_spend_amount -= amount
        self.spend_dict[uid] -= amount
        if(self.spend_dict[uid] == 0):
            del self.spend_dict[uid]
    
    def __str__(self) -> str:
        initial_string = f"{self.userId} is \n"

        spend_string = f"Spending of {self.total_spend_amount}\n"

        owe_string = f'Owe of {self.total_owe_amount}\n'

        if(self.total_owe_amount > 0):
            owe_string += " Details of owe to other users,"

            for uid, amount in self.owe_dict.items():
                owe_string += f"\n{amount} owe to {uid}\n"
        
        

        return initial_string + spend_string + owe_string
    
    