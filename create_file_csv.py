import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_Dict ={}

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    f = csv.DictReader(file)
    # Process each item of the dictionary
    i = 1
    for row in f:
        #return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
        # return_string.update(row)
        return_Dict[f"flower_{i}"] = dict(row)
        i+=1
    return return_Dict

#Call the function
for key, value in contents_of_file("flower.csv").items():
    print(f"{key} : {value}")
# print(contents_of_file("flowers.csv"), end="\n")
