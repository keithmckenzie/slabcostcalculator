#Slab Calculator
#Keith McKenzie
#08/12/21

print("Slab Calculator")
print("")
wide = input("How many slabs horizontal: ")
deep = input("How many slabs vertical: ")
cost = input("Cost much does one tile cost(£): ")
print("")

Nslabs= int(wide)*int(deep)
Tcost = Nslabs * float(cost)
print("")
print("Number of slabs required: " + str(Nslabs))
print("Total cost (£): " + str(Tcost))
print("")
print("Thank you for using Slab Calculator")

if Tcost == 0:
    print("Well done in getting such a good deal!")

input("Press Enter to close...")