import os.path

import pytest

from emrichen import Template


BASE_DIR = os.path.realpath(os.path.dirname(__file__))


def test_multiple_include_defaults():
    filename = os.path.join(BASE_DIR, 'test_include_defaults.in.yml')
    template = Template.parse(
        '''
        ab:
            !MultiInclude includes/multi-include-*.in.yml
        ''', filename=filename)
    enrich = template.enrich({})
    assert enrich == [{'ab': [{'a': 1,'aa': 11,'aaa': 111}, {'b': 2,'bb': 22,'bbb': 222}, {'d': 4,'dd': 44,'ddd': 444}, {'e': 5,'ee': 55,'eee': 555}]}]
