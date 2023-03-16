from django.shortcuts import render, redirect
from .models import Scheme
from .forms import SchemeForm
from django.views.generic import UpdateView
from django.views.generic import *
from django.shortcuts import *


# Create your views here.
def scheme_listing(request):
    user = request.user
    query = Scheme.objects.filter(author=user.id)
    # print(query)
    cntx = {"content": query}
    return render(request, "scheme_list.html", cntx)


def scheme_creation(request):
    user = request.user
    user = user.id
    if request.method == 'POST':
        form = SchemeForm(request.POST, initial={'author': user})
        if form.is_valid():
            form.save()
            return redirect('/list')

    return render(request, 'scheme_form.html', {'form': SchemeForm(initial={'author': user})})


class scheme_editing(UpdateView):
    template_name = "scheme_edit.html"
    form_class = SchemeForm
    success_url = '/list'

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Scheme, id=_id)


class scheme_deleting(DeleteView):
    template_name = "scheme_delete.html"
    success_url = '/list'

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Scheme, id=_id)

    def get_success_url(self):
        return "/list"

