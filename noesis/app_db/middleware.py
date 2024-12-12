from django.shortcuts import redirect

class ProfileRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Solo redirigir después de iniciar sesión
        if request.user.is_authenticated and request.path == '/':
            user = request.user
            if user.groups.filter(name='Administrador').exists():
                return redirect('admin_dashboard')
            elif user.groups.filter(name='Empleado').exists():
                return redirect('empleado_dashboard')
            elif user.groups.filter(name='Auditor').exists():
                return redirect('auditor_dashboard')
        return self.get_response(request)

