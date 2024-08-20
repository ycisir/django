from typing import Any
from django.shortcuts import HttpResponse

# ============ function based ====================

# def my_middleware(get_response):
#     print('One time initialization')

#     def my_function(request):
#         print('This is before view')
#         response = get_response(request)
#         print('This is after view')
#         return response
    
#     return my_function

# ================================================


# ============ class based =======================

# class MyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('One time initialization')

#     def __call__(self, request):
#         print('This is before view')
#         response = self.get_response(request)
#         print('This is after view')
#         return response

# ================================================


# class BrotherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('One time brother initialization')

#     def __call__(self, request):
#         print('This is brother before view')
#         response = self.get_response(request)
#         print('This is brother after view')
#         return response
    
# class FatherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('One time Father initialization')

#     def __call__(self, request):
#         print('This is Father before view')
#         # response = self.get_response(request)
#         response = HttpResponse('Denied')

#         print('This is Father after view')
#         return response
    
# class MotherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('One time Mother initialization')

#     def __call__(self, request):
#         print('This is Mother before view')
#         response = self.get_response(request)
#         print('This is Mother after view')
#         return response



# ============================== Hooks ==================================
# class MyProcessMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
    
#     def process_view(request, *args, **kwargs):
#         print('This is process view before view')
#         # return HttpResponse('This is before view')
#         return None
    


# class MyExceptionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
    
#     def process_exception(self, request, exception):
#         print('Exception occured!')
#         msg = exception
#         class_name = exception.__class__.__name__
#         print(class_name)
#         print(msg)
#         return HttpResponse(msg)


class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print('Process template response from middleware')
        response.context_data['name'] = 'Yasir'
        return response