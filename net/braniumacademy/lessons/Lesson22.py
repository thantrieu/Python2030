print("Where is the capital of Vietnam?")
print("1. Ha Noi")
print("2. Da Nang")
print("3. Hai Phong")
print("4. Ho Chi Minh")
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        print("Wonderful! Your answer is correct!")
    case 2 | 3 | 4:
        print("Ehh. Your answer is wrong!")
    case _:
        print("Huh? Wrong option. Please try again!")
