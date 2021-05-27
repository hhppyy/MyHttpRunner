import time


def sleep(n_secs):
    time.sleep(n_secs)


def setup_hooks(method, url, **kwargs):
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


def get_file(filepath):
    """
    上传图片函数
    :param filepath: 路径
    :return: file-like-objects
    """
    with open(filepath, 'rb') as f:
        return f

    # return open(filepath, 'rb')


if __name__ == '__main__':
    a = r'E:\MyHttpRunner\data\kenan.jpg'
    v = get_file(a)
    print(v)
