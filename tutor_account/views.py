from django.shortcuts import render,render_to_response,HttpResponse, redirect
from django.template import RequestContext
from tutor_account.models import UserProfile, Help
from tutor_account.forms import UserRegistrationForm, UserProfileForm, LogInForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required
# Create your views here
#
# .
def register(request):
    if request.POST:
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():

            username = registration_form.cleaned_data['username']
            password = registration_form.cleaned_data['password']
            email = registration_form.cleaned_data['email']
            user = User.objects.create(username=username,email=email)
            user.set_password(password)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            login(request, user)


            return redirect('fill_out_profile',profile_pk = user.pk)
        else:
            return render_to_response('tutor/registration_page.html', {'registration_form': registration_form},
                                      context_instance=RequestContext(request))
    registration_form = UserRegistrationForm()
    return render_to_response('tutor/registration_page.html',{'registration_form':registration_form},context_instance=RequestContext(request))

def log_in(request):
    if request.POST:
        login_form = LogInForm(request.POST)
        if login_form.is_valid():

            user_identification = login_form.cleaned_data['user_identification'].strip()
            password = login_form.cleaned_data['password'].strip()
            user_by_email = authenticate(email=user_identification, password=password)
            user_by_login = authenticate(username=user_identification, password=password)
            if user_by_email:
                login(request, user_by_email)
            elif user_by_login:
                login(request, user_by_login)

            return redirect('fill_out_profile')
        else:
            return render_to_response('tutor/login_page.html', {'login_form': login_form},
                                      context_instance=RequestContext(request))
    login_form = LogInForm()
    return render_to_response('tutor/login_page.html', {'login_form': login_form},
                              context_instance=RequestContext(request))



def loged_out_successfully(request):
    return render(request, 'tutor/logout_page.html')

def log_out(request):
    logout(request)
    return redirect('loged_out_successfully')

@login_required
def fill_out_profile(request):
    profile_form = UserProfileForm()
    return render_to_response('tutor/profile_fill.html', {'profile_form':profile_form}, context_instance=RequestContext(request))



def show_all_tutors(request):
    tutor_profiles = UserProfile.objects.all()
    return  render_to_response('tutor/tutor_profiles.html',{'tutor_profiles':tutor_profiles},context_instance=RequestContext(request))

@login_required
def show_all_helps(request):
    helps = Help.objects.all()
    return render(request,'help/helps.html', {'helps': helps})



