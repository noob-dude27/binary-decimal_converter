# Program intended to convert binary to decimal numbers
# Program was intended to assist in answering some CSS questions inwhich contained binary-to-decimal conversions.

def verify_binary(binary:int) -> bool:
    """Verifies that the given binary digits are actually convertible to decimal."""
    # First check: Checks if all are digits by converting the binary into int
    try:
        int(binary)
    except ValueError:
        print("Please enter 1s and 0s only! No letters!")
        return False

    # Second check: Checks the actual content if it is fully composed of 1s and 0s
    digit_list = ["1", "0"]
    for digit in binary:
        if digit not in digit_list:
            print("Please enter 1s and 0s only! No letters!")
            return False
    return True        
    
def init_num_list(interval:int) -> list:
    """Creates "num_list", the numbers inside the list will be used to align with each binary digit."""
    num_list = []

    num = 1 # CONSTANT
    starting_num = num # the original number is added before increment since it is part of the alignment. 
    num_list.append(starting_num)

    # Subtracts old interval by 1 then appends the original number to the first index for a correct "num_list".
    new_interval = interval-1
    i = 1
    while i <= new_interval:
        # summation occurs until "i" exceeds "new_interval"
        # resulting summation values are appended to the "num_list".
        i += 1
        num += num
        num_list.append(num)
    return num_list

def align_to_decimal(binary:str, num_list:list) -> list:
    """Matches the binary digits with their correspoding values."""
    alignment = []

    for value, digit in zip(num_list, reversed(binary)):
        tmp = [value, digit]
        alignment.append(tmp)
    return alignment

def filter_digit_alignment(alignment):
    """Removes the unnecessary alignments then creates the final version of "alignment" list only containing decimals."""
    # Removes the digit and its corresponding decimal if the digit is 0.
    for row in alignment[:]:
        if row[1] == "0":
            alignment.remove(row)
    print(f"After removing zeroes: {alignment}")

    # After removing the alignments with 0s it removes the 1s.
    for row in alignment[:]:
        row.remove('1')

    # Finally, extract the remaining values from "alignment" and insert to "final_alignment" to add all numbers.
    final_alignment = []
    for row in alignment:
        for items in row:
            values = items
            final_alignment.append(values)
    
    print(f"Values to be summed: {final_alignment}")
    return final_alignment

def combine_values(final_alignment):
    """The answer is obtained after summing the contents of the entire list."""
    answer = sum(final_alignment)
    return answer

if __name__ == "__main__":
    # Before immediately proceeding into converting the binary, a verification process takes place.
    # The verification checks for non-binary digits within "binary".
    binary = input("Enter a set of binary digits here: ")
    is_binary = verify_binary(binary)

    if is_binary:
        binary_length = len(binary)
        
        num_list = init_num_list(binary_length)
        alignment = align_to_decimal(binary, num_list)
        final_alignment = filter_digit_alignment(alignment)
        answer = combine_values(final_alignment)
        
        print(f"Binary to Decimal: {binary} => {answer}\n")
    else:
        print("Conversion was not successful.\n")