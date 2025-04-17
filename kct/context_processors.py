from .models import ProjectMaster


def project_list_processor(request):
    return {
        'Projects': ProjectMaster.objects.filter(is_active = True).all()
    }