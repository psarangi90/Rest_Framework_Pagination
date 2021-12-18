from rest_framework.pagination import CursorPagination
class EmployeeCursorPagination(CursorPagination):
    ordering ="-ename"
    page_size  =10
    cursor_query_param="wfmtcursor"