from django.shortcuts import redirect

def login_required(view):
    def _wrapped_view_func(request, *args, **kwargs): 
        if not request.session.get('current_teacher_id'):     
            return redirect('/login')
        else:
             return view(request, *args, **kwargs)     
    return _wrapped_view_func