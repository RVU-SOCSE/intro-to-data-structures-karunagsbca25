#NAME-KARUNA.G.S
#USN-1RUA25BCA0047




# Complete 22-Command Set Operations Program

my_set ={12,23,34,56,78}

while True:
    print("\n--- Set Operations Menu ---")
    print("1. Add Element")
    print("2. Update Set")
    print("3. Remove Element")
    print("4. Discard Element")
    print("5. Pop Element")
    print("6. Check Membership")
    print("7. Count Element")
    print("8. Min")
    print("9. Max")
    print("10. Sum")
    print("11. Length")
    print("12. Union")
    print("13. Intersection")
    print("14. Difference")
    print("15. Symmetric Difference")
    print("16. isSubset")
    print("17. isSuperset")
    print("18. isDisjoint")
    print("19. Intersection Update")
    print("20. Difference Update")
    print("21. Symmetric Difference Update")
    print("22. Clear Set")
    print("23. Display Set")
    print("24. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid number.")
        continue

    if choice == 1:
        my_set.add(int(input("Enter number: ")))

    elif choice == 2:
        my_set.update(set(map(int, input("Enter numbers: ").split())))

    elif choice == 3:
        try:
            my_set.remove(int(input("Enter number: ")))
        except KeyError:
            print("Element not found.")

    elif choice == 4:
        my_set.discard(int(input("Enter number: ")))

    elif choice == 5:
        if my_set:
            print("Removed:", my_set.pop())
        else:
            print("Set is empty.")

    elif choice == 6:
        num = int(input("Enter number: "))
        print("Exists" if num in my_set else "Not found")

    elif choice == 7:
        num = int(input("Enter number: "))
        print("Count:", 1 if num in my_set else 0)

    elif choice == 8:
        print("Min:", min(my_set) if my_set else "Set empty")

    elif choice == 9:
        print("Max:", max(my_set) if my_set else "Set empty")

    elif choice == 10:
        print("Sum:", sum(my_set) if my_set else "Set empty")

    elif choice == 11:
        print("Length:", len(my_set))

    elif choice == 12:
        other = set(map(int, input("Enter another set: ").split()))
        print("Union:", my_set.union(other))

    elif choice == 13:
        other = set(map(int, input("Enter another set: ").split()))
        print("Intersection:", my_set.intersection(other))

    elif choice == 14:
        other = set(map(int, input("Enter another set: ").split()))
        print("Difference:", my_set.difference(other))

    elif choice == 15:
        other = set(map(int, input("Enter another set: ").split()))
        print("Symmetric Difference:", my_set.symmetric_difference(other))

    elif choice == 16:
        other = set(map(int, input("Enter another set: ").split()))
        print("Is Subset:", my_set.issubset(other))

    elif choice == 17:
        other = set(map(int, input("Enter another set: ").split()))
        print("Is Superset:", my_set.issuperset(other))

    elif choice == 18:
        other = set(map(int, input("Enter another set: ").split()))
        print("Is Disjoint:", my_set.isdisjoint(other))

    elif choice == 19:
        other = set(map(int, input("Enter another set: ").split()))
        my_set.intersection_update(other)

    elif choice == 20:
        other = set(map(int, input("Enter another set: ").split()))
        my_set.difference_update(other)

    elif choice == 21:
        other = set(map(int, input("Enter another set: ").split()))
        my_set.symmetric_difference_update(other)

    elif choice == 22:
        my_set.clear()
        print("Set cleared.")

    elif choice == 23:
        print("Current Set:", my_set)

    elif choice == 24:
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")

    print("Updated Set:", my_set)
