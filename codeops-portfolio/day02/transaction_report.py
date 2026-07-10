INPUT_FILE = "transactions.txt"
OUTPUT_FILE = "report.txt"


def read_transactions(filename):

    totals = {}

    try:
        file = open(filename, "r")

        for line in file:
            name, amount = line.strip().split(",")

            amount = float(amount)

            totals[name] = totals.get(name, 0) + amount

        file.close()

    except FileNotFoundError:
        print("File not found!")
        return {}

    return totals



def print_summary(totals):

    sorted_totals = sorted(
        totals.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for name, amount in sorted_totals:
        print(f"{name}: {amount:.2f}")



def write_report(totals, filename):

    sorted_totals = sorted(
        totals.items(),
        key=lambda x: x[1],
        reverse=True
    )


    file = open(filename, "w")

    for name, amount in sorted_totals:
        file.write(f"{name}: {amount:.2f}\n")

    file.close()



def main():

    totals = read_transactions(INPUT_FILE)

    print_summary(totals)

    write_report(totals, OUTPUT_FILE)



if __name__ == "__main__":
    main()