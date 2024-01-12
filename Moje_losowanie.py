import pandas as pd

def sprawdz_w_historii(file_path, wybrane_glowne, wybrane_euro):
    try:
        data = pd.read_csv(file_path, header=None)
        kolumny_glowne = [2, 3, 4, 5, 6]
        kolumny_euro = [7, 8]

        for index, row in data.iterrows():
            historyczne_glowne = sorted([row[i] for i in kolumny_glowne])
            historyczne_euro = sorted([row[i] for i in kolumny_euro])
            if wybrane_glowne == historyczne_glowne and wybrane_euro == historyczne_euro:
                return True, row[0], row[1]
        return False, None, None
    except Exception as e:
        print("Wystąpił błąd:", e)
        return False, None, None

# Wprowadzenie liczb przez użytkownika
print("Podaj 5 głównych liczb (1-50), oddzielając je przecinkami:")
wybrane_glowne = sorted(list(map(int, input().split(','))))

print("Podaj 2 liczby Euro (1-10), oddzielając je przecinkami:")
wybrane_euro = sorted(list(map(int, input().split(','))))

# Ścieżka do pliku CSV
file_path = 'C:/Users/didym/Desktop/EJP/eurojackpot.csv'

# Sprawdzenie w historii
czy_trafiono, numer_losowania, data_losowania = sprawdz_w_historii(file_path, wybrane_glowne, wybrane_euro)

# Wynik
print(f"Twoje liczby: {wybrane_glowne}, Euro numery: {wybrane_euro}")
if czy_trafiono:
    print(f"Ten zestaw liczb padł w historii Eurojackpot. Numer losowania: {numer_losowania}, Data: {data_losowania}")
else:
    print("Ten zestaw liczb nie padł w historii Eurojackpot.")
