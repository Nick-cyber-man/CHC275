names = ["John","Paul","Luke"]
gradelevels = [12,11,10]
GPAs = [90,74,65]

print(f"Student records for {names[0]}. Gradelevel: {gradelevels[0]}. GPA: {GPAs[0]}")

for i in range(len(names)):
    print(f"Student records for {names[i]}. Gradelevel: {gradelevels[i]}. GPA: {GPAs[i]}")