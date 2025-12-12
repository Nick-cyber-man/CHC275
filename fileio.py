file = open("names.txt","r")
buffer = file.readlines()
print(buffer)
file.close()

names = []
grades = []
for line in buffer:
    line = line.strip()
    line = line.split(",")
    names.append(line[0])
    line[1] = int(line[1])
    grades.append(line[1])
print(names)
print(grades)

#file = open("name.txt","w")
#line = "hello world"
#file.write(line)
#file.close()

file = open("names.txt", "w")
for i in range(len(names)):
    line = f"{names[i]},{grades[i]}\n"
    buffer.append(line)
     
buffer[-1] = buffer[-1].strip()
file.writelines(buffer)
file.closed()

try:
    name = input("enter your name: ").strip()
    grade = input("enter yourt grade: ")
    grade = int(grade)
except Exception as e:
    print(e)
else:
    file = open("names.txt", "a")
    line = f"\n{name},{grade}"
    file.write(line)
    file.close()
    
date = "Nov42025"
file = open(date,"w")
avg = sum(grades)/len(grades)
line = f"the average GPA on {date} is {avg}"
file.write(line)
file.close()
