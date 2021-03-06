import datetime

#import csv module for reading 
#the csv files.
import csv

PRODUCT_KEY_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
REQUESTED_QUANTITY_INDEX = 1


def main():
    
    try:
        filename = "products.csv"
        
        #call the read_dict fucntion and save its reuturned value as producs_dict.
        products_dict = read_dict(filename, PRODUCT_KEY_INDEX)
        print()

        filename = "request.csv"
        
        #print name of store.
        print("Inkom Emporium Stores")
        print()
        
        #open and read the reciept.csv file
        with open(filename, "rt") as request_file:
            subtotal = 0
            total_products = 0
            request_file = csv.reader(request_file)
            next(request_file)

            #read rows of request.
            for line in request_file:
                product_num = line[PRODUCT_KEY_INDEX]

                #use the product number of each row in the request.csv
                #to find the corresponding items in the products dictionary.
                product_num_value = products_dict[product_num]
                product_name = product_num_value[PRODUCT_NAME_INDEX]
                product_price = float(product_num_value[PRODUCT_PRICE_INDEX])
                quantity = int(line[REQUESTED_QUANTITY_INDEX])
                total_products += quantity
                subtotal += (product_price * quantity)

                print(f"{product_name}: {quantity} @ {product_price}")
                
            sales_tax = compute_sales_tax(subtotal, 6)
            total_amount = compute_total(subtotal, sales_tax)
            current_date_and_time = datetime.datetime.now()
            date = datetime.date.today()
            
            print()
            print(f"Number of items: {total_products}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales tax: {sales_tax:.2f}")
            print(f"Total: ${total_amount:.2f}")
            print()
            print("Thanks for your patronage!!!")
            print(f"{current_date_and_time:%A %I:%M %p} {date}")
            print()
 
    #handle file not found error for products.csv or request.csv file    
    except FileNotFoundError as not_found_error:
        print("Error: missing file")
        print(not_found_error)
    
    #Handle permission error for products.csv or request.csv files.
    except PermissionError as no_permission:
        print(f"Error: You do not have permission to access \
            {filename}")
        print("Contact your admin or choose another file.")

    #Handle invalid dictionary key error for the products dictionary.
    except KeyError as key_error:
        print(f"Error: Unknown product in the {filename}") 
        print(product_num)

    #Handle wrong invalid quantity for the request.csv file.
    except ValueError as val_error:
        print(f"Error: invalid quantity of {product_name} entered: {line[REQUESTED_QUANTITY_INDEX]}")
        
     

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

        #skip the headings row                                                                                                                                                                                                                                                                 of the file.
        next(reader)

        #loop through each row of the csv file
        for row in reader:
            #save products index as variable key.
            key = row[key_column_index]

            #add products in the products dictionary
            #using the product number as the keys.
            products_dict[key] = row
    #return the products dictionary.
    return products_dict

def compute_sales_tax(subtotal, rate):
    """Compute the sales tax of the total items ordered at a given rate. 
    Parameters:
        subtotal: Total cost of items ordered without tax.
        rate: Percentage tax rate.
    Return: sales_tax
    """
    sales_tax = (subtotal * rate) / 100
    return sales_tax

def compute_total(subtotal, sales_tax):
    """Compute the cost of ordered items and sales tax.
    Parameters: 
        subtotal: Total cost of items ordered without tax.
        sales_tax: Amount of tax to be paid based on items ordered.
    Return: total
    """
    total = subtotal + sales_tax
    return total

if __name__ == "__main__":
    main()