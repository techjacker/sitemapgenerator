# import pytest


# @pytest.fixture
# def url():
#     return 'url'

import pytest

from pytest_httpbin.plugin import httpbin_ca_bundle


pytest.fixture(autouse=True)(httpbin_ca_bundle)
