import requests
def cenzura1(text):

    data = {
        'api_version': 'v1',
        'main_token': '1zZMy6zMIVRl',
        'query_details': {
            'source_token': '661_ebdd49053794023f535b2a276e4b604e',
            'text': text,
            'dictionaries': {
                'rus': ['heavy', 'terrorism','sex','weapon','expletive'],
                'eng': ['heavy']
            },
            'deep_check': 'yes'
        }
    }
    response = requests.post('https://lf.statusnick.com/api/text/check', json=data)
    print(response)

    if response.status_code == 200:
        result = response.json()
        # print(result)
        if result['result']['final']['check']['check_result'] == []:
            return True
        else:
            return False
    else:
        print('Произошла ошибка при отправке запроса.')

# print(cenzura(''))