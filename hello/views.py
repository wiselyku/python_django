from django.shortcuts import render

# Create your views here.
import re
from datetime import datetime
from django.http import HttpResponse
# Add these to existing imports at the top of the file:
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from hello.forms import LogMessageForm, ToDoListForm
from hello.models import LogMessage, ToDoList
from django.views.generic import ListView

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


class ToDoListView(ListView):
    model = ToDoList

    def get_context_data(self, **kwargs):
        context = super(ToDoListView, self).get_context_data(**kwargs)
        return context


def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")


def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )



# Add this code elsewhere in the file:
def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})


def to_do_list(request):
    form = ToDoListForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            to_do_data = form.save(commit=False)
            to_do_data.createdDatetime = datetime.now()
            to_do_data.save()
            return redirect("to_do_list")
    else:
        return redirect("todo")
      ##  return render(request, "hello/to_do_list.html", {"form": form})

def to_do_list_edit(request, id):
    context ={}
    context["data"] = ToDoList.objects.get(id = id) 
    return render(request, "hello/to_do_list_edit.html", context) 


def to_do_list_edit_ok(request, id):
    to_do_list_item = get_object_or_404(ToDoList, id=id)
    taskDone = request.POST.get("taskDone")
    if taskDone == 'True':
        to_do_list_item.taskDone = True
        to_do_list_item.finishedDatetime = datetime.now()

    form = ToDoListForm(request.POST or None, instance=to_do_list_item)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("to_do_list")
    else:
        return HttpResponse("something is wrong, inform website administrator")