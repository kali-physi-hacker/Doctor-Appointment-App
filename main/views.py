from django.shortcuts import render


def home_page(request):
    """
    Returns the homepage of the web application
    :param request:
    :return:
    """
    template = "home/index.html"
    context = {}
    return render(request, template, context)