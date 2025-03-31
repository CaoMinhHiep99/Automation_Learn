class Owner:
    def __init__(self, key = False, license = False):
        self.key = key
        self.lisence = license
        print(self.key)


    def drive(self, license):
        if license == True:
            print('Start drive the car')
