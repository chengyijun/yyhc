# -*- coding:utf-8 -*-
from aip import AipSpeech
"""
百度语音合成api接口说明
tex	必填	合成的文本，使用UTF-8编码。小于2048个中文字或者英文数字。（文本在百度服务器内转换为GBK后，长度必须小于4096字节）
tok	必填	开放平台获取到的开发者access_token（见上面的“鉴权认证机制”段落）
cuid	必填	用户唯一标识，用来计算UV值。建议填写能区分用户的机器 MAC 地址或 IMEI 码，长度为60字符以内
ctp	必填	客户端类型选择，web端填写固定值1
lan	必填	固定值zh。语言选择,目前只有中英文混合模式，填写固定值zh
spd	选填	语速，取值0-15，默认为5中语速
pit	选填	音调，取值0-15，默认为5中语调
vol	选填	音量，取值0-15，默认为5中音量
per	选填	发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
aue	选填	3为mp3格式(默认)； 4为pcm-16k；5为pcm-8k；6为wav（内容同pcm-16k）; 注意aue=4或者6是语音识别要求的格式，但是音频内容不是语音识别要求的自然人发音，所以识别效果会受影
"""


def get_audio(text=None, vol=5, pit=5, spd=5, per=0, aue=6):
    if text is None:
        return
    API_KEY = 'eIkgWzO0QvEtBGaGZkFoGg2T'  # 替换成你的api_key 在创建的应用中查找
    SECRET_KEY = 'uSrZtjiqTttk8LhTDPXkMx7b2IGjNM95'  # 替换成你的secret_key 在创建的应用中查找
    APP_ID = '19169841'  # 替换成你的app_id
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(text, 'zh', 1, {
        'vol': vol,
        'pit': pit,
        'spd': spd,
        'per': per,
        'aue': aue
    })
    file_name = text[:10]
    if not isinstance(result, dict):
        if aue == 3:
            with open(f'{file_name}.mp3', 'wb') as f:
                f.write(result)
        elif aue == 6:
            with open(f'{file_name}.wav', 'wb') as f:
                f.write(result)
        else:
            raise Exception('参数错误')
