#Class animal
class animal:
    def __init__(self, name, arms,legs,eyes,tail,furry ):
        self.name = name
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.furry = furry

    def describe(self):
        print("Animal: ",self.name)
        print("Arm Lenght:", self.arms)
        print("Leg Lenght:", self.legs)
        print("Number of Eyes:", self.eyes)

        if self.tail:
            print("This animal has a tail")
        else:
            print("This animal has no tail")

        if self.furry:
            print("This animal has furr")
        else:
            print("This animal has no furr")

#Create the Favorite Animal
owl = animal("Owl",6.5,2.7,2,True,False)
#Call the describe Method
owl.describe()

