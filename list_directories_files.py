import os

def list_dir_files():
    new_dir_list=[]
    new_file_list=[]

    absolute_path = os.path.abspath("/")
    list_file = os.listdir(absolute_path)
    for file_name in list_file:
        full_path = os.path.join(absolute_path,file_name)
        if os.path.isdir(full_path):
            new_dir_list.append(full_path)
        else:
            new_file_list.append(full_path)
    return new_dir_list, new_file_list

def output_dir(dir):
    return "{:>28} | {:<20}".format(dir, "Directory")

def output_file(file):
    return "{:>28} | {:<20}".format(file, "File")




def main():
    dir_list, file_list = list_dir_files()
    for dir in dir_list:
        print(output_dir(dir))
    for file in file_list:
        print(output_file(file))


main()