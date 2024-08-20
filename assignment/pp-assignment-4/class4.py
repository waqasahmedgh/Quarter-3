name: str = input("What is your name? ")
print(f"Hello, {name}!")

f_no1: int = int(input("Enter your first favorite number: "))
f_no2: int = int(input("Enter your second favorite number: "))
f_no3: int = int(input("Enter your third favorite number: "))

def is_even(num: int) -> bool:
    return num % 2 == 0
def is_odd(num: int) -> bool:
    return num % 2 != 0
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    if (is_even(f_no1))==True:
        print(f"The number {f_no1} is even.")
    else:
        print(f"The number {f_no1} is odd.")

    if (is_even(f_no2))==True:
        print(f"The number {f_no2} is even.")
    else:
        print(f"The number {f_no2} is odd.")
    
    if (is_even(f_no3))==True:
        print(f"The number {f_no3} is even.")
    else:
        print(f"The number {f_no3} is odd.")

    print(f"The number {f_no1} and its square: {(f_no1, f_no1**2)}")
    print(f"The number {f_no2} and its square: {(f_no2, f_no2**2)}")
    print(f"The number {f_no3} and its square: {(f_no3, f_no3**2)}")

    sum_fav_nums = f_no1 + f_no2 + f_no3

    print(f"The sum of your favorite numbers is: {sum_fav_nums}")
    
    if (is_prime(sum_fav_nums))==True:
       print(f"Wow, {sum_fav_nums} is a prime number!")
    else:
       print(f"Sorry, {sum_fav_nums} is not a prime number.")

