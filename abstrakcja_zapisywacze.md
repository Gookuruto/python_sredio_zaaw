
### Zadanie:

Stwórz abstrakcyjną klasę bazową `ZapisywaczDanych`, która będzie definiować interfejs zapisywania danych do różnych formatów (CSV, JSON, pickle i XML). Następnie stwórz klasy potomne, które będą dziedziczyć po klasie bazowej i implementować odpowiednie metody zapisywania danych do każdego formatu.

W tym rozwiązaniu definiujemy abstrakcyjną klasę bazową `ZapisywaczDanych`, która zawiera metodę abstrakcyjną `zapisz_dane()`. Następnie tworzymy klasy potomne (`ZapisywaczCSV`, `ZapisywaczJSON`, `ZapisywaczPickle` i `ZapisywaczXML`), które dziedziczą po klasie bazowej i implementują metodę `zapisz_dane()` dla każdego formatu. Na końcu prezentujemy przykładowe użycie każdego zapisywacza dla danych testowych.