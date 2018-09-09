from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
import logging
import pdfkit
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django import forms
import django_excel as excel
from django.views.decorators.csrf import csrf_exempt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Start reading database')


# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {"todos": todos}
    return render(request, "index.html", context)


def detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {"todo": todo}
    return render(request, "details.html", context)


@csrf_exempt
def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        todo = Todo(title=title, text=text)
        todo.save()
        return redirect("/todos")
    else:
        return render(request, 'add.html')


@csrf_exempt
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("/todos")


# def report_pdf(request):
#     # Use False instead of output path to save pdf to a variable
#     # http://ourcodeworld.com/articles/read/241/how-to-create-a-pdf-from-html-in-django
#     pdf = pdfkit.from_url('http://ourcodeworld.com', False)
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="ourcodeworld.pdf"'
#     return response
#
#
# def template(request):
#     # Returns some HTML as response
#     # http://ourcodeworld.com/articles/read/241/how-to-create-a-pdf-from-html-in-django
#     return HttpResponse("<h1>Hello World</h1>")
#
#
# def pdf(request):
#     # http://ourcodeworld.com/articles/read/241/how-to-create-a-pdf-from-html-in-django
#     # Create a URL of our project and go to the template route
#     projectUrl = request.get_host() + '/template'
#     pdf = pdfkit.from_url(projectUrl, False)
#     # Generate download
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="ourcodeworld.pdf"'
#
#     return response


def pdf_view(request):
    """Generate pdf."""
    # Model data
    todos = Todo.objects.all().order_by('title')
    context = {"todos": todos}

    # Rendered
    html_string = render_to_string('index.html', context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="AccountListReport.pdf"'
    buffer = BytesIO()
    buffer.getvalue()
    buffer.close()
    response.write(result)
    return response

    # response = HttpResponse(content_type='application/pdf;')
    # response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    # response['Content-Transfer-Encoding'] = 'binary'
    # with tempfile.NamedTemporaryFile(delete=True) as output:
    #     output.write(result)
    #     output.flush()
    #     output = open(output.name, 'r')
    #     response.write(output.read())
    #
    # return response


data = [
    [1, 2, 3],
    [4, 5, 6]
]


class UploadFileForm(forms.Form):
    file = forms.FileField()


# Create your views here.
@csrf_exempt
def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download")
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })


def download(request, file_type):
    sheet = excel.pe.Sheet(data)
    return excel.make_response(sheet, file_type)
