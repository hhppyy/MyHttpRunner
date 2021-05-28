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
    上传图片函数，获取图片file-like-objects
    :param filepath: 路径
    :return: file-like-objects
    """
    # with open(filepath, 'rb') as f:
    #     return f

    return open(filepath, 'rb')


def username_params():
    """
    参数化username
    :return: user_list
    """
    user_list = [
        {'p_username':'admin'},
        {'p_username': 'test'},
        {'p_username': '123123'}
    ]
    return user_list

def password_params():
    """
    参数化password
    :return: user_list
    """
    pwd_list = [
        {'p_password':'admin'},
        {'p_password': 'test'},
        {'p_password': '123456'}
    ]
    return pwd_list

def get_params():
    """
    参数化username、password
    :return: params_list
    """
    params_list = [
        {'p_username': 'admin','p_password':'111111'},
        {'p_username': 'test','p_password':'123456'},
        {'p_username': '123123','p_password':'111111'}
    ]
    return params_list

if __name__ == '__main__':
    a = r'E:\MyHttpRunner\data\kenan.jpg'
    v = get_file(a)
    print(v)
