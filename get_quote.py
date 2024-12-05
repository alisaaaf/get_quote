import requests

def get_response(lang):
    url = 'http://api.forismatic.com/api/1.0/'
    params = {
        'method': 'getQuote',
        'format': 'json',
        'lang': lang,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def print_quote(response):
    print(response['quoteText'], '\n', response['quoteAuthor'])

if __name__ == '__main__':
    lang = input("Choose language: enter 'ru' or 'en' ")
    if lang not in ['en', 'ru']:
        print("Invalid input of language")
    response = get_response(lang)
    print_quote(response)