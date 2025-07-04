from django.http import HttpResponse

# Create your views here.

def post_list(request, year=None, monthe=None):
    if monthe is not None:
        return HttpResponse(f"Post list archive for {year} and {monthe}")
    
    if year is not None:
        return HttpResponse(f"Post list archive for {year}")
    
    return HttpResponse("Post list page")

def categories_list(request):
    return HttpResponse("Category list page")

def post_detail(request, post_slug):
    return HttpResponse(f"Poat detail {post_slug}")

def custom_post_detail(request):
    return HttpResponse("Custom post detail")
