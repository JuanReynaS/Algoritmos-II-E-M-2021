import string as st
import sys

def esPalabraValida(s):
    assert(type(s) == str)
 
    lista1 = [i for i in st.ascii_letters]
    lista1.insert(14,"ñ")

    for letra in lista1:
        if not (letra in st.ascii_lowercase):
            return False
    return True

def distance(s1, s2):
  d=dict()
  for i in range(len(s1)+1):
     d[i]=dict()
     d[i][0]=i
  for i in range(len(s2)+1):
     d[0][i] = i
  for i in range(1, len(s1)+1):
     for j in range(1, len(s2)+1):
        d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not s1[i-1] == s2[j-1]))
  return d[len(s1)][len(s2)]


print(esPalabraValida(sys.argv[1]))

print(distance(sys.argv[2], sys.argv[3]))