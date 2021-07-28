token = ''
Token = ''
import requests
import json

class VkUser:
    url = 'http://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }
        self.owner_id = requests.get(self.url+'users.get', self.params).json()

    def get_photos(self, user_id=None):

        photos_url = self.url + 'photos.get'
        photos_params = {
            'album_id':'profile',
            'count':1000,
            'owner_id':552934290,
            'photo_sizes':1,
            'extended':1
        }
        res = requests.get(photos_url, params={**self.params, **photos_params})
        return res.json()


TOKEN = ''

class YaUploader:
    def __init__(self, token: str):
        self.token = Token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()


    def upload_file(self, disk_file_path, filename):
        print(self._get_upload_link(disk_file_path=disk_file_path))
        href = self._get_upload_link(disk_file_path=disk_file_path + filename).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()

        if response.status_code == 201:
            print("Success")




vk_client = VkUser(token, '5.126')







dict = {}
photos = []
photos_name = []
if __name__ == '__main__':
    uploader = YaUploader(token=TOKEN)
    for i in range(0, 5):

        upload_url = vk_client.get_photos()['response']['items'][i]['sizes'][-1]['url']
        name_photo = vk_client.get_photos()['response']['items'][i]['likes']['count']
        sizes_photo = vk_client.get_photos()['response']['items'][i]['sizes'][-1]['type']
        date = vk_client.get_photos()['response']['items'][i]['date']
        dict['size'] = sizes_photo
        response = requests.get(upload_url)

        if name_photo in photos_name:
            with open(f'{name_photo}{date}.jpg', 'wb') as f:
                f.write(response.content)
            dict['file_name'] = name_photo + date
            result = uploader.upload_file("", f"{name_photo}+{date}.jpg")
            photos.append(dict)
            photos_name.append(name_photo+date)

        else:
            with open(f'{name_photo}.jpg', 'wb') as f:
                f.write(response.content)
            dict['file_name'] = name_photo
            result = uploader.upload_file('', f"{name_photo}.jpg")
            photos.append(dict)
            photos_name.append(name_photo)




json = json.dumps(photos)


