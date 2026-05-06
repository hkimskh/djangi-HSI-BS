from django.shortcuts import render

def santri_home(request):
    return render(request, "santri/profile_home.html")

def biodata(request):
    return render(request, "santri/biodata.html")

def jadwal(request):
    return render(request, "santri/jadwal.html")

def galeri(request):
    return render(request, "santri/galeri.html")

def feedback(request):
    return render(request, "santri/feedback.html")