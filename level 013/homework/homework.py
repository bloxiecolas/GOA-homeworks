#) მომხმარებელს შეაყვანინე ორი რიცხვი. დაბეჭდე, პირველ რიცხვზე მეტია თუ არა მეორე რიცხსზე

num1 = int (input("enter sny num"))
num2 = int (input("enter sny num"))

print (num1<num2)


#2) მომხმარებელს შეაყვანინე გამოცდის ქულა. შეამოწმე, აიღო თუ არა მან 50 ან მეტი ქულა.

tryingcoin = int (input("whats your score"))
print (tryingcoin<50)


#) მომხმარებელს შეაყვანინე ტემპერატურა. შეამოწმე, არის თუ არა ტემპერატურა 30 გრადუსზე მეტი.

temp = int (input("what temp"))
print (temp<30)




#4) მომხმარებელს შეაყვანინე რიცხვი. შეამოწმე, უდრის თუ არა ის ნულს.
num4 = int (input("enter sny num"))
print (num4==0)



#5) მომხმარებელს შეაყვანინე მართკუთხედის სიგრძე და სიგანე. გამოთვალე ფართობი და შეამოწმე, 
# მეტია თუ არა ის 100-ზე. (ფართობის დასათვლელად მართკუთხედის სიგრძე გაამრავლეთ სიგანეზე)


size = int (input("what num"))
width = int (input("what num"))
print (size<100)
print (width<100)




#6) მომხმარებელს შეაყვანინე ორი ადამიანის ხელფასი. შეამოწმე:
# პირველი ადამიანის ხელფასი მეტია თუ არა მეორისაზე.
# აქვთ თუ არა თანაბარი ხელფასი.


firstperson = int (input("whats your balance"))
secondperson = int (input("whats your balance"))
print (firstperson==100)
print (secondperson==100)


#7) მომხმარებელს შეაყვანინე ორი ადამიანის ასაკი.
#  გამოთვალე ასაკებს შორის სხვაობა და შეამოწმე, არის თუ არა სხვაობა 5 წელზე მეტი.
year = int (input("what year"))
print (year<100)


#8)მომხმარებელს შეაყვანინე ანგარიშზე არსებული თანხა და პროდუქტის ფასი. 
# შეამოწმე, საკმარისია თუ არა თანხა პროდუქტის შესაძენად.
balance1 = int ("whats the price")
max = 100
print (balance1<max)



#9)მომხმარებელს შეაყვანინე სპორტსმენის ასაკი და სიმაღლე. შეამოწმე:
# არის თუ არა მისი ასაკი 18 ან მეტი.
# არის თუ არა მისი სიმაღლე 180 სმ-ზე მეტი.

age1 = int (input("whats your age"))
height = int (input("whats your height"))
print (age1<18)
print (height<180)



#10) მომხმარებელს შემოაყვანინე ორი მეგობრის სახელი და შემდეგ შეადარე ისინი  ერთმანეთს,
#  ახსენი როგორ შესრულდა შედარება და რატომ გამოიტანა ასეთი პასუხი.

friend = input ("whats your friends name")
friend2 = input ("whats your friends name")
print (friend<friend2)