# dictionary name
footballClubs = {
    "a" : "Arka",
    "b" : "Lechia",
    "c" : "Legia",
    "d" : "Wisła",
    "e" : "Śląsk",
    "f" : "Pogoń",
    "g" : "Ruch",
    "h" : "Górnik"
}

print(footballClubs["e"])
print(footballClubs.get("e"))
print(footballClubs.get("i", "Klub nie istnieje"))