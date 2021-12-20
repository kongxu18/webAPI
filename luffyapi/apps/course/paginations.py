from rest_framework.pagination import PageNumberPagination as DRFPageNumberPagination


class PageNumberPagination(DRFPageNumberPagination):
    # 一页一个
    page_size = 1
    max_page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'size'
