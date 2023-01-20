name=str(input('enter the student name:'))#total mark and percentage of five subject
sub1=float(input("enter the mark of c programming"))
sub2=float(input("enter the mark of data structure"))
sub3=float(input("enter the mark of web programming"))
sub4=float(input("enter the mark of software engineering"))
sub5=float(input("enter the mark of python"))
maximum_mark=1500
total=sub1+sub2+sub3+sub4+sub5#calculate total and percentage
percentage=(total/1500)*100
print("total mark:",total)#print total mark
print("percentage is:",percentage)#mark percentage
