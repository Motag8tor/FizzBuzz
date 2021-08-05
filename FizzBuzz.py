def begin():
    fizz, buzz = 3, 5
    for i in range(1, 101):
        value = ""
        if i % fizz == 0: value += "Fizz"
        if i % buzz == 0: value += "Buzz"
        if value == "": value = i
        print(value)

if __name__ == "__main__":
    begin()
