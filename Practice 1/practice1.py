sia = ["abc", "d", "efghi", "j", "klmnop", "qr", "st", "uv", "wxyz"]
name = sia[4][3] + sia[0][0] + sia[-3][1] + sia[0][0] + sia[4][1] + sia[2][-1]
lastname = sia[0][1] + sia[-2][0] + sia[0][1] + sia[-2][0] + sia[-3][1] + sia[2][0] + sia[2][-1] + sia[-3][0] + sia[2][-2] + sia[-2][1] + sia[2][-1] + sia[4][1] + sia[2][-1]
print(name)
print(lastname)

lasttwoofname = name[-2:]
firstthreeoflastname = lastname[:3]
print(lasttwoofname)
print(firstthreeoflastname)

variable1 = input("variable1:")
variable2 = input("variable2:")
variable3 = [3]

sia.append(variable1)
sia.append(variable2)

sia += variable3
print(sia)

