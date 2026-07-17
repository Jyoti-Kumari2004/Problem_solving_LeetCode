class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.medium=medium
        self.small=small

    def addCar(self, carType: int) -> bool:
        t=carType
        if t==3:
            ans=self.small>0
            self.small-=1
        elif t==2:
            ans=self.medium>0
            self.medium-=1
        else:
            ans=self.big>0
            self.big-=1
        return ans


        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)