fruits_and_colours = {"apple": "red", "pear":"green", "banana":"yellow"}

print(fruits_and_colours["apple"])  #output is "red"

fruits_and_colours["Mandarin"] = "red"



empty_dictionary = {}

# Wipe an existing dictionary
#fruits_and_colours = {}

#print(fruits_and_colours)

# Edit an item in a dictionary
fruits_and_colours["apple"] = "yellow"

print(fruits_and_colours)

for key in fruits_and_colours:
    print(key) #output is apple,pear,banana,mandarin
    print(fruits_and_colours[key]) # output: apple yellow  pear  green  banana yellow  Mandarin red

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested list dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

print(travel_log["France"][1]) # Output is Lille

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][0]) #Output is C


travel_log2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

print(travel_log2["Germany"]["cities_visited"][2]) #Output is Stuttgart