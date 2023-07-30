from backend.SWAPI.http_methods import HttpMethod

"""Working with SWAPI: open api recourse. Star Wars data"""


base_url = 'https://swapi.dev/api/'         # Main url for all requests

class Swapi:
    """Methods to get information about films and characters"""

    @staticmethod
    def characters_films(character_endpoint):
        """Get all films with a character"""

        get_character_info_url = base_url + character_endpoint
        get_character_info = HttpMethod.get(get_character_info_url)
        if get_character_info.status_code == 200:
            print(f'Запрос на получение информации о персонаже успешно выполнен')
        else:
            print(f'Произошла ошибка при выполнении запроса. Код ошибки: {get_character_info.status_code}')
        check_json = get_character_info.json()
        name = check_json.get('name')
        films = check_json.get('films')
        count = len(films)
        if count == 1:
            print(f'Найден {len(films)} фильм с участием {name}')
        elif 1 < count <= 4:
            print(f'Найдено {len(films)} фильма с участием {name}')
        elif 5 <= count <= 10:
            print(f'Найдено {len(films)} фильмов с участием {name}')
        return films

    @staticmethod
    def get_film_cast(films_url):
        """Get list of characters in film"""

        films_amount = len(films_url)
        i = 0
        result = []
        while i < films_amount:
            get_film_info = HttpMethod.get(films_url[i])
            if get_film_info.status_code == 200:
                check_json_film = get_film_info.json()
                title = check_json_film.get('title')
                print(f'Запрос на получение информации о фильме {title} успешно выполнен')
                result = result + check_json_film.get('characters')
                i += 1
            else:
                print(f'Произошла ошибка при выполнении запроса. Код ошибки: {get_film_info.status_code}')
        print('Ожидание... Сбор информации')

        with open('cast_names.txt', 'a', encoding='utf-8') as f:
            uniq_characters = list(dict.fromkeys(result))
            for a in uniq_characters:
                get_character_info = HttpMethod.get(a)
                check_json_name = get_character_info.json()
                name = check_json_name.get('name')
                if name != 'Darth Vader':
                    f.write(f'{name}\n')
            print(f'Список имен персонажей успешно сохранен в файле cast_names.txt')
            return uniq_characters


char = Swapi.characters_films('people/4/')      # should be in separate module. it's here for example of working code
film = Swapi.get_film_cast(char)
