class User:
    def __init__(self, username: str = "admin", password: str = "1234abcd"):
        self.__username = username
        self.__password = password
    
    def set_pass(self):
        self.__password = input("Yangi parolni kiriting: ")
        if len(self.__password) < 8:
            print("Parol 8 ta belgidan iborat bo'lishi kerak")
        else: 
            print("Parol muvaffaqiyatli o'zgartirildi")
    def check_pass(self):
        password = input("Parolni kiriting: ")
        if password == self.__password:
            print("Parol to'g'ri")
        else:
            print("Parol noto'g'ri")
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password


user = User()
user.set_pass()
user.check_pass()
print(user.get_username())
print(user.get_password())



