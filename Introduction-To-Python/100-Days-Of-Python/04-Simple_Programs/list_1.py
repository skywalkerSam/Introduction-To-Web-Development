# List: States Of America...
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america)
print(states_of_america[0])
states_of_america.append("Dreamland")
print(states_of_america)
states_of_america.remove("Dreamland")
print(states_of_america)


# Dirty Dozen
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
print(dirty_dozen)

# Nested List
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Cherries", "Peaches" ,"Pears"]
vegetables = ["Spinach", "Kale", "Tomatos", "Celery", "Potatos"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)      #Matrix

#test
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)