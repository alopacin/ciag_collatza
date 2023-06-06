#Program wypisujacy dla podanej liczby ciag Collatza
x = int(input('Podaj liczbę całkowitą od 1 do 100: ' ))
while True:
    if x % 2 == 0 and x != 1 :
        x = x/2
        x = int(x)
        print(x)
    elif x % 2 != 0 and x != 1:
        x = (x * 3) + 1
        x = int(x)
        print(x)
    else:
        break
        print(x)