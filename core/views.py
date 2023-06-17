from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def index(request):
    return render(request, "home.html")


def submit(request):
    import subprocess
    ip = request.POST.get('ip')

    res = subprocess.check_output(f"ping  -n 1 {ip}", shell=True)
    print(res)
    dados = {"resposta": res}
    return render(request, "home.html",dados)