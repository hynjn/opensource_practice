# get two numeric parameters
# return sum
def plus(x, y):
    return x + y

# get two numeric parameters
# return difference
def minus(x, y):
    return x - y

# get two numeric parameters
# return product
def multiply(x, y):
    return x * y

# get two numeric parameters
# return quotient
def divide(x, y):
    return x / y if y != 0 else float('inf') #양의 무한대임을 명시하여 알려줌

# main function
def main():
    check = 1
    print("Welcome to calculator")
    while check >= 1:
        print("0: exit, 1: plus, 2: minus, 3: multiply, 4: divide")
        try:
            check = int(input())
        except ValueError:
            print("숫자를 입력하세요.")
            continue
        if check == 1:
            try:
                print("First Number:")
                x = float(input())
                print("Second Number:")
                y = float(input())
                print("Answer:", plus(x, y))
            except ValueError:
                print("숫자를 입력하세요.")
        elif check == 2:
            try:
                print("First Number:")
                x = float(input())
                print("Second Number:")
                y = float(input())
                print("Answer:", minus(x, y))
            except ValueError:
                print("숫자를 입력하세요.")
        elif check == 3:
            try:
                print("First Number:")
                x = float(input())
                print("Second Number:")
                y = float(input())
                print("Answer:", multiply(x, y))
            except ValueError:
                print("숫자를 입력하세요.")
        elif check == 4:
            try:
                print("First Number:")
                x = float(input())
                print("Second Number:")
                y = float(input())
                print("Answer:", divide(x, y))
            except ValueError:
                print("숫자를 입력하세요.")
        elif check > 4:
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()

