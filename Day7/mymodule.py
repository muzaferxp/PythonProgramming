#1 variables
#2 functions
#3 classes


Name = "Sam"

def write_data(data,file_path):
    #write data to file in appending mode
    f = open(file_path, "a")
    for line in data:
        f.write(line + "\n") 
    f.close()
