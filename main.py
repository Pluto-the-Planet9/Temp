
def main():

    temp = input("what is your temperature")
    corf = input("Convert from celsius or fahrenheit(c or f)")
    temp = int(temp)

    if corf == 'c':
        fan = temp * (9/5) + 32
        print(fan)
        fan = str(fan)
    elif corf == 'f':
        can = (temp - 32) * (5/9)
        print(can)
        can = str(can)
    else:
        print("Error did you type c or f?")

    if corf == 'c':
        file = open('temps_recorded.txt', 'a')
        file.write(fan)
        file.close()

    if corf == 'f':
        file = open('temps_recorded.txt', 'a')
        file.write(can)
        file.close()

    if __name__ == '__main__':
        main()

main()