import time
from typing import Optional

from seleniumwire import webdriver
from seleniumwire.utils import decode as sw_decode

from dto.response_dto import NetworkTraffic


def capture_network(dest_url: str) -> Optional[NetworkTraffic]:
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")
    time.sleep(6)

    for res in driver.requests:
        if res.url.__contains__(dest_url):
            return NetworkTraffic(res)
            # if 'application/json' == res.response.headers.get_content_type():
            #     print(res.url)
            #     print('res.body')
            #     body = sw_decode(res.response.body, res.response.headers.get('Content-Encoding', 'identity')).decode(
            #         "utf8")
            #     body_json = eval(body)
            #     print(body_json)
    return None
