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

## Word Counter 만들기

> 프로젝트생성 ➔ app생성 ➔ app등록 ➔ template만들기 ➔ view작성 ➔ url연결

### href 링크

```python
    <a href="{% url 'wordcount' %}">Word count로 이동</a> #템플릿 언어로 작성해주어야 우리가 사용했던 name= 을 사용할 수 있음
```

#### 입력 form 예시

```python
    <a href="{% url 'home' %}">Hello world로 이동</a>
    <form action="{% url 'result' %}" >
        <textarea name="fulltext" id="" cols="30" rows="10"></textarea>
        <br>
        <input type="submit" value="Count">
    </form>
```

#### 결과값 받아서 출력 예시

- `dic` 자료형을 for문에서 사용하기위해서 `iterable` 한 `list`로 반환해주는 `item()` 을 사용하였다
- 나는 for문을 돌때마다 items를 적용해주었는데, views.py 에서 애초에 items()를 적용해서 넘겨줘도된다

```python
<body>
    <h1>입력하신 글은 <span style="color:red">{{ wordlength }}</span> 개의 단어로 이루어져있습니다!</h1>
    <hr>
    <h1>단어별 사용횟수</h1>
    {% for word,count in word_dic.items %}
    {{ word }} : {{ count }}번
    <br>
    {% endfor %}
</body>
```

#### views.py 로직

- `dic` 자료형에서 `key` 값이 있는지 없는지를 확인하기 위해서 `in` 연산자를 사용한다

```python
def result(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()
    word_dic = {}
    for word in wordlist:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    print(word_dic.items())
    return render(
        request, "result.html", {"wordlength": len(wordlist), "word_dic": word_dic}
    )
```

## Blog를 활용한 DB사용하기 (model)

### 한국시간으로 바꾸기

- settings.py

```python
LANGUAGE_CODE = 'ko-kr' #해도되고 안해도되고
TIME_ZONE = "Asia/Seoul"
```

### Django의 시간처리 패키지

```python
from datetime import datetime
from django.utils import timezone
```

#### datetime 패키지

```python
from datetime import datetime

datetime.now()
# 결과: datetime.datetime(2020, 10, 28, 0, 33, 21, 553440)
```

#### imezone 패키지

```python
from django.utils import timezone

timezone.now()
# 결과: datetime.datetime(2020, 10, 27, 15, 34, 16, 677327, tzinfo=<UTC>)

timezone.localtime()
# 결과: datetime.datetime(2020, 10, 28, 0, 34, 23, 350281, tzinfo=<DstTzInfo 'Asia/Seoul' KST+9:00:00 STD>)
```

### auto_now_add, auto_now

- 보통 모델에서 생성, 수정 시간을 기록하기 위해 아래와 같이 `auto_now_add와` `auto_now를` 사용한다. 이렇게 하면 해당 컬럼이 생성, 수정되었을 때 시간이 자동으로 기록된다.

```python
models.DateTimeField(auto_now_add=True)
models.DateTimeField(auto_now=True)
```

### model 의 id

- detail 페이지를 만들기위해서는 해당 글의 `id`값을 가져와서 불러와야된다.
- django model에서는 특별이 `pk`나 `id` 를 지정해주지않으면 자동으로 `.id`로 포함된다

```python
id = models.AutoField(primary_key=True, **옵션 )
```

### template 언어로 pram 넘기기

#### html

```html
<body>
  <h1>Blog HOME</h1>
  {% for post in posts %}
  <div>
    <h2><a href="{% url 'blogdetail' post.id %}"> {{post.title}}</a></h2>
    <h5>{{post.body}}</h5>
    작성일 : {{post.write_date}}
    <br />
    수정일 : {{post.modify_date}}
    <hr />
  </div>
  {% endfor %}
</body>
```

#### urls.py

```python
    path("blogdetail/<int:blog_id>", blogApp.views.blogdetail, name="blogdetail"),
```

#### views.py

```python
def blogdetail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    print(post)
    return render(request, "blogdetail.html", {"post": post})

```

### new post 작성하기

#### form문은 반드시 csrf보안을 설정해줘야한다 `csrf_token`

