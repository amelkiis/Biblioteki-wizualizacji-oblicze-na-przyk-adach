import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Przykładowe dane: Godziny nauki (zmienna niezależna) i wynik egzaminu (zmienna zależna)
godziny_nauki = np.array([3, 4, 5, 6, 7, 8, 9, 10])[:, np.newaxis]  # Przykładowe godziny nauki
wynik_egzaminu = np.array([40, 50, 55, 60, 65, 70, 75, 80])  # Przykładowe wyniki egzaminu

# Tworzenie i dopasowanie modelu regresji liniowej
regresja_liniowa = LinearRegression()
regresja_liniowa.fit(godziny_nauki, wynik_egzaminu)

# Obliczenie predykcji na podstawie modelu
predykcje = regresja_liniowa.predict(godziny_nauki)

# Wykres danych oraz prostej regresji
plt.scatter(godziny_nauki, wynik_egzaminu, label='Dane')
plt.plot(godziny_nauki, predykcje, color='red', label='Regresja liniowa')
plt.xlabel('Godziny nauki')
plt.ylabel('Wynik egzaminu')
plt.title('Regresja liniowa: Godziny nauki vs. Wynik egzaminu')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

# Przykładowe dane: Dwie cechy (zmienne niezależne) i przewidywana klasa (zmienna zależna)
cecha_1 = np.random.rand(100, 1)  # Przykładowa cecha 1
cecha_2 = np.random.rand(100, 1)  # Przykładowa cecha 2
klasa = np.random.randint(0, 2, size=(100,))  # Przykładowa klasa: 0 lub 1

# Tworzenie i dopasowanie modelu regresji logistycznej
regresja_logistyczna = LogisticRegression()
regresja_logistyczna.fit(np.hstack((cecha_1, cecha_2)), klasa)

# Tworzenie siatki danych do wizualizacji granic decyzyjnych
x_min, x_max = cecha_1.min() - 0.1, cecha_1.max() + 0.1
y_min, y_max = cecha_2.min() - 0.1, cecha_2.max() + 0.1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
siatka_danych = np.c_[xx.ravel(), yy.ravel()]

# Predykcja klas na podstawie modelu
predykcje = regresja_logistyczna.predict(siatka_danych)
predykcje = predykcje.reshape(xx.shape)

# Wykres danych oraz granic decyzyjnych
plt.figure()
plt.scatter(cecha_1, cecha_2, c=klasa, cmap='viridis', edgecolors='k')
plt.contourf(xx, yy, predykcje, alpha=0.3, cmap='viridis')
plt.xlabel('Cecha 1')
plt.ylabel('Cecha 2')
plt.title('Regresja logistyczna: Dwuwymiarowa klasyfikacja')
plt.show()
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Przykładowe dane: Dwie cechy (zmienne niezależne) i przewidywana klasa (zmienna zależna)
cecha_1 = np.random.rand(100, 1)  # Przykładowa cecha 1
cecha_2 = np.random.rand(100, 1)  # Przykładowa cecha 2
klasa = np.random.randint(0, 2, size=(100,))  # Przykładowa klasa: 0 lub 1

# Tworzenie i dopasowanie modelu KNN
model_knn = KNeighborsClassifier(n_neighbors=5)  # Ustalenie liczby sąsiadów na 5 (wartość przykładowa)
model_knn.fit(np.hstack((cecha_1, cecha_2)), klasa)

# Tworzenie siatki danych do wizualizacji granic decyzyjnych
x_min, x_max = cecha_1.min() - 0.1, cecha_1.max() + 0.1
y_min, y_max = cecha_2.min() - 0.1, cecha_2.max() + 0.1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
siatka_danych = np.c_[xx.ravel(), yy.ravel()]

# Predykcja klas na podstawie modelu KNN
predykcje = model_knn.predict(siatka_danych)
predykcje = predykcje.reshape(xx.shape)

# Wykres danych oraz granic decyzyjnych
plt.figure()
plt.scatter(cecha_1, cecha_2, c=klasa, cmap='viridis', edgecolors='k')
plt.contourf(xx, yy, predykcje, alpha=0.3, cmap='viridis')
plt.xlabel('Cecha 1')
plt.ylabel('Cecha 2')
plt.title('KNN: Dwuwymiarowa klasyfikacja')
plt.show()
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# Generowanie przykładowych danych
np.random.seed(42)
X = np.random.rand(100, 5)  # 100 przykładów, 5 cech
y = np.random.randint(0, 2, size=100)  # Przykładowe klasy: 0 lub 1

# Tworzenie instancji modeli
model_regresji_liniowej = LinearRegression()
model_regresji_logistycznej = LogisticRegression()
model_knn = KNeighborsClassifier()

# Ocena wydajności modeli za pomocą walidacji krzyżowej
wyniki_regresji_liniowej = cross_val_score(model_regresji_liniowej, X, y, cv=5)
wyniki_regresji_logistycznej = cross_val_score(model_regresji_logistycznej, X, y, cv=5)
wyniki_knn = cross_val_score(model_knn, X, y, cv=5)

# Wydrukowanie wyników
print("Wyniki regresji liniowej:", wyniki_regresji_liniowej.mean())
print("Wyniki regresji logistycznej:", wyniki_regresji_logistycznej.mean())
print("Wyniki KNN:", wyniki_knn.mean())
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Przykładowa wizualizacja danych
data = np.random.randn(100)
plt.hist(data, bins=20)
plt.xlabel('Wartości')
plt.ylabel('Liczba wystąpień')
plt.title('Histogram danych')
plt.show()

# Przykładowa wizualizacja krzywej uczenia
epochs = range(1, 11)
train_loss = np.random.rand(10)
val_loss = np.random.rand(10)

plt.plot(epochs, train_loss, 'b', label='Strata treningowa')
plt.plot(epochs, val_loss, 'r', label='Strata walidacyjna')
plt.title('Krzywa uczenia')
plt.xlabel('Epoki')
plt.ylabel('Strata')
plt.legend()
plt.show()

# Przykładowa wizualizacja macierzy korelacji
data = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
corr_matrix = data.corr()
sns.heatmap(corr_matrix, annot=True)
plt.title('Macierz korelacji')
plt.show()
