my_list = [1, 2, 3, 4, 5]

for item in my_list:
      print(f"{item}hello")


employees = {"ceo":"cindy", "cfo":"james", "cto":"chris"}

for position in employees:
      print(employees[position], "first case")
      print(f"the {position} is held by {employees[position]}")

for key, value in employees.items():
      print(f"{key} : {value}", "second case")

for position in employees.keys():
      print(f"the {key} is {value} ")

for name in employees.values():
      print(f"the name is {name}")



for i in range(1, 6): 
      print(i)

for i in range(1, 10, 2):
      print(i)

for i in range(10, 0, -1):
      print(i)

for i in range(10, 0, -2):
      print(i)
