class Vehicle:

    def __init__(self, owner, make, model, vin, cylinders, color, licplate):
        self.owner = owner
        self.make = make
        self.model = model
        self.vin = vin
        self.cylinders = cylinders
        self.color = color
        self.licplate = licplate

    def createOwner(self, name):
        self.owner = owner(name)

    def getMake(self, make):
        self.make = make

    def getModel(self, model):
        self.model = model

    def getVin(self, vin):
        self.vin = vin
        
    def getCylinders(self, cylinders):
        self.cylinders = cylinders

    def setColor(self, color):
        self.color = color

    def setLicPlate(self, licplate):
        self.licplate = licplate

    def describeTheVehicle(self):
        print ('Owner %s, Make %s, Model %s, Vin %s, Cylinders %s, Color %s, LicPlate %s' % (self.owner, self.make, self.model, self.vin, self.cylinders, self.color, self.licplate))



ford1 = Vehicle('Professor Kumar', 'Ford', 'F150', '1FTEW1E53LFA80314', 6, 'Black', 'ABC123')
ford1.describeTheVehicle()

ford2 = Vehicle('Mond Treje', 'Ford', 'Mustang', '1FA6P8CF5K5111613', 8, 'Red', 'G0F4ST')
ford1.describeTheVehicle()

ford3 = Vehicle('Jea Retre', 'Ford', 'Explorer', '1FATP8FF6G5312006', 8, 'Silver', 'SCRM0M')
ford3.describeTheVehicle()
print("")
print("After Paintjobs:")
print("")
ford1.setColor('Red')
ford1.describeTheVehicle()

ford2.setColor('Neon Green')
ford2.describeTheVehicle()

ford3.setColor('Purple')
ford3.describeTheVehicle()
