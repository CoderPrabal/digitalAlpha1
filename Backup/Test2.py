import numpy as np
list_of_name=[]
list_of_sub1=[]
list_of_sub2=[]
list_of_sub3=[]

for i in range(0,5):
    name=input("Enter the name of student")
    list_of_name.append(name)
    sub1=float(input("Enter the marks in subject1"))
    list_of_sub1.append(sub1)
    sub2=float(input("Enter the marks in subject2"))
    list_of_sub2.append(sub2)
    sub3=float(input("Enter the marks in subject3"))
    list_of_sub3.append(sub3)
    
#print the table

print("Name    Subject1  Subject2   Subject3")
for i in range(0,5):
    print(list_of_name[i]+"       "+str(list_of_sub1[i])+"      "+str(list_of_sub2[i])+"      "+str(list_of_sub3[i]))
    
print()
print()
print()
array_sub1=np.array(list_of_sub1)
array_sub2=np.array(list_of_sub2)
array_sub3=np.array(list_of_sub3)
print("The mean of the first subject",np.mean(array_sub1))
print("The mean of the second subject",np.mean(array_sub2))
print("The mean of the third subject",np.mean(array_sub3))
print("The median of the first subject",np.median(array_sub1))
print("The median of the second subject",np.median(array_sub2))
print("The median of the third subject",np.median(array_sub3))
array_final=array_sub1+array_sub2+array_sub3
array_percentage=(array_final/10)*100
dict_stu={array_final[i]:list_of_name[i] for i in range(0,5)}
print(dict_stu)

for i in range(0,5):
    print(list_of_name[i]+"  "+str(array_percentage[i]))
    if array_percentage[i]>=90:
        print(list_of_name[i]+" "+" Grade A+")
    elif array_percentage[i]>=80 and array_percentage[i]<90:
        print(list_of_name[i]+" "+" Grade A")
    elif array_percentage[i]>=70 and  array_percentage[i]<80:
        print(list_of_name[i]+" "+" Grade B+")
    elif  array_percentage[i]>=60 and  array_percentage[i]<70:
        print(list_of_name[i]+" "+" Grade B")
    elif array_percentage[i]>=50 and  array_percentage[i]<60:
        print(list_of_name[i]+" "+" Grade C")
    else:
        print(list_of_name[i]+" "+" Grade D")
            

