t = int(input("Indique un tiempo:"))
h = "h"
m = "m"
s = "s"
tiempo = str(t) + s if 0 <= t < 60 else str(t // 60) + m
print(tiempo)

jo = 230000000000000
print(jo)
if not jo:
	print("chao")
