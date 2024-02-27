# import pickle
#
#
# class KlasaDoZapisu:
#     def __init__(self,nazwa):
#         self.nazwa = nazwa
#     def __str__(self):
#         return f'obiekt {self.nazwa}'
# #
# obiekt_do_zapisu = KlasaDoZapisu('pierwszyobiekt')
# obiekt_do_zapisu2 = KlasaDoZapisu(' obiekt dwa')
# obiekt_do_zapisu3 = KlasaDoZapisu('obiekt trzy')
# data = [obiekt_do_zapisu,obiekt_do_zapisu2,obiekt_do_zapisu3]
#
# with open('data.pickle', 'wb') as f:
#     pickle.dump(data, f)
# # print(data)
# # print(obiekt_do_zapisu3)
#
# #2 1/2 Deserializacja danych: Napisz program, który odczytuje listę obiektów z pliku
# #2 2/2 utworzonego przez pickle i wyświetla jej zawartość
#
# with open('data.pickle', 'r') as rf:
#     odczyt = pickle.load(rf)
#
# print(odczyt)
# for itrem in odczyt:
#     print(itrem.nazwa)

with open("file.txt")as f:
    pass
for line in f:
    print(line)