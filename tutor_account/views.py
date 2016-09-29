from django.shortcuts import render,render_to_response,HttpResponse, redirect
from django.template import RequestContext
from tutor_account.models import UserProfile, Help
from tutor_account.forms import UserRegistrationForm, UserProfileForm, LogInForm, HelpForm
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
    if request.POST:
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            user_profile_base = UserProfile.objects.filter(registration_info = request.user).first()
            if user_profile_base:
                # user_profile_base.delete()
                for key in profile_form.cleaned_data:
                    if hasattr(user_profile_base,key):
                        setattr(user_profile_base,key,profile_form.cleaned_data[key])
                # changed_data = profile_form.cleaned_data
                # if user_profile_base.name != changed_data['name']:
                #     user_profile_base.name = changed_data['name']
                user_profile_base.save()
            else:
                user_profile = profile_form.save(commit=False)
                user_profile.registration_info = request.user
                user_profile.save()
            return redirect('fill_out_profile')
        else:
            return render(request, 'tutor/profile_fill.html', {'profile_form': profile_form})
    user_profile = UserProfile.objects.filter(registration_info = request.user).first()
    if user_profile:
        profile_form = UserProfileForm(instance=user_profile)
    else:
        profile_form = UserProfileForm()
    return render(request, 'tutor/profile_fill.html', {'profile_form': profile_form})



def show_all_tutors(request):
    tutor_profiles = UserProfile.objects.all()
    return  render_to_response('tutor/tutor_profiles.html',{'tutor_profiles':tutor_profiles},context_instance=RequestContext(request))

@login_required
def show_all_helps(request):
    helps = Help.objects.all()
    return render(request,'help/helps.html', {'helps': helps})

@login_required
def fill_out_help(request):
    if request.POST:
        help_form = HelpForm(request.POST)
        if help_form.is_valid():
            if not hasattr(request.user,'profile'):
                return redirect('fill_out_profile')
            help = help_form.save(commit=False)
            help.tutor = request.user.profile
            help.save()
            return redirect('show_all_helps')
        else:
            return render(request, 'tutor/register_help.html', {'help_form': help_form})
    help_form = HelpForm()
    return render(request, 'tutor/register_help.html', {'help_form': help_form})

@login_required
def edit_help(request, help_pk):
    help=Help.objects.get(pk=help_pk)
    if request.POST:
        help_form=HelpForm(request.POST)
        if help_form.is_valid():
            for key in help_form.cleaned_data:
                if hasattr(help, key):
                    setattr(help, key, help_form.cleaned_data[key])
            help.save()
            return redirect('edit_help',help_pk= help_pk)
        else:
            return render(request, 'help/edit_help.html', {'help_form':help_form})

    help_form=HelpForm(instance=help)
    return render(request, 'help/edit_help.html', {'help_form':help_form})

@login_required
def get_help(request, help_pk):
    help = Help.objects.get(pk=help_pk)
    return render(request, 'help/help.html', {'help': help})


@login_required
def delete_help(request, help_pk):
    help=Help.objects.get(pk=help_pk)
    help.delete()
    return redirect('show_all_helps')


