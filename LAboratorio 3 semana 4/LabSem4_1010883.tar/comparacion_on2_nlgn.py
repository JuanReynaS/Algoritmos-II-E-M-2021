# Descripción: Este módulo esta encargado de mostrar los resultados de los
#              algoritmos de ordenamiento simple y los resultados de mergesort
#              three para poder estudiarlos.

#              El módulo run_sortlib.py genera archivos:
#              Algoritmo_nlgn.csv, Algoritmos_on2.csv

#              Este módulo procesara los datos de los los archivos CSV
#              y los mostrará de forma que permita evaluación de los resultados
#              arrojado por los algortimos de ordenamiento.

#             La ejecución de este módulo se hace a través de la siguiente
#             línea de comando:
#
#             >./ python3 comparacion_on2_nlgn.py

# Creado por: Juan Reyna
# email: 10-10883@usb.ve


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd.set_option("max_rows", None)

alg_nlgn = pd.read_csv('Algoritmos_nlgn.csv', sep='\t')
alg_on2 = pd.read_csv('Algoritmos_on2.csv', sep='\t')

alg_nlgn = pd.DataFrame(alg_nlgn)  # Dataframe
alg_on2 = pd.DataFrame(alg_on2)  # DataFrame


print("\n\n******************** MERGE DE DATAFRAME *******************\n\n")
dat = pd.concat([alg_nlgn, alg_on2], sort=False, ignore_index=True)
lista = dat['Num. de elementos'].tolist()
lista = sorted(list(set(lista)))
print(lista)
for i in lista:
    # (dat['Algoritmos'] != "MergeOPT") &
    mer = dat[(dat['Algoritmos'] != "MergeIterativo") & (dat['Algoritmos'] != "MergeThree") & (dat['Algoritmos'] != "MergeSort") & (dat['Num. de elementos'] == i)]
    mer1 = dat[(dat['Algoritmos'] == "MergeThree") & (dat['Num. de elementos'] == i)]
    print(mer)
    print(mer1, "\n")
    for i in mer1.index:
        for j in mer.index:
            if mer["Tiempo(seg)"][j] < mer1["Tiempo(seg)"][i]:
                print("{} es mas rápido que: {}".format(mer["Algoritmos"][j], mer1["Algoritmos"][i]))
                print(mer["Algoritmos"][j], mer["Tiempo(seg)"][j])
                print(mer1["Algoritmos"][i], mer1["Tiempo(seg)"][i],"\n")

# gráfica los datos si -g esta activo
sns.lineplot(data=dat, x="Num. de elementos", y="Tiempo(seg)",
             hue="Algoritmos", err_style="bars")
plt.show()
