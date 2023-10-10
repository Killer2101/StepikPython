# TODO Найдите количество книг, которое можно разместить на дискете
str_ = 25*4
stroki = str_*50
stranici = stroki*100
kniga = stranici / 1024 / 1024
disketa = 1.44
knigi = round(disketa / kniga)

print("Количество книг, помещающихся на дискету:", knigi)
