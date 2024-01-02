def main():

    temp = input("what is your temperature")
    corf = input("Convort from celsius or fahrenheit(c or f)")
    temp = int(temp)

    if corf == 'c':
        fan = temp * (9/5) + 32
        print(fan)
    elif corf == 'f':
        can = (temp - 32) * (5/9)
        print(can)
    else:
        print("Error did you type c or f, or did you not type a number?")

    if __name__ == '__main__':
        main()

main()