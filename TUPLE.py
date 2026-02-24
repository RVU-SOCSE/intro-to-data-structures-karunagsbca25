#NAME-KARUNA.G.S
#USN-1RUA25BCA0047


# Tuple Operations Program

my_tuple = (2,4,7,9,10)

while True:
    print("\n--- Tuple Operations Menu ---")
    print("1. Add Element")
    print("2. Remove Element")
    print("3. Index")
    print("4. Count")
    print("5. Min")
    print("6. Max")
    print("7. Sum")
    print("8. Length")
    print("9. Sort")
    print("10. Reverse")
    print("11. Display Tuple")
    print("12. Clear Tuple")
    print("13. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        try:
            element = int(input("Enter number to add: "))
            my_tuple = my_tuple + (element,)
            print("Element added.")
        except ValueError:
            print("Invalid input.")

    elif choice == 2:
        try:
            element = int(input("Enter number to remove: "))
            if element in my_tuple:
                temp_list = list(my_tuple)
                temp_list.remove(element)
                my_tuple = tuple(temp_list)
                print("Element removed.")
            else:
                print("Element not found.")
        except ValueError:
            print("Invalid input.")

    elif choice == 3:
        try:
            element = int(input("Enter number to find index: "))
            if element in my_tuple:
                print("Index:", my_tuple.index(element))
            else:
                print("Element not found.")
        except ValueError:
            print("Invalid input.")

    elif choice == 4:
        try:
            element = int(input("Enter number to count: "))
            print("Count:", my_tuple.count(element))
        except ValueError:
            print("Invalid input.")

    elif choice == 5:
        if my_tuple:
            print("Minimum value:", min(my_tuple))
        else:
            print("Tuple is empty.")

    elif choice == 6:
        if my_tuple:
            print("Maximum value:", max(my_tuple))
        else:
            print("Tuple is empty.")

    elif choice == 7:
        if my_tuple:
            print("Sum:", sum(my_tuple))
        else:
            print("Tuple is empty.")

    elif choice == 8:
        print("Length:", len(my_tuple))

    elif choice == 9:
        if my_tuple:
            my_tuple = tuple(sorted(my_tuple))
            print("Tuple sorted.")
        else:
            print("Tuple is empty.")

    elif choice == 10:
        if my_tuple:
            my_tuple = my_tuple[::-1]
            print("Tuple reversed.")
        else:
            print("Tuple is empty.")

    elif choice == 11:
        print("Current Tuple:", my_tuple)

    elif choice == 12:
        my_tuple = ()
        print("Tuple cleared.")

    elif choice == 13:
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")

    print("Updated Tuple:", my_tuple)
