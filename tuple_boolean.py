# TUPLE IS IMMUTABLE

mylist = [1,2,3]
mytuple = (1,2,3)

print(mytuple)

mylist.append("NEW")
# mytuple[0] = "NEW"
print(mylist)
print(mytuple)

print("--------------------------------")

# BOOLEAN

print(1 > 2)
print(1 < 2)
is_logged_in = True
is_logged_out = False

print(is_logged_in)
print(is_logged_out)

print(type(is_logged_in))
print(type(is_logged_out))