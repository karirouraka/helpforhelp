from help_system.models import HelpReceived


def count_all_helps(request):
    return {'request':request,'help_count':HelpReceived.objects.count()}
