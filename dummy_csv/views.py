from django.shortcuts import render, redirect
from .models import Scheme
from .forms import SchemeForm
from django.views.generic import UpdateView, DeleteView
from django.views.generic import *
from django.shortcuts import *
import datetime
from .dummy_data_generator import csv_data_generator
import os
import csv
from django.conf import settings
from django.http import HttpResponse, Http404


# Create your views here.
def scheme_listing(request):
    user = request.user
    query = Scheme.objects.filter(author=user.id)
    # print(query)
    cntx = {"content": query}
    return render(request, "scheme_list.html", cntx)


def media_download(request, id):

    query = Scheme.objects.get(id=id)
    file = query.upload
    file_path = settings.MEDIA_ROOT
    with open(f"{file_path}\\{file}", "w") as f:
        csv.writer(f)

    user = request.user
    query = Scheme.objects.filter(author=user.id)
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


def csv_generator_setting(request, id):
    # Get scheme
    scheme = Scheme.objects.get(id=id)
    scheme_id = int(scheme.id)
    print(scheme)
    print(scheme.id)
    print(int(scheme.id))

    # COLUMNS
    # Get columns
    columns_content = [scheme.type_1, scheme.type_2, scheme.type_3, scheme.type_4, scheme.type_5,
                       scheme.type_6, scheme.type_7, scheme.type_8, scheme.type_9, scheme.type_10]

    # Replace IDs with names
    columns_names = {'1': 'Choose from...',
                     '2': 'Full name',
                     '3': 'Job',
                     '4': 'Email',
                     '5': 'Domain Name',
                     '6': 'Phone number',
                     '7': 'Company name',
                     '8': 'Text',
                     '9': 'Integer',
                     '10': 'Address',
                     '11': 'Date'}

    def replace(list, dictionary):
        for idx, val in enumerate(list):
            list[idx] = dictionary[list[idx]]
        return list

    replace(columns_content, columns_names)
    while 'Choose...' in columns_content:
        columns_content.remove('Choose...')

    print('Columns: ')
    print(columns_content)

    # NAMES
    # Get names
    names = [scheme.name_1, scheme.name_2, scheme.name_3, scheme.name_4, scheme.name_5,
             scheme.name_6, scheme.name_7, scheme.name_8, scheme.name_9, scheme.name_10]

    while '' in names:
        names.remove('')

    while 'None' in names:
        names.remove('None')

    print('Names of columns: ')
    print(names)

    # ORDER
    # Get order
    order = [scheme.order_1, scheme.order_2, scheme.order_3, scheme.order_4, scheme.order_5,
             scheme.order_6, scheme.order_7, scheme.order_8, scheme.order_9, scheme.order_10]

    while 0 in order:
        order.remove(0)

    print('Order: ')
    print(order)

    if order:
        columns_content = [x for _, x in sorted(zip(order, columns_content))]
        names = [x for _, x in sorted(zip(order, names))]

    print('Columns in order: ')
    print(columns_content)
    print(names)

    rows = scheme.rows
    print('Number of rows:')
    print(rows)

    filename = str(scheme.author) + ' - ' + str(scheme.name) + ' - ' + str(
        datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'

    csv_data_generator(rows, columns_content, names, filename, scheme_id, request)
    print(filename)

    user = request.user
    query = Scheme.objects.filter(author=user.id)
    # print(query)
    cntx = {"content": query}
    return render(request, "scheme_list.html", cntx)
