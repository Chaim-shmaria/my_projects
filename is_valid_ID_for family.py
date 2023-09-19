def is_valid_id_numer(id):
    # Check if the input consists of digits and has a length of 9
    if id.isdigit() and len(id) == 9:
        # Convert the ID string into a list of integers
        id = [int(num) for num in id]

        # Calculate the sum of odd-indexed digits
        sum_of_odds = sum(id[0:8:2])

        # Create a list of even-indexed digits
        list_of_evens = id[1:8:2]

        # Calculate the sum of even-indexed digits with special handling for digits greater than 4
        sum_of_evens = sum(((item * 2 - 9) if (item > 4) else item * 2) for item in list_of_evens)  # !!!

        # Calculate the sum of all digits
        sum_of_all = sum_of_odds + sum_of_evens

        # Check if the last digit of the sum (checksum) is equal to the last digit of the input ID
        if 10 - (sum_of_all % 10) == id[8]:
            print("The ID number you entered is a valid ID number")
        else:
            print("The ID number you entered is not a valid ID number")

    else:
        # If the input does not consist of 9 digits, return False
        print("You did not enter a 9-digit ID number")


def main():
    # Input an ID number from the user
    id = input("Hello,\nI can check if ID number is correct or not.\nPlease enter ID number:")

    # Call the is_valid_id_numer function to check its validity and print the result
    is_valid_id_numer(id)


if __name__ == "__main__":
    main()
