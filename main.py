names = ["mohammed", "jaber", "tarq", "ahemed"]

while True:

    choice = input("Choose an option: ")

    if choice == "0":
        break

    if choice == "1":
        print(names)

        for name in names:
            print(name)

    elif choice == "2":
        new_name = input("Enter a new name: ")
        names.append(new_name)
        print(names)

    elif choice == "3":
        name = input("Enter the name to remove: ")
        names.remove(name)
        print(names)

    elif choice == "4":
        index = int(input("Enter the index to remove: "))
        names.pop(index)
        print(names)

    elif choice == "5":
        name = input("Enter the name to search: ")

        if name in names:
            print("Name is in the list")
        else:
            print("Name is not in the list")

    elif choice == "6":
        print(len(names))

    elif choice == "7":
        name = input("Enter the name to count: ")
        print(names.count(name))

    elif choice == "8":
        name = input("Enter the name: ")
        print(names.index(name))

    elif choice == "9":
        names.sort()
        print(names)

    elif choice == "10":
        names.reverse()
        print(names)
        # My first Git update