class Vehicle:

    def __init__(self, make, model, vin, cylinders, color, lic_plate):
        self.make = make
        self.model = model
        self.vin = vin
        self.cylinders = cylinders
        self.color = color
    self.lic_plate = lic_plate

    def createOwner(self, name):
        persn = Person(name)

    def setColor(color):
        self.color = color

    def setLicPlate(self, lic_plate):
        self.lic_plate = lic_plate

    def getMake(self):
        return self.make

    def describeTheVehicle(self):
        print ('Make %s, Model %s, Color %s' % (self.make, self.model, self.color))



ford1 = Vehicle('Ford', 'F150', '12345', 6, 'Black', 'ABC123')
ford1.describeTheVehicle()
ford1.setColor('Red')
ford1.describeTheVehicle()

fordEx = Vehicle('Ford', 'Explorer', '454334', 4, 'Silver',87875)
fordEx.describeTheVehicle()

