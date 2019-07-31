print("**************************************************\n kwota zarobiona odjac ubezpieczenie spoleczne,\n zaokraglenie do pelnej zlotowki,\n pomnozenie przez procent podatku,\n zaokraglamy,\n odejmujemy ubezpieczenie zdrowotne do odliczenia\n**************************************************\n\n")


kwota_zarobiona = float(input("Podaj zarobiona kwote (do 2och miejsc - uzyj kropki, a nie przecinka): "))
print("TWOJA zarobiona kwota to:",kwota_zarobiona,"zl") 

ubezp_zdrow_odl = 294.78
ubezp_spol = 555.89
procent_podatku = 0.085

# sprawdzamy
a = kwota_zarobiona - ubezp_spol
print(a)
b = round(a)
print(b)
c = b * 0.085
print(c)
d = round(c)
print(d)
e = d - 294.78
print(e)
f = round(e, 2)
print(f)

podatek = round((round(kwota_zarobiona - ubezp_spol) * procent_podatku)) - ubezp_zdrow_odl

print("Podatek do zaplaty wynosi:",round(podatek, 2),"zl")

print("\n")
input("Nacisnij ENTER aby wyjsc :-)")
