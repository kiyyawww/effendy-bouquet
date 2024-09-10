from django.shortcuts import render

def show_main(request):
    context = {
        'nama' : 'Naila Zakiyyah Effendy',
        'kelas' : 'PBP B'
    }

    return render(request, "main.html", context)