employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}
]
print(type(employees))
for k in range (len(employees)):
      print("name", ':' , employees[k]["name"])
      print("job", ':', employees[k]["job"])
      print("city", ':', employees[k]["address"]["city"])
print(employees[1]["address"]["country"])
