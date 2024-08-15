from functions import *

def main():
    create_tables()

    while True:
        print("Choose an option:")
        print("1.Add product")
        print("2.Add customer")
        print("3.Add order")
        print("4.Total sales volume")
        print("5.Number of orders per customer")
        print("6.Average order check")
        print("7.The most popular category of goods")
        print("8.The total number of products in each category")
        print("9.Product price updates in the 'phones' category")
        print("10.Exit")

        choice = input("Enter choice:")

        if choice == '1':
            name = input("Enter product name:")
            category = input("Enter product's category:")
            price = float(input("Enter product's price:"))
            add_product(name, category, price)
            print("Product added.")
        elif choice == '2':
            first_name = input("Enter first name:")
            last_name = input("Enter last name:")
            email = input("Enter email:")
            add_customer(first_name, last_name, email)
            print("Customer added.")
        elif choice == '3':
            customer_id = int(input("Enter customer's id:"))
            product_id = int(input("Enter product's id:"))
            quantity = int(input("Enter quantity:"))
            order_date = input("Enter order date (ex.: 2011-10-05):")
            add_order(customer_id, product_id, quantity, order_date)
            print("Order added.")
        elif choice == '4':
            total_sales_volume()
        elif choice == '5':
            orders_per_customer()
        elif choice == '6':
            break
        elif choice == '7':
            break
        elif choice == '8':
            break
        elif choice == '9':
            break
        elif choice == '10':
            break
        else:
            print("Invalid choice.")

main()