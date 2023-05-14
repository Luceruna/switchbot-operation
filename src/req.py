import requests
import json
import signer

base_url = 'https://api.switch-bot.com'


def get_device_list():
    req_url = f'{base_url}/v1.1/devices'
    try:
        res = requests.get(req_url, headers=signer.create_sign())
        res.raise_for_status()

        deviceList = res.json()
        with open('../private/deviceList.json', 'w', encoding='utf8') as f:
            json.dump(deviceList, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print('request error: ', e)


if __name__ == '__main__':
    get_device_list()
