import csv

def main():
    readfile("cse111\provinces.txt")

def readfile(filename):
    """Read a file and modify it.
    parameters: 
    filename: name of file to be read.

    return: nothing
    """
    albertas = 0
    provinces_list = []
    #Open the provinces.txt file for reading.
    with open(filename, "rt") as provinces:
    
        #Read the contents of the file into a list where each line 
        # of text in the file is stored in a separate element in the list. 
        for province in provinces:

            #remove spaces.
            clean = province.strip()
            provinces_list.append(clean)
        
        #Print the entire list.
        print(provinces_list)

        #Remove the first element from the list.
        provinces_list.remove(provinces_list[0])
        #Remove the last element from the list.
        provinces_list.pop()
        print()
        print(provinces_list)

        #Replace all occurrences of "AB" in the list with "Alberta".
        for province in provinces_list:
            if province == "AB":
                ab_index = provinces_list.index(province)
                provinces_list[ab_index] = "Alberta"
            #Count the number of elements that are "Alberta".
            if province == "Alberta" or province == "AB":
                albertas += 1
            
        print()
        print(provinces_list)

        print(albertas)


if __name__ == "__main__":
    main()