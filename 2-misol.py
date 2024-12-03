class Car:
    def __init__(self, brand: str, speed: int):
        self.__brand = brand
        self.__speed = speed

    def accelerate(self):
        self.__speed += int(input("Tezlikni qanchaga oshirmoqchisiz: "))
        if self.__speed > 200:
            print("Tezlikni 200 dan oshirib bo'lmaydi")
        else:
            print(f"Tezlik: {self.__speed} km/h")

    def brake(self):
        self.__speed -= int(input("Tezlikni qanchaga kamaytirmoqchisiz: "))
        if self.__speed < 0:
            print("Tezlikni 0 dan kamaytirib bo'lmaydi")
        else:
            print(f"Tezlik: {self.__speed} km/h")

    def get_speed(self):
        return self.__speed


car = Car("Lamborghini", 0)
car.accelerate()
car.brake()
print(f"Moshina brendi: {car.__brand}")
print(f"Tezlik: {car.get_speed()} km/h")