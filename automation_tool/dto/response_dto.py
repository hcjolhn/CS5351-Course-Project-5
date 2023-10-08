import datetime
from dataclasses import dataclass
from typing import Optional

from seleniumwire.request import Request
from seleniumwire.utils import decode as sw_decode

@dataclass
class NetworkTraffic:
    req_url: str
    req_path_params: str
    req_query_params: dict
    req_body: Optional[list]
    res_status: str
    res_body: str
    req_time: datetime
    res_time: datetime

    def __init__(self, res: Request) -> None:
        self.req_url = res.url
        self.req_path_params = res.params
        if 'application/json' == res.response.headers.get_content_type():
            print(res.url)
            print('res.body')
            body = sw_decode(res.response.body, res.response.headers.get('Content-Encoding', 'identity')).decode(
                "utf8")
            body_json = eval(body)
            print(body_json)



