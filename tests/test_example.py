#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `example` package."""

import pytest

from click.testing import CliRunner

#from example import example


from example import *

class TestExample(unittest.TestCase):
#@pytest.fixture
    def response(test):
        """Sample pytest fixture.
        
        See more at: http://doc.pytest.org/en/latest/fixture.html
        """
        # import requests
        # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

        
    def test_content(test):
        """Sample pytest test function with the pytest fixture as an argument."""
        # from bs4 import BeautifulSoup
        # assert 'GitHub' in BeautifulSoup(response.content).title.string
        
        

    def test_create_graph(self):
        assert create_graph(np.ones(10),np.ones(10),'hehe')=='hehe.png'
        assert len(arr1)==len(arr2)
        assert answer=='yusuf.png'
