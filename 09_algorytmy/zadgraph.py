lista_obiektow = ['dom', 'muzeum', 'kino', 'restauracja', 'szpital', 'bar', 'teatr']


graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1]
]

for row in range(4):
    for col in range(5):
        if graph[row][col] == 1:
            print(lista_obiektow[row], '<--->', lista_obiektow[col])
