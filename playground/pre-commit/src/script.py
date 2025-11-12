#!/bin/env python

import requests


def call_request() -> None:
    url: str = "https://example.com"
    req = requests.get(url)
    if req.status_code == 200:
        return "ok"
    return "ng"


if __name__ == "__main__":
    print(call_request())
