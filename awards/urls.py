from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView,  LogoutView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns=[
    
    url(r'^$', views.index, name='homepage'),
    url('accounts/profile/$', views.myProfile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^details/(\d+)$', views.details, name='details'),
    url(r'^api/profile/$', views.Profile_list.as_view()),
    url(r'^api/projects/$', views.Project_list.as_view()),
    url(r'^profile/$',views.profile_edit,name='edit_profile'),
    # url('project/review/<project_id>',views.project_review,name='project_review'),
    url('accounts/login/',LoginView.as_view(redirect_authenticated_user=True,template_name='accounts/login.html'),name='login'),
    url('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    url('accounts/register/',views.register, name='register'),
   


]
