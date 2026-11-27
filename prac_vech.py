vech_type = input("enter vechile type: ")
hrs = int(input("enter number of parking hrs: "))

if vech_type == "2-wheeler":
    Fee = 20 * hrs 
elif vech_type == "3-wheeler":
    Fee = 50 * hrs
elif vech_type == "heavy-vech":
    Fee = 100 * hrs
else:
    Fee = 0
    print("invalid vechile type ...")

print("----Vechile parking details----")
print("Vechile type:" , vech_type)
print("Parking duration: ", hrs)
print("total parking fee: ", Fee)    