```python
    <form action="{% url 'createnew' %}" method="POST">
        {% csrf_token %}
        <h2>제목</h2>
        <input type="text" name="title" required><br>
        <h2>내용</h2>
        <textarea name="body" id="" cols="30" rows="10" required></textarea><br>
        <input type="submit" value="작성하기">
    </form>
```

#### redirect 사용과 str() 사용

```python
return redirect("/blogdetail/" + str(post.id))

```

#### model 생성

```python
def createnew(request):
    if request.method == "POST":
        post = Blog() # 객체생성 왜 new 연산자를 안쓰는가 ?? 클래슨데!!
        post.title = request.POST["title"]
        post.body = request.POST["body"]
        post.write_date = timezone.localtime()
        post.modify_date = timezone.localtime()
        post.save() # 저장

        return redirect("/blogdetail/" + str(post.id))


```

## static file

### 단순히 앱 단위로 사용할 경우

- app 폴더에서 static 폴더를 만들어서 넣는다. 끝
- html에서 아래와 같이 불러와주고, 사용하면 끝

```html
{% load static %}
<img src="{% static 'spiderman.jpeg' %}" alt="" />
<img src="{% static 'iron.jpg' %}" alt="" />
```

> 원래는 STATICFILES_DIRS, STATIC_ROOT 도 설정을 했었는데, 도데체 settings.py에서 등록하는 것들이 어떻게 동작하는지 궁금해서 이것저것 실험을 해보니 결론은 STATIC_URL = "/static/" 기본적으로 적혀있는 이문장하나가 app내에서든 project단에서든 존재하는 static 파일을 읽을수 있도록 해주는것 같다. 그래서 별도의 설정없이 static 파일만만들어서 정적파일을 관리하면 앱과 앱사이에서의 static파일도 로드가 가능하다. 하지만 배포하기에는 한곳에 모아야 되기때문에 적합하지 않다는 생각이든다. 그래서 정적파일을 한데 모아주는 명령어를 사용하던지, 에초에 project단에서 static 파일들을 모아서 관리하든지 하면된다. 만약 앱단에서 각각 static 파일을 관리하고있다면 아래의 설정과 명령어를 사용하면된다

> STATIC_URL = "/static/" 은 "/photo1.png" 를 "/media/photo1.png" 게 생략할수있도록 해준다

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'portfolio', 'static') # 각 앱마다의 static 폴더위치 배열에 등록
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static') # 한곳에 모을 static 폴더 위치지정
```

```bash
python manage.py collectstatic
```

## media file (추후 다시..)

- static vs media : 개발자가 준비한파일 vs 사용자가 업로드하는 파일

```python
# settings.py
MEDIA_URL = "/media/" # 각 media파일에 접근할 때 접두사(prefix)의 역할을 하게 됩니다
MEDIA_ROOT = os.path.join(BASE_DIR, "media") #실제로 파일이 저장되는 경로를 설정하는 값
```

## template extends (상속)

- html을 작성하다보면 nav바와 같은 고정적인 부분들이있는데 이것들을 일일이 작성하게 되면 나중에 유지보수도 어렵고 작성도 어렵다
- 그래서 템플릿엔진에서는 상속을지원한다.
- 아래 3개를 활용하면된다. 활용법은 생략

```
{% extends 'base.html' %}
{% block content %}
{% endblock %}
```

## urls.py 분리

- 앱이 많아질수록 url은 많아지고, 한곳에서 관리한다면 해깔린다.
- 앱마다 urls.py를 만들고, import 구분 수정후 프로젝트 urls.py 는 다음과 같이 수정해준다

### blog 예시 ,blog/로 시작하는 url은 blogApp 앱의 urls.py로 넘긴다!

```python
    path("blog/", include("blogApp.urls")),
```

### blogApp 에 새로 만든 urls.py

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.bloghome, name="bloghome"),
    path("blogdetail/<int:blog_id>", views.blogdetail, name="blogdetail"),
    path("createnew/", views.createnew, name="createnew"),
    path("newpost/", views.newpost, name="newpost"),
]

```

- 이렇게하면 모든 url은 모두 blog로 시작하고 뒤에 추가적으로 붙는다.
