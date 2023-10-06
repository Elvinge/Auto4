import logging
import requests
import yaml


with open('testdata.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

S = requests.Session()


def test_post_create(user_login):
    res = S.post(url=data['address_post'], headers={'X-Auth-Token': user_login},
           data={'title': data['title'], 'description': data['description'], 'content': data['content']})
    logging.debug(f"Response is {str(res)}")
    assert str(res) == '<Response [200]>', 'post_create FAIL'
