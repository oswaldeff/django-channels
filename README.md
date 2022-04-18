# django-channels
-----------------

## [project tree]
장고 채널을 이용한 채팅서버 프로젝트 구조는 아래와 같습니다.  작업 파일들은 아래와 같습니다.

- config app
  - ./config/asgi
  - ./config/routing
  - ./config/settings
  - ./config/urls
- chat app
  - ./chat/consumers
  - ./chat/routing
  - ./chat/templates
  - ./chat/urls
  - ./chat/views
```
.
├── README.md
├── chat
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── consumers.py
│   ├── models.py
│   ├── routing.py
│   ├── templates
│   │   ├── chatroom.html
│   │   ├── index.html
│   │   └── layout.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── routing.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env
├── manage.py
└── requirements.txt
```

## [env]
virtualenv를 사용하여 아래와 같은 버전으로 작업하였습니다.  localhost와 redis-server를 통하여 로컬환경에서 작업 및 테스트하였습니다.

- python 3.8
- django 3.2
- channels 3.0
- localhost

## [install]
프로젝트에 필요한 서드파티들은 ./requirements.txt 파일을 통해 설치할 수 있습니다.

## [runserver]
프로젝트는 redis-server구동 이후  ./manage.py를 통해 runserver합니다.
```
Django version 3.2, using settings 'config.settings'
Starting ASGI/Channels version 3.0.4 development server at http://127.0.0.1:8000/
```

## [urls]
- channel
http://127.0.0.1:8000/chat/
