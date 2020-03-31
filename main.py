# main.py
#main to nazwa aplikacji
#w konsoli można uruchomić aplikację za pomocą uvicorn main:app
#main odnosi się do plik main.py, app - to obiekt stworzony wewnątrz main.py
#można też: uvicorn mian:app -- reload, wtedy kod sie odsieży jesli sa jakies ziany w pliku main.py


from fastapi import FastAPI #pobieramy moduł FastApi, jest on zainstalowany w srd_1 (venv)
# FastAPI to klasa w pythonie, zapewnia funkcjonalność API (interfejs programistyczny aplikacji)


app = FastAPI() # stworzenie instancji, app to egzemplarz klasy FastAPI
# właśnie do tej nazwy oswołujemy się przy uvicorn

#dekorator - @  bierze funkcję pod soba i coś z nią robi
#path operation decorator
@app.get("/") #dekorator, GET - to pobranie zasobu
#stworzenie ścieżki, odnosi się do ostatniej czesci URL po pierwszym /
# np. https://example.com/items/foo, scieżką jest /items/foo
#sciezka jest rownież nazywana 'endpoint' lub 'route'
# powyższy kod mówi: weź funkcję pod sobą i idź do ścieżki '/' i użyj operacji GET
# GET - operator który czyta dane

# path operation function 
def root():
    return {"message": "Hello World"} # na stronie zobaczymy - JSON response

#JSON - to format wymiany danych w środowisku internetowym
#JSON dane tekstowe, JSON to łańcuch znaków
#JSON to skrót: JavaScript Object Notation
#warto zwrócić uwagę że musi być podwójny cudzysłów
#Najczęściej jest wykorzystywany do przekazywania i odbierania danych z serwera przez aplikacje na stronie internetowej.

# można returnować słownik (tu), listę, pojedyńcze wrtosci jak str, int itd.
