import requests


# функция которая проверяет фото на запрещенку
def analyze_image(image_path):
    url = 'https://api.imagga.com/v2/tags'
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    response = requests.post(
        url,
        auth=('acc_59ab7007b0399be', '914260aa0d54ebc7fdb60bd17db88ac1'),
        files={'image': image_data}
    )
    categories = response.json()['result']['tags'][0]['confidence']
    if int(categories) > 68:
        print('запрещенка')
        return 'запрещенка'
    else:
        print('все прошло')
        return 'все прошло'

#analyze_image('users_photo/forbidde.jpg') #фото запрещенки
#analyze_image('users_photo/norm.jpg') #фото не запрещенки
# analyze_image('users_photo/oru.jpg') #фото запрещенки


