from django.contrib.auth.decorators import user_passes_test


def check_user(user):
  return not user.is_authenticated or user.is_superuser

user_logout_required = user_passes_test(check_user,'/dashboard/',None)

def auth_user_should_not_access(viewfunc): 

  return user_logout_required(viewfunc)