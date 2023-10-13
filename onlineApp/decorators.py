# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from .utils import get_tokens_for_user
# from functools import wraps
# from jwt import DecodeError, ExpiredSignatureError
# from .utils import get_tokens_for_user


# def admin_required(view_func):
#     @wraps(view_func)
#     def wrapper(request, *args, **kwargs):
#         try:
#             payload = get_tokens_for_user(request)
#             user_type = payload['user_type']
#             if user_type!='admin':
#                 return JsonResponse({'error':'unauthorized access'}, status=401)
#         except (DecodeError, ExpiredSignatureError, KeyError):
#             return JsonResponse({'error':'Unauthorized access'}, status=401)
        
#         return view_func(request, *args, **kwargs)
    
#     return wrapper