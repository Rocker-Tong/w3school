# Delete blanks at the beginning and the end
a = " Hello, World! "
print(a.strip())
# returns "Hello, World!"

# String format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# Use index numbers for correct placeholders
quantity = 4
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


# False boolean values
class MyClass:
    def __len__(self):
        return False


myobj = MyClass()
print(bool(myobj))
