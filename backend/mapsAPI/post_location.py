import requests


class LocationMap:
    """Working with a new location"""

    def save_new_location_place_id(self):
        """Create and save new location's place_id"""

        server_url = 'https://rahulshettyacademy.com'
        post_path = '/maps/api/place/add/json'
        key = '?key=qaclick123'
        json_body_post_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        result_post = requests.post(server_url + post_path + key, json=json_body_post_location)
        assert result_post.status_code == 200
        if result_post.status_code == 200:
            print(f'Успешно! Код ответа: {result_post.status_code}')
        else:
            print(f'Провал! Ошибка в коде ответа. Полученный код: {result_post.status_code}')
        check_json = result_post.json()
        status = check_json.get('status')
        assert status == 'OK'
        if status == 'OK':
            print(f'Успешное создание новой локации. Статус: {status}')
        else:
            print(f'Провал. Ошибка статуса создания локации. Статус: {status}')

        place_id = check_json.get('place_id')
        print(f'place_id созданной локации: {place_id}')
        f = open('place_id.txt', 'a')
        f.write(f'{place_id}\n')
        f.close()

    def check_new_location_created(self):

        server_url = 'https://rahulshettyacademy.com'
        get_path = '/maps/api/place/get/json'
        key = '?key=qaclick123'
        with open('place_id.txt', 'r') as place_id:
            for lines in place_id:
                get_result = requests.get(server_url + get_path + key + '&place_id=' + str(lines).strip())
                assert get_result.status_code == 200
                if get_result.status_code == 200:
                    print(f'Успех! Локация существует в каталоге. Код ответа: {get_result.status_code}')
                else:
                    print(f'Провал! Созданной локации нет в каталоге. Код ответа: {get_result.status_code}')
            print('Тестирование окончено.')

    def delete_new_location(self):
        """Deleting second and fourth locations with saved place_id in place_id.txt"""

        server_url = 'https://rahulshettyacademy.com'
        delete_path = '/maps/api/place/delete/json'
        key = '?key=qaclick123'
        with open('place_id.txt', 'r') as f:
            i = 0
            while i <= 5:
                my_place_id = f.readline()
                i += 1
                if i == 2 or i == 4:
                    print(f'Удаление локации с place_id: {my_place_id.strip()}')
                    json_body_delete_location = {
                        "place_id": f"{my_place_id.strip()}"
                    }
                    delete_result = requests.delete(server_url + delete_path + key, json=json_body_delete_location)
                    assert delete_result.status_code == 200
                    if delete_result.status_code == 200:
                        print(f'Успех! Код ответа на удаление локации: {delete_result.status_code}')
                    else:
                        print(f'Провал! Код ответа на удаление локации: {delete_result.status_code}')
                    check_json = delete_result.json()
                    status = check_json.get('status')
                    assert status == 'OK'
                    if status == 'OK':
                        print(f'Успешное удаление локации. Статус: {status}')
                    else:
                        print(f'Провал. Ошибка статуса удаления локации. Статус: {status}')


new_location = LocationMap()
i = 1
while i <= 5:
    new_location.save_new_location_place_id()
    i += 1
new_location.delete_new_location()
