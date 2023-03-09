# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



menu = True

#Thomas adding decode function
def decode(password):
    decoded_password = ""
    for char in password:
        num = int(char)
        num -= 3
        if num < 0:
            num += 10
        decoded_password += str(num)
    return decoded_password



def main():




    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    while menu:
        if option == 1:
            option = int(input("please enter an option: "))
            password = int(input("Please enter your password to encode: "))
            new_password = int(input('Your password has been encodded and stored!'))
        elif option == 2:
            pass
        elif option ==3:
            pass




if __name__ == '__main__"':
    main()