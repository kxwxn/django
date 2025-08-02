def name_of_function():
      "Docstring explains what the function does"
      print("hello")

name_of_function()

def name_of_function(name):
      print("hello " + name)

name_of_function("KW")

def name_of_function(name, age):
      print(f"hello {name} you are {age} years old")

name_of_function("KW", 20)

# return 
def add_numbers(num1,num2):
      return num1 + num2

result = add_numbers(3,4)
print(result)

def checker(num):
      if num > 100:
            return "greater than 100"
      else:
            return "less than 100"
      
print(checker(111))
print(checker(42))

def checker2(list,num):
      for item in list:
            if item == num:
                  return True
            
      return False

print(checker2([1,2,3,4,5],3))
print(checker2([1,2,3,4,5],6))



