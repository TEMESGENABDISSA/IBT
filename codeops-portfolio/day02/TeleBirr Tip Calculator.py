bill_total=1000 
number_of_people=4
friends=[ 'temesgen','abdissa','chala',"tom"]

def split_bill(total, people, tip_rate=0.10):
     tip= total* tip_rate
     total_with_tip= total+tip
     each_person_pays = total_with_tip/people
     return each_person_pays

share= split_bill(bill_total,number_of_people)
# Step 6: Display bill information
# ----------------------------------------
print("Restaurant Bill:", bill_total, "ETB")
print("Number of People:", number_of_people)
print("Tip Rate: 10%")
print()
for friend in friends:
     print (friend, "pays",share, "ETB")