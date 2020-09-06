"""定义learning_logs的URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 显示所有主题
    url(r'^topics/$', views.topics, name='topics'),
    # 特定主题的详细内容
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 用于添加新主题
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 用于编辑主题
    url(r'^edit_topic/(?P<topic_id>\d+)$', views.edit_topic, name='edit_topic'),
    # 用于删除主题
    url(r'^delete_topic/(?P<topic_id>\d+)$', views.delete_topic, name='delete_topic'),
    # 用于添加新条目
    url(r'^new_entry/(?P<topic_id>\d+)$', views.new_entry, name='new_entry'),
    # 用于编辑已有条目
    url(r'^edit_entry/(?P<entry_id>\d+)$', views.edit_entry, name='edit_entry'),
    # 用于删除已有条目
    url(r'^delete_entry/(?P<entry_id>\d+)$', views.delete_entry, name='delete_entry'),

]
