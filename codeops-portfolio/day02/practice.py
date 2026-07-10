# Exercise 1: Temperature label

temperature = float(input("Enter temperature in Celsius: "))


if temperature < 15:
    print("cold")

elif temperature <= 28:
    print("warm")

else:
    print("hot")



# Exercise 2: Receipt loop

for number in range(1, 11):
    print(f"Receipt #{number}")



# Exercise 3: Even numbers

for number in range(1, 21):

    if number % 2 == 0:
        print(number)



# Exercise 4: Discount function

def apply_discount(price, percent=10):

    discount = price * percent / 100

    return price - discount



print(apply_discount(100))

print(apply_discount(100, 20))



# Exercise 5: Countdown

count = 5


while count >= 1:

    print(count)

    count -= 1


print("Liftoff!")