# Q.1 Flat List Code

def flatten_and_multiply(nested_list):
    def flatten(lst):
        flattened_list = []
        for element in lst:
            if type(element) in [list, tuple, set]:
                flattened_list.extend(flatten(element))
            elif type(element) == dict:
                for key, value in element.items():
                    flattened_list.extend(flatten([key, value]))
            else:
                flattened_list.append(element)
        return flattened_list

    def is_number(num):
        return isinstance(num, (int, float))

    flattened_list = flatten(nested_list)
    product = 1
    for num in flattened_list:
        if is_number(num):
            product *= num
    return product

list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)}, [56, 'data science'], 'Machine Learning']
result = flatten_and_multiply(list1)
print(result)


# Q.2 Encryption code 
def encrypt_message(message):
  encrypted_message = ""
  for char in message:
    if char.isalpha():
      encrypted_message += chr(122 - ord(char.lower()) + 97)
    elif char == " ":
      encrypted_message += "$"
    else:
      encrypted_message += char
  return encrypted_message

message = "I want to become a Data Scientist."
encrypted_message = encrypt_message(message)
print("Encrypted Message:", encrypted_message)
