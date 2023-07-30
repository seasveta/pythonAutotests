import requests

""""HTTP methods list"""


class HttpMethod:

    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
        return result
