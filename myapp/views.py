from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *
import pdfkit

# Create your views here.
def home__page(request):
    context = dict()
    url = request.META.get("HTTP_REFERER")

    if request.method == "POST":
        form = UserProfilForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return HttpResponseRedirect(url)

    else:
        context["form"] = UserProfilForm()

    return render(request,"index.html")


def list__page(request):
    user_profiles=UserProfil.objects.all()
    context={"users":user_profiles}
    return render(request,"list.html",context)


def resume(request, id):
    user_profile = UserProfil.objects.get(id=id)
    template = loader.get_template("resume.html")
    html = template.render({"user_profile": user_profile})
    options = {
        "page-size": "Letter",
        "encoding": "UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type="application/pdf")
    # response["Content-Disposition"] = "attachment"
    # filename = "download.pdf"
    response['Content-Disposition'] = f'attachment; filename="download.pdf"'
    return response