import datetime
from dataclasses import dataclass


from seleniumwire.request import Request
from seleniumwire.utils import decode as sw_decode


@dataclass
class NetworkTraffic:
    req_url: str
    req_path_params: str
    req_query_params: dict
    req_body: list
    res_status: int
    res_body: list
    req_time: datetime
    res_time: datetime

    def __init__(self, req: Request) -> None:
        self.req_url = req.url
        self.req_path_params = req.path
        self.req_query_params = req.params
        self.req_body = eval(req.body.decode('utf-8')) if req.body.decode('utf-8') != '' else []
        self.res_status = req.response.status_code
        self.req_time = req.date
        if 'application/json' == req.response.headers.get_content_type():
            body: str = sw_decode(req.response.body, req.response.headers.get('Content-Encoding', 'identity')).decode(
                "utf8")
            res_body = eval(body)
            self.res_body = res_body
        self.res_time = req.response.date
