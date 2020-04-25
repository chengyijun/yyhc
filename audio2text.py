import json
import os
import pickle
import time

import requests


class Audio2Text:
    API_KEY = 'ICwzDk4upDquwaBUUq8OWWGs'  # 替换成你的api_key 在创建的应用中查找
    SECRET_KEY = '2os45zZiEAPUt4u0hX7Ytyy5KlbbAKey'  # 替换成你的secret_key 在创建的应用中查找
    APP_ID = '19591144'  # 替换成你的app_id

    def __init__(self):
        self.access_token = None
        self.expires_in = 2592000
        self.get_token()

    def query_task(self):
        url = 'https://aip.baidubce.com/rpc/2.0/aasr/v1/query'
        data = {'task_ids': ['5ea3c92c654d513416c0f8aa']}
        params = {'access_token': self.access_token}
        headers = {'content-type': "application/json"}
        res = requests.post(url=url,
                            data=json.dumps(data),
                            params=params,
                            headers=headers)
        print(res.json())

    def create_task(self):
        url = 'https://aip.baidubce.com/rpc/2.0/aasr/v1/create'
        params = {'access_token': self.access_token}
        data = {
            "speech_url":
            "http://speech-doc.gz.bcebos.com/rest-api-asr/public_audio/16k.pcm",
            "format": "pcm",
            "pid": 1537,
            "rate": 16000
        }
        headers = {'content-type': "application/json"}
        res = requests.post(url=url,
                            data=json.dumps(data),
                            params=params,
                            headers=headers)
        print(res.json())

    @staticmethod
    def get_token_from_file():
        with open('./token', 'rb') as f:
            data = pickle.load(f)
        return data.get('access_token'), data.get('request_time')

    def get_token(self):
        if self.is_vaild_token():
            self.access_token, _ = self.get_token_from_file()
        else:
            self.get_token_from_api()

    def is_vaild_token(self):
        if not os.path.exists('./token'):
            return False
        self.access_token, request_time = self.get_token_from_file()
        if int(time.time()) - request_time < self.expires_in:
            return True
        else:
            return False

    def get_token_from_api(self):
        """
        :return: 
        """
        # 判断token是否过期
        # 存储的token文件信息内容
        # {'access_token': '****', 'request_time': 1587805086}
        url = 'https://openapi.baidu.com/oauth/2.0/token'
        params = {
            'grant_type': 'client_credentials',
            'client_id': self.API_KEY,
            'client_secret': self.SECRET_KEY
        }
        res = requests.post(url=url, params=params)
        print(res.json())
        if res.status_code == 200:
            self.access_token = res.json().get('access_token')
            self.expires_in = res.json().get('expires_in')
            request_time = int(time.time())
            data = {
                'access_token': self.access_token,
                'request_time': request_time
            }
            with open('./token', 'wb') as f:
                pickle.dump(data, f)
        else:
            raise Exception('access_token 获取失败')


def main():
    audio2text = Audio2Text()
    # audio2text.create_task()
    audio2text.query_task()


if __name__ == '__main__':
    main()
