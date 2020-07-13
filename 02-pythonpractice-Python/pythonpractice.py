"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []
    
    def addItem(self, item):
        self.items.append(item)
    
    def classiness(self):
        classiness = 0
        for item in self.items:
            if item == "tophat":
                classiness = classiness + 2
            elif item == "bowtie":
                classiness = classiness + 4
            elif item == "monocle":
                classiness = classiness + 5
            # else:
            #     classiness = 0
        return classiness

# a = Classy()

# a.classy("bowtie")
# print(a.calculate())




