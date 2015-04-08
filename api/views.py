from django.contrib.auth.hashers import check_password,make_password

def index(res):
    print(make_password('123456'))
    return None;