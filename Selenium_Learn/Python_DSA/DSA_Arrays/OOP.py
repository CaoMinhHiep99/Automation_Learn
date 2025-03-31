from Onwer import Owner

class Car(Owner):
    def __init__(self, name, model, color, key=False):
        super().__init__(key)
        self.name = name
        self.model = model
        self.color = color
    def start_engine(self):
        if self.key == True:
            print(f"{self.color} {self.name} {self.color} engine started")  
        else:
            print("Cannot start engine")
        
    def start_drive(self, license):
        Owner.drive(Owner,license)

my_car = Car('Toyota', 'Camry', 'Black', key=True)
my_car.start_engine()
my_car.start_drive(license=True)




# class (lớp) => attributes & methods # Constructor (Khởi tạo (init))

# Object (đối tượng)




# Inheritance (kế thừa): def start()

# Encapsulation (Đóng gói): _stop_service_with_systemctl    .__is_running()

# Polymorphism (Đa hình):

# Abstraction (trừu tượng):
