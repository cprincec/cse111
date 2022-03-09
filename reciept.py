#import csv module for reading 
#the csv files.
import csv

PRODUCT_KEY_INDEX = 0

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    #create an empty dictionary for products.
    products_dict = {}

    #open the products.csv file and 
    # save its contents as products_file.
    with open(filename, "rt") as products_file:
        #call the csv reader function 
        # to read the products file.
        #save it as reader.
        reader = csv.reader(products_file)

        #skip the headings row of the file.
        next(reader)

        #Remove leading and trailing spaces from 
        #each row in the file.
        clean_file = reader.strip()

        #loop through each row of the csv file
        for row in clean_file:
            
            #save products index as variable key.
            key = row[PRODUCT_KEY_INDEX]

            #add products in the products dictionary
            #using the product number as the keys.
            products_dict[key] = row

    #return the products dictionary.
    return products_dict

print(read_dict("products.csv", PRODUCT_KEY_INDEX))
