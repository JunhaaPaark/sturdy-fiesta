#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()  # manage.py 스크립트 파일이 모듈로 사용될 때는 main()의 실행을 금지.


'''
어떤 스크립트 파일이든 파이썬 인터프리터가 최초로 실행한 스크립트 파일의 __name__에는
'__main__'이 들어갑니다. 이는 프로그램의 시작점(entry point)이라는 뜻입니다.
__name__ 변수를 통해 현재 스크립트 파일이 시작점인지 모듈인지 판단합니다.

if __name__ == '__main__':처럼 __name__ 변수의 값이 '__main__'인지 확인하는 코드는
현재 스크립트 파일이 프로그램의 시작점이 맞는지 판단하는 작업입니다.
즉, 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위한 용도입니다.
'''


