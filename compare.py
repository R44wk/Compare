"""By r4wk
script that compare between two files content"""

from io import open


def clean ():
    print ("\n\tCompare between two files\n")
    path_file1= input(r"Path of original file: ")
    path_file2= input(r"Path of file to compare: ")
    fileout= input(r"Name of out file: ")
    
    open_file1 = open(path_file1, "r")
    line1= set(open_file1.readlines())
    open_file1.close()
    
    open_file2 = open(path_file2,"r")
    line2= set(open_file2.readlines())
    open_file2.close()

    difference=set(line1).difference(line2)

    
    print ("\nThere {0} data missing in the \"{1}\" file. ".format(len(difference),path_file2))
    
    new_file = open(fileout, "w")
    for l in difference:
        new_file.write(l)
    new_file.close()
    
    print ("Done!\nThe data save in \'{}\' file.".format(fileout))
    
    
clean()
