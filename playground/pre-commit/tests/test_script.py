#!/bin/env python

import sys
import os

sys.path.append(
    os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../src/")
)

from src import script


def test_call_request():
    assert script.call_request() == "ok"
