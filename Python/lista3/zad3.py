def usun_w_nawiasach(s):
    napis = ""

    nawias = False

    i = 0
    while i < len(s):
        if s[i] == '(':
            napis = napis[:i-1]
            nawias = True
        elif s[i] == ')':
            nawias = False
            i+=1

        if nawias == False:
            napis += s[i]
        i+=1
    return napis

print(usun_w_nawiasach("Ala ma (grubrgo) kota (i psa)!"))