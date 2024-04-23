# todo/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),
]

# todolist/urls.py (urls.py 파일을 todolist 폴더안에 생성해줘야 함)


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	# path('', )
]