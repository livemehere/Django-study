# Django-study

## MTV 패턴 (MVC패턴)

- Model (ORM 제공)
- View
- Template

## Admin 기능제공

- 상당히 편한거같다

## 시작

### 가상환경설치 & 실행

```bash
python -m venv myvenv
```

```bash
source myvenv/bin/activate
```

```bash
deactivate
```

> 가상환경은 이 프로젝트만을 위한 패키지를 외부 패키지들과 충돌하지 않고 독립적으로 관라히기 위해서 사용한다

### Django 설치

가상환경 실행한 상태에서

```bash
pip install django
```

### 프로젝트 생성

```bash
django-admin startproject myproject
```

### Django 서버 작동

```bash
python manage.py runserver
```

### Hello world (App 만들기)

```bash
python manage.py startapp helloworld
```

1. settings.py ⇒ project에게 app의 존재 알리기
2. templates ⇒ views.py에서 처리된 데이터를 받아 사용자에게 화면을 보여줌
3. views.py ⇒ 데이터를 처리하는 함수 작성
4. urls.py ⇒ 요청에 맞는 함수를 views.py에서 찾아 요청 전달

### Hello world 띄우기

#### settings.py 에 앱추가

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'helloworld.apps.HelloworldConfig', # 여기
]
```

#### templates 폴더만들고 html 파일 만들고 helloworld 적고 저장

#### views.py 에 로직함수 생성

```python
def helloworld(request):
    return render(request,'helloworld.html')
```

#### urls.py에 views 연결

```python
from django.contrib import admin
from django.urls import path
import helloworld.views # 불러오기

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', helloworld.views.helloworld,name='home'), # 경로,함수,대명사로 쓸 이름
]

```

### Word Counter 만들기

준비중..
