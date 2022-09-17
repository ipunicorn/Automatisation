from src.csv_reader import CSVReader
from src.json_reader import JsonReader
from src.json_writer import JsonWriter

if __name__ == '__main__':
    books_reader = CSVReader("./files/books.csv")
    users_reader = JsonReader("./files/users.json")

    users = users_reader.read()
    books = books_reader.read()

    users_list = []

    for el in users:
        users_list.append({"name": el["name"],
                           "gender": el["gender"],
                           "address": el["address"],
                           "age": el["age"],
                           "books": []})

    books_list = []
    for el in books:
        books_list.append({"title": el["Title"],
                           "author": el["Author"],
                           "pages": el["Pages"],
                           "genre": el["Genre"]})

    j = 0
    for i in range(len(books_list)):
        if j == len(users_list):
            j = 0
        users_list[j]['books'].append(books_list[i])
        j += 1

    writer = JsonWriter("./files/result.json")
    writer.write(users_list)
 
# from src.Rectangle import Rectangle
# from src.Square import Square
# from src.Triangle import Triangle

# if __name__ == '__main__':
#     new_rectangle = Rectangle(1, 1)
#     new_square = Square(1)
#     new_triangle = Triangle(1, 1, 1)

#     print(new_square.add_area(new_rectangle))

