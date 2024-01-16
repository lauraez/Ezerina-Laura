#   izveidot sarakstu 'atzimes' ar punktiem (testa iegutajiem) (10 rezultaati no 60 lidz 99)
#   ar for ciklu iziet cauri visam sarakstam
#   ar elif nosacijumu uz ekrana paradiit punktus un atzimi
#   >=90 - a   >=80 - b   starp 70 un 80 - c    no 60 lidz 70 - d    ja zem 60 - f

#   grutak - var pielikt datu ievadi atkariba no ievadita skaitla paradit burtu

#int(input())
#[90, 85, 80, 75, 70, 65, 60, 98, 81, 69]


atzimes = [int(input('punkti = '))]
rezult = []
for punkti in atzimes:
    if punkti >=90:
        atzime = 'A'
    elif punkti >=80:
        atzime = 'B'
    elif punkti >=70:
        atzime = 'C'
    elif punkti >=60:
        atzime = 'D'
    else:
        atzime = 'F'
    rezult.append([punkti, atzime])
print(rezult)

