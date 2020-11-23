# SejongLocker

1. 'VirtualEnvironment\Scripts\activate'를 실행하여 가상환경 실행
2. 'python manage.py flush' 명령어를 실행하여 데이터배이스를 청소
3. 'python manage.py createsuperuser' 명령어를 실행하여 최고권한자 생성
4. 아래 명령어들을 실행
<br/> python manage.py makemigrations
<br/> python manage.py migrate
<br/> python manage.py loaddata locker\fixtures\defaultLockersA.json
<br/> python manage.py loaddata locker\fixtures\defaultLockersB.json
<br/> python manage.py loaddata locker\fixtures\defaultLockersC.json
<br/> python manage.py loaddata locker\fixtures\defaultLockersD.json
<br/> python manage.py loaddata locker\fixtures\defaultLockersE.json

5. 'python manage.py runserver' 명령어를 실행하여 서버를 시작
6. 인터넷 브라우저를 통해 '127.0.0.1:8000' 접근

* manage.py 파일은 SejongLocker 파일 안에 있음
* locker\fixitures 폴더 안에 있는 .json 파일들을 수정하여 초기 데이터배이스 정보들을 수정할 수 있음
