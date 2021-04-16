
import time

def sleep(n_secs):
    time.sleep(n_secs)


def setup_hooks(method,url,**kwargs):
    """
    - method: 请求方法，e.g. GET, POST, PUT
    - url: 请求 URL
    - kwargs: request 的参数字典
    :return:
    """
    pass

def teardown_hooks(resp_obj):
    """
    - resp_obj: requests.Response 实例
    :return:
    """
    pass