from django.contrib.auth.decorators import user_passes_test


def role_required(*roles):
    return user_passes_test(lambda user: user.role_tag in roles, login_url='forbidden')
