print("**************************************************\n kwota zarobiona odjac ubezpieczenie spoleczne,\n zaokraglenie,\n pomnozenie przez procent podatku,\n zaokraglamy,\n odejmujemy ubezpieczenie zdrowotne do odliczenia\n**************************************************\n\n")


kwota_zarobiona = float(input("Podaj zarobiona kwote (do 2och miejsc - uzyj kropki, a nie przecinka): "))
print("TWOJA zarobiona kwota to:",kwota_zarobiona,"zl\n") 

ubezp_zdrow_odl = 312.02
ubezp_spol = 609.14
procent_podatku = 0.085

# sprawdzamy
a = kwota_zarobiona - ubezp_spol
print(a)
b = round(a, 2)
print(b)
c = b * procent_podatku
print(c)
d = round(c, 2)
print(d)
e = d - ubezp_zdrow_odl
print(e)
f = round(e, 2)
print(f)

# liczymy xD
podatek = round(round(kwota_zarobiona - ubezp_spol, 2) * procent_podatku, 2) - ubezp_zdrow_odl

print("\n")
print("Podatek do zaplaty wynosi:",round(podatek, 2),"zl\n")

input("Nacisnij ENTER aby wyjsc :-)")
