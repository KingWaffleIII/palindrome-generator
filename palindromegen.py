from time import sleep

def reverseme(num):
    return int(str(num)[::-1])


def palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


def main():

    global answer
    print("Panindrome Generator by KingWaffleIII.")
    sleep(1)
    print('''Palindrome Definition:
noun (palɪndrəʊm)
a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.''')
    number = input("Please input a number: ")
    tries = 0

    if number.isdigit():

        # number1 = list(str(number))
        # number1 = list(map(int, number1))
        number2 = reverseme(number)
        # origin = [int(number), int(number2)]
        # print(f"Got number: {origin.index(0)} and reversed: {origin.index(1)}")
        sleep(1)

        while number > str(0):

            if tries <= 0:

                answer = int(number) + int(number2)
                print(f"Added numbers and got {answer}")
                sleep(1)
                palindrome(answer)

                tries += 1

                if palindrome(answer):

                    print(f"Number {number} becomes a palindrome after {tries} tries.")
                    sleep(10)
                    break

            else:

                number1 = answer
                number2 = reverseme(answer)
                answer = int(number1) + int(number2)
                print(f"Added numbers and got {answer}")
                sleep(1)
                palindrome(answer)
                tries += 1

                if palindrome(answer):

                    print(f"Number {number} becomes a palindrome after {tries} tries.")
                    sleep(10)
                    break

    else:

        print("That's not a number! Resetting...")
        sleep(1)
        main()


main()
