def swappingFileData():
    file1=input("Enter The First File Name To Swap ")
    file2=input("Enter The Second File Name To Swap ")
    with open(file1,'r')as a:
        data_a=a.read()
    with open(file2,'r')as b:
        data_b=b.read()
    with open(file1,'w')as a:
        a.write(data_b)
    with open(file2,'w')as b:
        b.write(data_a)
swappingFileData()