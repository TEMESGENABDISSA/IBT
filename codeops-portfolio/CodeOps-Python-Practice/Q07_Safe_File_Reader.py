def read_numbers(filename):
    numbers = []

    try:
        with open(filename, "r") as file:

            for line_number, line in enumerate(file, start=1):

                try:
                    numbers.append(int(line.strip()))

                except ValueError:
                    print(
                        f"Warning: Invalid number at line {line_number}"
                    )

    except FileNotFoundError:
        print(
            f"Error: File '{filename}' does not exist."
        )
        return []

    return numbers