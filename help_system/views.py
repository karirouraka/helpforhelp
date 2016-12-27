from django.shortcuts import render,HttpResponse, redirect
from help_system.models import UserProfile, Help, HelpReceived
from help_system.forms import *
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import login_required
# Create your views here


def index(request):
    return render(request, 'index.html', {})

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
            return redirect('fill_out_profile')
        else:
            return render(request, 'tutor/registration_page.html', {'registration_form': registration_form})
    registration_form = UserRegistrationForm()
    return render(request,'tutor/registration_page.html',{'registration_form':registration_form})

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
            return render(request,'tutor/login_page.html', {'login_form': login_form})
    login_form = LogInForm()
    return render(request, 'tutor/login_page.html', {'login_form': login_form})



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
                for key in profile_form.cleaned_data:
                    if hasattr(user_profile_base,key):
                        setattr(user_profile_base,key,profile_form.cleaned_data[key])
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
    return  render(request, 'tutor/tutor_profiles.html',{'tutor_profiles':tutor_profiles})

@login_required
def get_tutor_by_pk(request, tutor_pk):
    tutor = UserProfile.objects.get(pk=tutor_pk)
    reference_form = ReferenceForm()

    return render(request, 'tutor/tutor.html', {'tutor': tutor, 'reference_form': reference_form})

@login_required
def send_reference(request, tutor_pk):
    tutor = UserProfile.objects.get(pk=tutor_pk)
    reference_form = ReferenceForm(request.POST)
    if reference_form.is_valid():
        reference = reference_form.save(commit=False)
        reference.author = request.user
        reference.tutor = tutor
        reference.save()
        return redirect('get_tutor_by_name', tutor_pk=tutor_pk)
    return render(request,'tutor/tutor.html', {'tutor': tutor, 'reference_form': reference_form})

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
def add_record(request):
    if request.POST:
        record_form = RecordForm(request.POST)
        if record_form.is_valid():
            if not hasattr(request.user,'profile'):
                return redirect('fill_out_profile')
            helps = Help.objects.filter(tutor = request.user.profile)
            data = record_form.cleaned_data
            times = data.get('time', None)
            date = data.get('date')
            for help in helps:
                record = Record()
                record.date = date
                record.help = help
                record.save()
                record = Record.objects.last()
                for t in times:
                    record.time.add(t)
            record.save()
            return redirect('show_all_helps')
        else:
            return render(request, 'help/add_date.html', {'record_form': record_form})
    record_form = RecordForm()
    return render(request, 'help/add_date.html', {'record_form': record_form})


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
    return render(request, 'help/detailed_help_information.html', {'help': help})

@login_required
def receive_help(request, help_pk):
    student_profile = request.user.profile
    help = Help.objects.get(pk=help_pk)
    received_help = HelpReceived.objects.create(student = student_profile, help = help)
    return redirect('get_help', help_pk=help_pk)

@login_required
def delete_help(request, help_pk):
    help=Help.objects.get(pk=help_pk)
    help.delete()
    return redirect('show_all_helps')