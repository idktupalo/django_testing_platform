from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'cms_templates/main_page.html')


def prepare_page(request):
    return render(request, 'cms_templates/prepare_page.html')


def test_page(request):
    return render(request, 'cms_templates/test_page.html')


def done_page(request):
    return render(request, 'cms_templates/done_test.html')
