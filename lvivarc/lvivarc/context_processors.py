from datetime import datetime
from architecture.models import ArchitectureGroup

def current_year(request):
    return {
        "current_year" : datetime.now().year
    }

def groups(request):
    return {
        "groups": ArchitectureGroup.objects.all()
    }