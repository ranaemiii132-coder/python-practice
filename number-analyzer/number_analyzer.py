total = 0
count = 0
positive = 0
negative = 0
numbers = []

while True:
    try:
        number = int(input("Enter a number, 0 to stop: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if number == 0:
        break

    numbers.append(number)

    total = total + number
    count = count + 1

    if number > 0:
        positive = positive + 1
    else:
        negative = negative + 1


if count > 0:
    average = total / count

    print("\n----- Result -----")
    print("Total:", total)
    print("Count:", count)
    print("Positive numbers:", positive)
    print("Negative numbers:", negative)
    print("Highest number:", max(numbers))
    print("Lowest number:", min(numbers))
    print("Average:", round(average, 2))
else:
    print("No valid numbers were entered.")
