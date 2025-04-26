class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: {self.movies}"


class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: {self.movies}"


# Создание объектов Comedy и Drama
comedy = Comedy()
drama = Drama()

# Добавление фильмов и вывод результата
print(comedy.add_movie('Большой куш'))  # Вывод: Комедии: ['Большой куш']
print(drama.add_movie('Оружейный барон'))  # Вывод: Драмы: ['Оружейный барон']