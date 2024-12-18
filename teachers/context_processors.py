from .models import Teacher
def session_data(request):

    """
    if user_id:
        teach = Teacher.objects.get(user=user_id)
    else:
        teach = " "
    """
    return {
        'user_id': request.session.get('user_id'),
        'user_email': request.session.get('email'),
        'is_teacher': request.session.get('is_teacher'),

    }