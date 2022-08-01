# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)


list_of_coord = "1 4 6 8"

def distance_betwee_two_dots(text : str):
    x1,y1,x2,y2 = list(map(int ,text.split()))
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

print(f"Distance between x1,y1,x2,y2 [{list_of_coord}] -> {distance_betwee_two_dots(list_of_coord):.2f}")