class Bus:

    def init(self, speed, capacity, seats):
        self.speed = speed
        self.capacity = capacity
        self.maxSpeed = maxSpeed
        self.passengers = []
        self.hasEmptySeats = True
        self.seats = seats

    def addPassenger(self, passenger):
        self.passengers.append(passenger)

    def removePassenger(self, passenger):
        self.passengers.remove(passenger)

    def setSpeed(self, newSpeed):
        if newSpeed >= 0 and newSpeed <= self.maxSpeed:
            self.speed = newSpeed
        else:
            print("Invalid speed.")