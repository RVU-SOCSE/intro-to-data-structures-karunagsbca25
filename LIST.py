#NMAE-KARUNA.G.S
#USN-1RUA25BCA0047


# List Operations Program with min, max, sum, count, len

my_list = [10,20,30,40,50]

while True:
    print("\n--- List Operations Menu ---")
    print("1. Append")
    print("2. Insert")
    print("3. Extend")
    print("4. Remove")
    print("5. Pop")
    print("6. Index")
    print("7. Count (specific element)")
    print("8. Sort")
    print("9. Reverse")
    print("10. Copy")
    print("11. Clear")
    print("12. Display List")
    print("13. Min")
    print("14. Max")
    print("15. Sum")
    print("16. Length")
    print("17. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        try:
            element = int(input("Enter number to append: "))
            my_list.append(element)
            print("Element appended.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == 2:
        try:
            element = int(input("Enter number to insert: "))
            pos = int(input("Enter position (0-based index): "))
            if 0 <= pos <= len(my_list):
                my_list.insert(pos, element)
                print("Element inserted.")
            else:
                print("Invalid position.")
        except ValueError:
            print("Invalid input.")

    elif choice == 3:
        try:
            new_list = list(map(int, input("Enter numbers separated by space: ").split()))
            my_list.extend(new_list)
            print("List extended.")
        except ValueError:
            print("Please enter valid numbers.")

    elif choice == 4:
        try:
            element = int(input("Enter number to remove: "))
            if element in my_list:
                my_list.remove(element)
                print("Element removed.")
            else:
                print("Element not found.")
        except ValueError:
            print("Invalid input.")

    elif choice == 5:
        if my_list:
            try:
                pos = int(input("Enter position to pop: "))
                if 0 <= pos < len(my_list):
                    removed = my_list.pop(pos)
                    print("Removed element:", removed)
                else:
                    print("Invalid position.")
            except ValueError:
                print("Invalid input.")
        else:
            print("List is empty.")

    elif choice == 6:
        try:
            element = int(input("Enter number to find index: "))
            if element in my_list:
                print("Index:", my_list.index(element))
            else:
                print("Element not found.")
        except ValueError:
            print("Invalid input.")

    elif choice == 7:
        try:
            element = int(input("Enter number to count: "))
            print("Count:", my_list.count(element))
        except ValueError:
            print("Invalid input.")

    elif choice == 8:
        my_list.sort()
        print("List sorted.")

    elif choice == 9:
        my_list.reverse()
        print("List reversed.")

    elif choice == 10:
        copied_list = my_list.copy()
        print("Copied list:", copied_list)

    elif choice == 11:
        my_list.clear()
        print("List cleared.")

    elif choice == 12:
        print("Current List:", my_list)

    elif choice == 13:
        if my_list:
            print("Minimum value:", min(my_list))
        else:
            print("List is empty.")

    elif choice == 14:
        if my_list:
            print("Maximum value:", max(my_list))
        else:
            print("List is empty.")

    elif choice == 15:
        if my_list:
            print("Sum of elements:", sum(my_list))
        else:
            print("List is empty.")

    elif choice == 16:
        print("Length of list:", len(my_list))

    elif choice == 17:
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")

    print("Updated List:", my_list)
