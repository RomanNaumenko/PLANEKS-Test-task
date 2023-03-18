from .models import Scheme
from .forms import SchemeForm
from django.views.generic import *
from django.shortcuts import *
import datetime
from .dummy_data_generator import csv_data_generator
import csv
from django.conf import settings


# Create your views here.
def scheme_listing(request):
    user = request.user
    query = Scheme.objects.filter(author=user.id)
    cntx = {"content": query}
    return render(request, "scheme_list.html", cntx)


def media_download(request, id):
    results = []
    query = Scheme.objects.get(id=id)
    file = query.upload.name
    file_path = str(settings.BASE_DIR) + f'/{file}'
    with open(file_path, 'r', encoding='UTF-8') as read_file:
        reader = csv.reader(read_file, delimiter=',', quotechar=',')
        for row in reader:
            results.append(row)

    file_path = settings.MEDIA_ROOT
    with open(f'{file_path}/{file}', 'a', encoding='UTF-8') as write_file:
        writer = csv.writer(write_file)
        writer.writerows(results)

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
    columns_content = [scheme.type_1, scheme.type_2, scheme.type_3, scheme.type_4, scheme.type_5,
                       scheme.type_6, scheme.type_7, scheme.type_8, scheme.type_9, scheme.type_10]  # Get columns

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

    # Replace ids with names
    def replace(list, dictionary):
        for idx, val in enumerate(list):
            list[idx] = dictionary[list[idx]]
        return list

    replace(columns_content, columns_names)
    while 'Choose...' in columns_content:
        columns_content.remove('Choose...')

    names = [scheme.name_1, scheme.name_2, scheme.name_3, scheme.name_4, scheme.name_5,
             scheme.name_6, scheme.name_7, scheme.name_8, scheme.name_9, scheme.name_10]

    while '' in names:
        names.remove('')

    while 'None' in names:
        names.remove('None')

    order = [scheme.order_1, scheme.order_2, scheme.order_3, scheme.order_4, scheme.order_5,
             scheme.order_6, scheme.order_7, scheme.order_8, scheme.order_9, scheme.order_10]

    while 0 in order:
        order.remove(0)

    if order:
        columns_content = [x for _, x in sorted(zip(order, columns_content))]
        names = [x for _, x in sorted(zip(order, names))]

    filename = str(scheme.author) + '__' + str(scheme.name) + '__' + str(
        datetime.datetime.today().strftime('%Y-%m-%d__%H-%M-%S')) + '.csv'

    csv_data_generator(rows, columns_content, names, filename, scheme_id, request)
    print(filename)

    user = request.user
    query = Scheme.objects.filter(author=user.id)
    cntx = {"content": query}
    return render(request, "scheme_list.html", cntx)
