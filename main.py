class User:
    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name
        self.__access_level = 'user'

    def userid(self):  return self.__id
    def getname(self):  return self.__name


class Admin(User):
    def __init__(self,admin_id,admin_name):
        super().__init__(admin_id,admin_name)
        #self.user_list = None
        self.__access_level='admin'
        self.users_list = []

    def add_user(self,user_id,name):
        new_user = User(user_id,name)
        if not user_id in list(x.userid() for x in self.users_list):
            self.users_list.append(new_user)
        else : print (f'Пользователь с ИД = {user_id} уже в списке')

    def del_user(self,user_id):
        # получить список ид пользователей и проверить на екзист
        user_ids = list(x.userid() for x in self.users_list)
        index = None
        if user_id in user_ids: index = user_ids.index(user_id)
        #print(user_ids)
        #print (index)
        if  not index  is None : self.users_list.pop(index)  #print (index) #
        else : print (f'Пользователя с ИД = {user_id} нет в списке')



    def get_list_users(self):
        for i in self.users_list: print(i.getname())

# Создание пользователя
employee_1 = User('U001', 'Иван Иванов')
# employee_1.userid()
admin_1 = Admin('A001', 'admin иванов')

admin_1.add_user('User2','новый пользователь2')
admin_1.add_user('User3','новый пользователь3')
admin_1.get_list_users()
print()
print('Удаление существующего')
admin_1.del_user('User3')
admin_1.get_list_users()
print()
print('Удаление НЕ существующего')
admin_1.del_user('User4')
admin_1.get_list_users()
print()
print('Добавление нового ')
admin_1.add_user('User5','новый пользователь5')
admin_1.get_list_users()
print()
print('Добавление дубля: ')
admin_1.add_user('User2','новый пользователь2')
admin_1.get_list_users()