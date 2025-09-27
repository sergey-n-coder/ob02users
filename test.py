class User:
    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name
        self.__access_level = 'user'

    def userid(self):  return self.__id
    def getname(self):  return self.__name

employee_1 = User('U001', 'Иван Иванов')
employee_2 = User('U002', 'Иван Иванов')
users_list = [employee_1,employee_1]

print(employee_1.userid())
user_ids = list(x.userid() for x in users_list)
user_ids.pop(1)

print(user_ids)