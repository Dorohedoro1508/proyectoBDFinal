def user_groups_context(request):
    if request.user.is_authenticated:
        return {
            'is_admin': request.user.groups.filter(name='Administrador').exists(),
            'is_employee': request.user.groups.filter(name='Empleado').exists(),
            'is_auditor': request.user.groups.filter(name='Auditor').exists(),
        }
    return {}
