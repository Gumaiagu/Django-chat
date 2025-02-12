from django.shortcuts import render, redirect
from .models import Group, Mensage
from django.utils import timezone


def defining_groups(request):
    # defines the errors
    enter_error = request.session.get('enter_error', '')
    request.session['enter_error'] = ''
    creation_error = request.session.get('creation_error', '')
    request.session['creation_error'] = ''

    # show the page if there's a user, if there isn't the user goes to the login page
    return render(request, 'groups/group_define.html', {'creation_error': creation_error, 'enter_error': enter_error})


def create_group(request):
    # gets the group name and password
    group_name = request.POST.get('group_name', '')
    password = request.POST.get('password', '')

    # gives an error if the group already exists
    if Group.objects.filter(name=group_name).exists():
        request.session['creation_error'] = "This group already exists"
        return redirect("groups:group")

    # creates a group if group_name isn't null
    if group_name:
        g = Group.objects.create()
        g.name = group_name
        g.password = password
        g.save()
    else:
        request.session['creation_error'] = "You did't fill one of the fields"
        return redirect("groups:group")

    return redirect("groups:group_entered", group_name=group_name)


def enter_group(request):
    # gets the group name and password
    group_name = request.POST.get('group_name', '')
    password = request.POST.get('password', '')

    # verify if the group exist and the password is correct
    if Group.objects.filter(name=group_name).exists():
        if Group.objects.get(name=group_name).password == password:
            return redirect("groups:group_entered", group_name=group_name)
        else:
            request.session['enter_error'] = "Wrong password"
            return redirect("groups:group")

    request.session['enter_error'] = "Group doesn't exist"
    return redirect("groups:group")


def entred_group(request, group_name):
    user = request.user
    password = request.session.get('password', '')
    if (Group.objects.get(name=group_name).password != password) or (not request.user.is_authenticated):
        return redirect("groups:group")

    request.session['group_name'] = group_name
    request.session['password'] = password
    messages = list(Mensage.objects.filter(group=Group.objects.get(name=group_name)))
    messages.reverse()
    return render(request, 'groups/group.html', {'group_name': group_name, 'user': user, 'messages': messages, 'is_banned': user.groups.filter(name="Banned").exists()})
