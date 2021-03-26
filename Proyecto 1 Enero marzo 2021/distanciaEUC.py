import sys

def distancia(tupla1, tupla2):

    x_d = tupla1[0] - tupla2[0]
    y_d = tupla1[1] - tupla2[1]
    d_ij = abs(mt.sqrt((x_d ** 2 )+ (y_d ** 2)))
    
    return int(d_ij)

print("Distancia entre {} y {} es: {}".format(sys.argv[1], sys.argv[2], distancia(sys.argv[1], sys.argv[2])))

