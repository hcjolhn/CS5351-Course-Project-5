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
        if dest_url in res.url:
            return NetworkTraffic(res)

    driver.quit()
    return None
