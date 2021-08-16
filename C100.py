class Car (object):
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelerate(self):
        print("Accelerate")
        
    def changeGear(self, gear_type):
        print("Gear Changed " + gear_type)

audi = Car("a6","red", "audi", 80)
print(audi.start())
print(audi.stop())
print(audi.accelerate())
print(audi.changeGear("second gear"))