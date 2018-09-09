from django.conf.urls import url
from django_pdfkit import PDFView
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^details/(?P<id>\d+)', views.detail, name="details"),
    url(r'^delete/(?P<id>\d+)', views.delete, name="delete"),
    url(r'^add/$', views.add, name="add"),
    # url(r'^report/$', views.report_pdf, name="report_pdf"),
    # url(r'^pdf/$', views.pdf, name="pdf"),
    # url(r'^pdf/$', PDFView.as_view(template_name='report.html'), name='my-pdf'),
    url(r'^pdf/$', views.pdf_view, name='pdf_view'),
    url(r'upload-file/$', views.upload, name="UploadFileForm"),
    url(r'download-file/$', views.download, name="UploadFileForm")
]
