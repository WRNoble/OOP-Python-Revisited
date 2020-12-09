class Corgi:
    ears = 2
    legs = 4
    friendly = True

    def __init__(self, coat="light", eyes="brown", size="small"):
        self.coat = coat
        self.eyes = eyes
        self.size = size

    def sit(self):
        print("The dog has sit")

    def bark(self, sound):
        print(f'The dog barked {sound}ly')

dog_one = Corgi()
dog_one.sit()
dog_one.bark("loud")