import re
def line_fetch(list_of_line_file):
    mobile=[]
    for line in list_of_line_file:
        m1=re.findall('[6-9]{1}[0-9]{9}',line)
        if len(m1)==0:
            continue
        else:
            mobile.append(m1[0])
    return mobile
def line_read(file_path):
    fp=open(file_path)
    data=fp.readlines()
    return data
def main():
    print("Entering the main function")
    file_path='text file'
    print("list of line read in file")
    list_of_line_file=line_read(file_path)
    print("mobile no fetch")
    mobile=line_fetch(list_of_line_file)
    print("mobile")
    return mobile








