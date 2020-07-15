"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order. Make it function with name as sortUSA(), return list of cities
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this: (Make it function with name as alphaAsia(), return list of cities)
1
American City
American City
2
Asian City - Country
Asian City - Country"""



# locations = {'North America': {'USA': ['Mountain View', 'Mountain View']}}
# locations['North America']['USA'].append('Atlanta')
# locations = {'North America': {'USA': ['Atlanta', 'Mountain View']}
# locations = {'Asia' : {'India': ['Bangalore']}}
# locations['Asia'] = {'China':['Shanghai']}
# locations['North America']['USA'].append('Atlanta')


# print("1")
locations = {'North America': {'USA': ['Atlanta', 'Mountain View']}, 'Asia': {'India':'Bangalore', 'China':'Shanghai'}}

def sortUSA():
    # print("1")
    USA = sorted(locations['North America'].values())
    for i in USA:
        return i
sortUSA()



# locations = {'Asia': {'India':'Bangalore', 'China':'Shanghai'}}


def alphaAsia():
    # print("2")
    
    result = []
    for i in sorted(locations['Asia'].values()):
        print(i)
        for j in locations['Asia']:
            output = ""
            if locations['Asia'][j] == i:
                output += i + " - " + j
                result.append(output)
    return result
 
alphaAsia()





