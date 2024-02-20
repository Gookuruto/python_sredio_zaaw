1. **Klasy bazowe:**
   Stwórz dwie klasy bazowe `Animal` i `Machine`, które będą miały odpowiednie metody i atrybuty.

2. **Klasa potomna:**
   Stwórz klasę potomną `Robot`, która będzie dziedziczyć zarówno po klasie `Animal`, jak i `Machine`. Klasa `Robot` powinna mieć dodatkowe metody i atrybuty specyficzne dla robotów.

3. **Metody konfliktowe:**
   Dodaj metody o tej samej nazwie w klasach bazowych `Animal` i `Machine`, a następnie zobacz, co się stanie, kiedy spróbujesz wywołać tę metodę z klasy potomnej `Robot`.

4. **Wywoływanie metod z klas bazowych:**
   W klasie `Robot` wywołaj metody z klas `Animal` i `Machine`, aby pokazać, że możesz korzystać z funkcjonalności obu klas bazowych.

5. **Atrybuty konfliktowe:**
   Stwórz atrybuty o tej samej nazwie w klasach bazowych `Animal` i `Machine`, a następnie sprawdź, jakie wartości będą miały te atrybuty w klasie `Robot`.

6. **Przesłanianie metod:**
   Stwórz metodę o tej samej nazwie w klasach `Animal` i `Machine`, a następnie w klasie `Robot` stwórz metodę o tej samej nazwie. Sprawdź, która metoda zostanie wywołana, gdy użyjesz jej z obiektu klasy `Robot`.

7. **Zastosowanie super():**
   Wykorzystaj funkcję `super()` w klasie `Robot`, aby wywołać metody z klas bazowych `Animal` i `Machine`.

8. **Przeciążanie operatorów:**
   Dodaj przeciążenie operatorów do klas `Animal` i `Machine`, a następnie stwórz odpowiednie implementacje w klasie `Robot`.