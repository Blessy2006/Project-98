def swapFileData():

    path1 = input("Enter the file1 path:- ")
    path2 = input("Enter the file2 path:- ")

    with open(path1, 'r') as a:
        data_a = a.read()

    with open(path2, 'r') as b:
        data_b = b.read()    

    with open(path1, 'w') as a:
        a.write(data_b)    

    with open(path2, 'w') as b:
        b.write(data_a)            

swapFileData()        