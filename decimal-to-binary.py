# As program name suggests, converts a decimal(integer) into binary
# Created after "binary-to-decimal.py" for back and forth conversion
# Might be useful soon?

def verify_decimal(decimal: int) -> list:
    """Checks if decimal is a whole number and if it only consists of integers."""
    try:
        int(decimal)
    except ValueError:
        print("Please insert a whole number")
        return False, 0
    else:
        # since input is always string, converts "decimal" to actual integers.
        return True, int(decimal)


def init_num_list(limit: int) -> list:
    """
    Creates "num_list" not exceeding the given limit. "num_list" will be
    used to add numbers within it."""
    num_list = []

    num = 1  # CONSTANT
    # Adds original number before increment since it is part of the alignment.
    starting_num = num
    num_list.append(starting_num)

    # Appends the summation of numbers to that are less than the given limit to "num_list".
    while num < limit:
        num += num

        # Periodically checks the elements, prevents including a greater number
        # than the limit from being added into the list.
        if num > limit:
            break
        else:
            num_list.append(num)

    # NOTE: Incorrect results will most likely happen if "num_list" is not in reverse!
    num_list.reverse()
    return num_list


def find_ones(decimal: int, num_list: list) -> list:
    """Finds the correct combination of numbers to be added and are then appended to "ones_list". """
    ones_list = num_list.copy()

    current = 0
    for selected in ones_list[:]:
        # Program attempts to add the current value to the selected element in "ones_list."
        # If "current", after being added to the selected element is higher than the given decimal,
        # it removes that element and then tries again.
        current += selected
        if current > decimal:
            current -= selected
            ones_list.remove(selected)

    print(f"Numbers used to get {decimal}: {ones_list}")
    return ones_list


def create_alignment(orig_num_list: list, ones_list: list) -> list:
    """
    Creates an alignment of binary digits and numbers from the given "num_list"
    Numbers in ones_list are assigned to '1' while the rest is '0'. """
    alignment = []

    for values in orig_num_list:
        # Program initializes 0s on all values in the original "num_list"
        # as binaries and appends them to "alignment".
        tmp = [values, '0']
        alignment.append(tmp)

    value = '1'
    for row in alignment:
        # Checks for numbers in ones_list that also exists in alignment.
        # If they do exist in both lists, it means that the value was used
        # to add to get the decimal.
        for item in row:
            if item in ones_list:
                row[1] = value  # alignment[0] numbers, alignment[1] bits.

    print(f"Alignment of binary and numbers: {alignment}")
    return alignment


def create_binary(alignment: list):
    """
    Creates and formats the actual binary using a provided alignment of
    individual binary digits and numbers.
    """
    tmp_list = []
    for row in alignment:
        # Removes the numbers.
        for _ in row:
            row.pop(0)

        # Appends to a new list and turns them into string.
        for digit in row:
            tmp_list.append(digit)

    str1 = ""
    binary = str1.join(tmp_list)

    return binary


if __name__ == "__main__":
    while True:
        user_input = input("Enter a decimal(integer) here: ")
        verification = verify_decimal(user_input)

        if verification:
            decimal = verification[1]

            num_list = init_num_list(decimal)
            ones_list = find_ones(decimal, num_list)
            alignment = create_alignment(num_list, ones_list)
            binary = create_binary(alignment)

            print(f"Decimal to Binary: {decimal} => {binary}\n")
        else:
            print("Conversion was not successful.\n")
