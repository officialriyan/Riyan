# saarc = ["Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal", "Pakistan", "Sri-Lanka"]
# print(saarc[1])
#
# countryName = input("Enter your country name :")
# if countryName in saarc:
#     print("countryName in Saarc")
# else:
#     print("Not in saarc")
#
# district = ["Dhaka", "Barishal", "Cumilla", ]
# print(district[0])


mark = int(input("Enter your result  "))
if 0 <= mark <= 32:
    print("Failed")
if mark >= 33 and mark <= 39:
    print("D")
if mark >= 40 and mark <= 49:
    print("C")
if mark >= 50 and mark <= 59:
    print("B")
if mark >= 60 and mark <= 69:
    print("A-")
if mark >= 70 and mark <= 79:
    print("A")
if mark >= 80 and mark <= 100:
    print("A+")
    print("Thank You")
