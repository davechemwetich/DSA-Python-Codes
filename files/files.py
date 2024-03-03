# # oopen file method 
# # create a path variable and assign the path of the file to it
# # path = "C:\projects\pypro\cobra\files.py"
# file_input =open("C:\projects\pypro\cobra\propy\elsa.txt", "r")
# data = file_input.read()

# print(data)


# elsa_input =open("C:\projects\pypro\cobra\propy\elsa.txt", "r")
# data = elsa_input.read()
# print(data)

# elsa_input =open("C:\projects\pypro\cobra\propy\elsa.txt", "r")
# data = elsa_input.readlines(20)
# print(data)

elsa_input =open("C:\projects\pypro\cobra\propy\elsa.txt", "a")
data = elsa_input.write("True.")
print(data)


