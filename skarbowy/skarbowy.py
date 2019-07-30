print("*************************************************\n kwota zarobiona minus ubezpieczenie spoleczne,\n zaokraglenie do pelnej zlotowki,\n pomnozenie razy procent podatku,\n zaokraglamy,\n odejmujemy ubezpieczenie zdrowotne do odliczenia\n*************************************************\n\n")
print("Podaj zarobiona kwote: ")

input()

ubezp_zdrow_odl = 294.78
ubezp_spol = 555.89
procent_podatku = 0.085

podatek = (7000 - ubezp_spol) * procent_podatku - ubezp_zdrow_odl

print("Podatek do zaplaty wynosi:",podatek,"zl")

print("\n")
input("Wcisnij ENTER aby wyjsc :-)")