stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop

stops.append("edinburgh Waverley")
stops.insert("Glasgow Queen St", 0)
stops.insert("Polmont", 3)
print(stops.index("Linlithgow"))
stops.pop("Livingston")
stops.pop(1)
print(len(stops))
stops
stops.reverse()
for stations in stops:
    print(stations)