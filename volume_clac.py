#상자의 입력값
width  = float(input("Width:"))
length = float(input("Length:"))
heigth = float(input("Heigth:"))
#부피계산
volume = width * length * heigth

print("Volume:", volume, "cm^3")
#총길이계산
total_length = width + length + heigth
#총길이 별 택배요금
if    total_length <= 80:
      charge = 5000
elif  total_length <= 100:
      charge = 8000
elif  total_length <= 120:
      charge = 10000
elif  total_length <= 160:
      charge = 13000
else  :
      charge = "unavailable"

print("Total length:", total_length)
print("Charge:", charge)
print("git test")