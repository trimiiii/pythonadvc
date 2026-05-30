studentat = ["eldon", "liza","trimi","ylli"]

print(studentat)
print(studentat[0])
print(studentat[2])
print(studentat[3])
print(studentat[1])

studentat.append("donjeta")
studentat.insert(6,"donjetaa")

print(studentat.count("donjeta"))
studentat.remove("trimi")


lista2 = studentat.copy()
lista2.clear()
print(lista2)
print("ylli eshte ne nje pozicion e : " studentat.index("ylli"))

print(studentat)