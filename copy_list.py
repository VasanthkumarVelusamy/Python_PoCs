fruits = ['apple','orange','mango']

flowers = ['Jasmine','Rose','Lily']

# copying items of fruits in to fruits_copy
fruits_copy = fruits

# iterating over items in fruits_copy
for each in fruits_copy:
    print(each)

# Now, lets try to assign fruits list to flowers
flowers = fruits

for fruit in flowers:
    print(fruit)
