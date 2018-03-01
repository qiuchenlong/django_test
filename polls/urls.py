


from django.conf.urls import url, include
from polls import views


extra_patterns = [
    url(r'^reports/(?P<year>[0-9]+)/$', views.testx, name="testx"),
    url(r'^charge/$', views.test, name="charge-test"),
]

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^upup$', views.upload_file, name="uploadfile"),
    url(r'^upup/[0-9]{4}$', views.index, name="index"),  # 只是作为路径
    url(r'^upup/([0-9]{4})$', views.index, name="index"), # 当作参数传入

    url(r'^upups/$', views.test, name="upups-test"),  # 捕获的值作为关键字参数而不是位置参数传递给视图函数
    url(r'^upups/(?P<year>[0-9]{4})$', views.test, name="upups--test"), #捕获的值作为关键字参数而不是位置参数传递给视图函数

    url(r'^credit/', include(extra_patterns)),
]




