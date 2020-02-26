class User:
    active_users = 0
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
    def __repr__(self):
        return f'{self.first} is {self.age}'

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"
    def full_name(self):
        return f"{self.first} {self.last}"
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"
    def likes(self, thing):
        return f"{self.first} likes {thing}"
    def is_senior(self):
        return self.age >= 65
    def birthday(self):
        self.age += 1
        return f'Happy {self.age}th Birthday!'

user1 = User("Joe", "Rogan", 42)
user2 = User("Blanca", "Lopez", 28)

# print(user1.is_senior())
# print(user2.birthday())
# print(user2.age)
# print(User.active_users)
# print(user2.logout())
# print(User.active_users)
#
# User.display_active_users()
# print(User.display_active_users())
tom = User.from_string("Tom,Bradey,45")
# print(tom.first)
# print(tom.full_name())
print(tom)