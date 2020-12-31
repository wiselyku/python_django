from django.urls import path
from hello import views
from hello.models import LogMessage, ToDoList

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

to_do_list_view = views.ToDoListView.as_view(
    queryset=ToDoList.objects.order_by("createdDatetime")[:20],
    context_object_name="to_do_list",
    template_name="hello/to_do_list.html",    
)


urlpatterns = [
    path("", home_list_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),    
    path("log/", views.log_message, name="log"),
    path("todo/", to_do_list_view, name="to_do_list"),
    path("todolist_add/", views.to_do_list, name="to_do_list_add"),
    path("todolist_edit/<id>", views.to_do_list_edit, name="to_do_list_edit"),
    path("todolist_edit_ok/<id>", views.to_do_list_edit_ok, name="to_do_list_edit_ok"),
]