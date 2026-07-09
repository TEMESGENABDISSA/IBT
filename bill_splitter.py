# Bill Splitter Program

bill = 1000
people = 4

names = ["Temesgen", "efrem", "nat","rich" ]

def split_bill(total, people, tip_rate=0.10):
    total = total + (total * tip_rate)
    return total / people

amount = split_bill(bill, people)

for name in names:
    print(name, "pays", amount, "ETB")