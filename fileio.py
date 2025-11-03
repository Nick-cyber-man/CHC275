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