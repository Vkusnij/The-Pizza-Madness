# String repeat

def string_repeat(number, text):
    return text * number

print(string_repeat(2, "HawaiiPizza"))  

# 2. No whitespaces
def no_space(text):
    return text.replace(" ", "")

print(no_space("Hawaii Pizza"))  

# 3. Number to string
def number_to_string(number):
    return str(number)

value = 2 
print(value, type(value))
converted_value = number_to_string(value)
print(converted_value, type(converted_value))  

# 4. Boolean to string
def boolean_to_string(bool_val):
    return str(bool_val)

value_bool = True
print(type(value_bool))
value_converted = boolean_to_string(value_bool)
print(value_converted, type(value_converted))  

# 5. Abbreviate a Pizza name
def abbrev_name(full_name):
    if not full_name or not all(word.isalpha() for word in full_name.split()):
        return "Invalid input!!!"
    initials = [word[0].upper() for word in full_name.split() if word]
    return ".".join(initials)

print(abbrev_name("Hawaii Pizza"))  

# 6. Pizza length
def name_length(pizza_names):
    if not isinstance(pizza_names, str):
        return "Invalid input!!!"
    return [f"{name} {len(name)}" for name in pizza_names.split() if name]

print(name_length("Pepperoni Margarita Hawaii Wiesjska"))  

# 7. Remove the first and last element
def remove_orders(order_string, separator=","):
    if not order_string:
        return "Error: Input cannot be empty!"
    orders = order_string.split(separator)
    if len(orders) <= 2:
        return "Error: Not enough orders to remove ;("
    modified_orders = orders[1:-1]
    return separator.join(modified_orders)

print(remove_orders("hawaii,Wiejska,Pepperoni,Margarita"))  

# 8. The menu
def food_menu(food_items):
    if not isinstance(food_items, list) or not food_items:
        return "Error: Input must be a non-empty list of food items!!!"
    return [f"{i + 1}. {item}" for i, item in enumerate(food_items) if item]

print(food_menu(["Hawaii Pizza", "Diablo Pizza"]))