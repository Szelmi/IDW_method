import csv
import numpy as np
import idw
import matplotlib.pyplot as plt

with open('sensor_locations.csv', newline='') as f:
    reader = csv.reader(f)
    sensors_data_csv = list(reader)

with open('may-2017.csv', newline='') as f:
    reader = csv.reader(f)
    may_data_csv = list(reader)

may_data_csv = may_data_csv[1:2]
may_data = []
for i in range(1, len(may_data_csv[0]) // 6):
    if may_data_csv[0][6 * i] == '':
        may_data.append(0)
    else:
        may_data.append(float(may_data_csv[0][6 * i]))

sensors_data = np.zeros((56, 3))
for i in range(1, len(sensors_data_csv)):
    for j in range(0, len(sensors_data_csv[i])):
        sensors_data[i - 1][j] = float(sensors_data_csv[i][j])

vals = []
for i in range(0, 20):
    vals.append(idw.idw_method(50.057746, 19.961373, sensors_data, may_data, i))


plt.plot(vals)
plt.xlabel("Wartość parametru p")
plt.ylabel("Wartość zinterpolowana")
plt.show()

print(vals)


# W przypadku uruchomienia algorytmu, który poszukuje interpolowanej wartości w pobliżu aktualnej znanej wartości,
# (w tym przypadku dla czujnika o id 140), była interpolowana wartość, znajdująca się w pobliżu tego czujnika),
# współrzędne punktu w którym interpolujemy, to: 50.057746 19.961373 (o 10^-6) różnicy z punktem o id 140.
# W przypadku uruchomienia algorytmu dla rożnych wartości współczynnika p, wraz ze zwięszkaniem wartości parametru p,
# otrzymujemy coraz lepsze wyniki, znajdujące się coraz bliżej wartości oczekiwanej. Optymalne rozwiązania
# (o różnicy mniejszej niż 0.1), otrzymujemy dla parametru p większego niż 10. Wtedy obliczane współczynniki wagowe są
# na tyle zróżnicowane, żeby zdecydowanie większe znaczenie w obliczanej wartości miały współczynniki najbliższe
# punktowi, który chcemy interpolować. Metoda IDW, dla dużych wartości współczynnika p, nadaje się do interpolacji
# wyników z sensorów jakości powietrza.
