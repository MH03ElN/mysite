from django.http import HttpResponse,JsonResponse

def http_test(requests):
    return HttpResponse('<h1>hi this is a text for test</h1>')

def json_test(requests):
    return JsonResponse({'name':'hosein','lastname':'karbasi','age':19})