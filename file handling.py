import os
print("Lets start the file handling program")
print("\n1.Create the file \n2.Read the file \n3.List the file \n4.Edit the file \n5.Delete the file \n6.Stop the program")
while True:
    a=int(input("Enter the choice:"))
    def f():
        print("1.Create the file")
        print("2.Read the file")
        print("3.List the file")
        print("4.Edit the file")
        print("5.Delete the file")
        print("6.Stop the program")
    match a:
        case 1:
            print("\n1.Creating a file")
            name=input("Enter the file name:")
            name=name+".txt"
            file=open(name,"w")
            file.write("Hello")
            print("File created successfully")
            print("_______________________________________________________")
            f()
        case 2:
            print("\n2.Reading a file")
            name=input("Enter the file name:")
            name=name+".txt"
            file=open(name,"r")
            print(file.read())
            print("_______________________________________________________")
            f()
        case 3:
            print("\n3.Listing a file")
            print("_______________________________________________________")
            path="D:/Nandini 1st BCA/python.nandini"
            files=os.listdir(path)
            for file in files:
                print(file)
            print("_______________________________________________________")
            f()
        case 4:
             print("\n4.Editing a file")
             name=input("Enter the file name:")
             name=name+".txt"
             file=open(name,"a")
             print(file.write("Nandini"))
             print("__________________________________")
             f()
        case 5:
            print("\n5.Deleting a file")
            name=input("Enter the file name:")
            name=name+".txt"
            os.remove(name)
            print("file",name,"Deleted successfully")
            print("_______________________________________________________")
            f()
        case 6:
            print("\n6.Program End")
            print("*******************************************************")
            break
        case _:
            print("Invalid choice")
print("File handling program ends")
            
