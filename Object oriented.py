class Car():
    def __init__(self,brand,model,color,year):

        self.brand=brand
        self.model=model
        self.color=color
        self.year=year
    def show (self):
        print (f"brand is :{self.brand}")
        print (f"model is :{self.model}")
        print (f"color is :{self.color}")
        print (f"year is :{self.year}")
        print("_"*30)

    def move (self):
         print (f"{self.brand} move")

    def beep (self):
        print ("beeeeeep")

car_1 = Car(brand="benz",model="g class",color="red",year=2022)
car_1 .show()
car_1 .move()
car_1 .beep()