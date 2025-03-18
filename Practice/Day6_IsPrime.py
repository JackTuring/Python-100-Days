num = int(input("Please enter a number: "))
end = int(num ** 0.5)
prime_flag = True

for i in range(2, end + 1):
    if num % i == 0:
        prime_flag = False
        break

if prime_flag:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
