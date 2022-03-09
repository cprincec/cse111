#import csv module for reading 
#the csv files.
import csv

PRODUCT_KEY_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

REQUESTED_QUANTITY_INDEX = 1

def main():
    #call the read_dict fucntion and save its reuturned value as producs_dict.
    products_dict = read_dict(r"C:\Users\USER\Desktop\byu\Winter 2022\CSE111\cse111\products.csv", PRODUCT_KEY_INDEX)

    print()
    print("All Products")
    print(products_dict)

    #open and read the reciept.csv file
    with open(r"C:\Users\USER\Desktop\byu\Winter 2022\CSE111\cse111\request.csv", "rt") as request_file:
        
        request_file = csv.reader(request_file)
        next(request_file)
        print()
        print("Requested Items")

        #read rows of request.
        for line in request_file:
            product_num = line[PRODUCT_KEY_INDEX]

            #use the product number of each row in the request.csv
            #to find the corresponding items in the products dictionary.
            if product_num in products_dict:
                product_num_value = products_dict[product_num]
                product_name = product_num_value[PRODUCT_NAME_INDEX]
                product_price = product_num_value[PRODUCT_PRICE_INDEX]
                quantity = line[REQUESTED_QUANTITY_INDEX]

                print(f"{product_name}: {quantity} @ {product_price}")
            else:
                print(f"{product_name.capitalize()} is out of stock.")
        print()


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

        #loop through each row of the csv file
        for row in reader:
            
            #save products index as variable key.
            key = row[PRODUCT_KEY_INDEX]

            #add products in the products dictionary
            #using the product number as the keys.
            products_dict[key] = row

    #return the products dictionary.
    return products_dict

if __name__ == "__main__":
    main()