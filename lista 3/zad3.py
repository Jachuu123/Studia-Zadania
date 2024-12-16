def remove_parentesis(text):
    is_valid = True
    str = ""
    for char in text:
        if char == "(":
            is_valid = False
        if is_valid:
            str+= char

        if char == ")":
            is_valid = True
    return str



print(remove_parentesis("1. Ala ma kota (perskiego)!"))
print(remove_parentesis("2. Wczoraj (choć padał deszcz) poszedłem na spacer, a po drodze (całkiem niespodziewanie) spotkałem starego znajomego."))
print(remove_parentesis("3. Zrobiłem ciasto (według nowego przepisu), ale zapomniałem dodać cukru (co nie było najlepszym pomysłem)."))
print(remove_parentesis("4. W przyszłym tygodniu (o ile wszystko pójdzie zgodnie z planem) wyjedziemy na wakacje (mam nadzieję, że pogoda dopisze)."))
print(remove_parentesis("5. Książka, którą czytam (choć jest bardzo długa), wciąga mnie coraz bardziej (szczególnie rozdział trzeci)."))
print(remove_parentesis("6. Spotkanie zostało przełożone na jutro (z powodu nieobecności kilku osób), więc będziemy musieli przygotować prezentację (może to być wyzwanie)."))