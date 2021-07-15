token = ''
import requests

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
            'owner_id':454381118,
            'photo_sizes':1,
            'extended':1
        }
        res = requests.get(photos_url, params={**self.params, **photos_params})
        return res.json()


TOKEN = " "

class YaUploader:
    def __init__(self, token: str):
        self.token = token

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
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")




vk_client = VkUser(token, '5.126')
print(vk_client.owner_id)
sizes_photo = vk_client.get_photos()['response']['items'][0]['sizes'][-1]['type']
upload_url = vk_client.get_photos()['response']['items'][0]['sizes'][-1]['url']
name_photo = vk_client.get_photos()['response']['items'][0]['likes']['count']

print(sizes_photo)


if __name__ == '__main__':
    uploader = YaUploader(token=TOKEN)
    result = uploader.upload_file("netology/photo", f"{name_photo}")