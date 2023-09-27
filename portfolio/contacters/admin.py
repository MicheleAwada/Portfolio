from django.contrib import admin
from .models import User,contacts

from django.shortcuts import render


def view_messages(request):

    context = {}
    return render(request, 'my_custom_template.html', context=context)

# register the custom view
# admin.site.register_view('my-custom-view/', view=view_messages, name='Message view')
admin.site.register(User)
admin.site.register(contacts)