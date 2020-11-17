from django.contrib.auth import authenticate
from django.shortcuts import redirect


def is_logedin(view_func):
    def wrapper(request, *args , **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args , **kwargs)
    return wrapper


def is_restricted(allowed_roles = [] ):
    def decorator(view_func):
        def wrapper(request , *args , **kwargs):
            group = None
            if request.user.groups.exists():
                # request.user.groups.all() returns a query set so we have to take the first element
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request , *args , **kwargs)
            else:
                return redirect('profile')
        return wrapper
    return decorator


