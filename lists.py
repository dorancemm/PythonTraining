def main():
    shopping_list = []

    while True:
        print("\n --- List of Shopping ---")
        print("1. Add Article")
        print("2. Remove Article")
        print("3. Show List of Shopping")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            item = input("Enter the name of an item to add to the shopping list: ")
            shopping_list.append(item)
        elif option == "2":
            item = input("Enter the name of an item to remove to the shopping list: ")
            if item in shopping_list:
                shopping_list.remove(item)
        elif option == "3":
            print("\nShopping List")
            for item in shopping_list:
                print("- ", item)
        elif option == "4":
            break
        else:
            print ("Invalid option")

if __name__ == "__main__":
    main()