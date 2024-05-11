from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate(request, data, count):
    paginator = Paginator(data, count)
    page = request.GET.get('page')
    try:
        paginated_data = paginator.page(page)
    except PageNotAnInteger:
        paginated_data = paginator.page(1)
    except EmptyPage:
        paginated_data = paginator.page(paginator.num_pages)
    
    return paginated_data
