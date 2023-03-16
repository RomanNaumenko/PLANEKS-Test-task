from django.shortcuts import render, redirect
from .models import Scheme
from .forms import SchemeForm


# Create your views here.
def scheme_list(request):
    user = request.user
    query = Scheme.objects.filter(author=user.id)
    # print(query)
    cntx = {"content": query}
    return render(request, "scheme_list.html", cntx)


def scheme_create(request):
    user = request.user
    user = user.id
    if request.method == 'POST':
        form = SchemeForm(request.POST, initial={'author': user})
        if form.is_valid():
            form.save()
            return redirect('/list')

    return render(request, 'scheme_form.html', {'form': SchemeForm(initial={'author': user}), })
