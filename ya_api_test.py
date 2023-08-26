import requests

token = "y0_AgAAAAAZXUOIAADLWwAAAADkYcIcFk1UCK-CS0WRr8DMyjMu4obVZ1I"

class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    def create_folder(self, folder_name):
        """ Creates a folder for the upload to Ya Disk"""

        headers = {

            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)

        }
        folder_url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": folder_name}
        response = requests.put(folder_url, headers=headers, params=params)
        return response.status_code


    def check_folder(self, folder_name):

        headers = {

            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)

        }
        folder_url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": folder_name}
        response = requests.get(folder_url, headers=headers, params=params)
        return response.status_code


def test_success(folder_name):
    myuploader = YaUploader(token)
    assert myuploader.create_folder(folder_name) == 201, " folder not created"


def test_folder_exists(folder_name):

    myuploader = YaUploader(token)
    assert myuploader.check_folder(folder_name) == 200, " folder does not exist"
    

if __name__ == "__main__":
    test_folder_exists("new_folder3")
    test_success("new_folder3")
    