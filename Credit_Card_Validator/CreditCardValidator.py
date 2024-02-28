sumOddDigits = 0
sumEvenDigits = 0
total = 0

# Step 1: Remove any "-" or " "
cardNumber = input("Enter card number: ")
cardNumber = cardNumber.replace("-" , "")
cardNumber = cardNumber.replace(" " , "")

#Step 2: add all digits in the odd places from right to left
cardNumber = cardNumber[::-1]
for x in cardNumber[::2]:
    sumOddDigits += int(x)

#Step 3: double every second digits from right to left
for x in cardNumber[1::2]:
    x = int(x) * 2
    if x >= 10:
        sumEvenDigits += (1 + (x % 10))
    else:
        sumEvenDigits += x

#Step 4: sum totals of step 2 and step 3
total = sumOddDigits + sumEvenDigits

#Step 5: if sum  is divisible by 10 , the credit card is valid
if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")

