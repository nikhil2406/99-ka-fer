# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import UserPersonal, UserFinancial
from rango.forms import UserPersonalForm, UserFinancialForm

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    #context_dict = {'boldmessage': "I am bold font from the context"}
    #user_list = UserPersonal.objects.all()
    #context_dict = {'userlist': user_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('rango/index.html', {}, context)

def add_user_details(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = UserPersonalForm(request.POST)
        if form.is_valid():
            userpersonal = form.save(commit=True)
            return show_user_details(request,userpersonal.name)
        else:
            print form.errors
    else:
        form = UserPersonalForm()

    return render_to_response('rango/add_user_details.html', {'form': form}, context)


def show_user_details(request, username):
    context = RequestContext(request)
    user = UserPersonal.objects.get(name=username)

    return render_to_response('rango/show_user_details.html',
        {'username': username, 
        'userage': user.age,
        'userphone': user.phone},
        context)

def cash_flow_proj_plan(request, user_name_url):
    context = RequestContext(request)
    return render_to_response('rango/cash_flow_proj_plan.html', {'name': user_name_url}, context)

def retirement_plan(request, user_name_url):
    context = RequestContext(request)
    return render_to_response('rango/retirement_plan.html', {'name': user_name_url}, context)

def insurance_plan(request, user_name_url):
    context = RequestContext(request)
    return render_to_response('rango/insurance_plan.html', {'name': user_name_url}, context)



