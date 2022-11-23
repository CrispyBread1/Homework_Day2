united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom[1]["capital"] = "Cardiff"
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
united_kingdom.append({"name": "Northern Ireland", "population": "1811000", "capital": "Belfast"})
# 3. Use a loop to print the names of all the countries in the UK.
for country_name in united_kingdom:
  print(f'{country_name["name"]}')
# 4. Use a loop to find the total population of the UK.
total_pop = 0
for pop in united_kingdom:
  current = pop["population"] #when the pop functiuon runs through and gets to population that turns the current variable into the the value thats in that key.
  total_pop += current

print(total_pop)

