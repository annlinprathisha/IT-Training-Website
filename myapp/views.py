from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import*
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import*
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.hashers import check_password,make_password
from django.views.generic import ListView,DetailView,DeleteView,UpdateView
from django.http import JsonResponse
from django.urls import reverse_lazy,reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpRequest



# def register(request):
#     if request.method=="POST":
#         full_name=request.POST['myname']
#         date_of_birth=request.POST['dob']
#         gender=request.POST['gender']
#         educational_qualification=request.POST['education']
#         upload_avatar=request.FILES['avatar']
#         mobile_number=request.POST['number']
#         email=request.POST['email']
#         guardians_mobile=request.POST['mobile']
#         training_mode=request.POST['mode']
#         location=request.POST['location']
#         guardians_name=request.POST['guardian1']
#         guardians_occupation=request.POST['guardian2']
#         hobbies_list = request.POST.getlist('hobbies')
#         hobbies = ', '.join(hobbies_list)
#         address=request.POST['address']
#         country=request.POST['country']
#         state=request.POST['state']
#         city=request.POST['city']
#         pin_zip_code=request.POST['pin']
#         user = get_object_or_404(User, email=email)
#         obj=Registration()
#         obj.full_name=full_name
#         obj.date_of_birth=date_of_birth
#         obj.gender=gender
#         obj.educational_qualification=educational_qualification
#         obj.upload_avatar=upload_avatar
#         obj.mobile_number=mobile_number
#         obj.email=email
#         obj.guardians_mobile=guardians_mobile
#         obj.training_mode= training_mode
#         obj.location= location
#         obj.guardians_name=guardians_name
#         obj.guardians_occupation=guardians_occupation
#         obj.hobbies=hobbies
#         obj.address=address
#         obj.country=country
#         obj.state=state
#         obj.city=city
#         obj.pin_zip_code=pin_zip_code
#         obj.user=user
#         obj.save()
#         return redirect('signin')
#     else:
#         return render(request,'register.html')  


# def register(request):
#     if request.method == "POST":
#         full_name = request.POST['myname']
#         date_of_birth = request.POST['dob']
#         gender = request.POST['gender']
#         educational_qualification = request.POST['education']
#         upload_avatar = request.FILES['avatar']
#         mobile_number = request.POST['number']
#         email = request.POST['email']
#         guardians_mobile = request.POST['mobile']
#         training_mode = request.POST['mode']
#         location = request.POST['location']
#         guardians_name = request.POST['guardian1']
#         guardians_occupation = request.POST['guardian2']
#         hobbies_list = request.POST.getlist('hobbies')
#         hobbies = ', '.join(hobbies_list)
#         address = request.POST['address']
#         country = request.POST['country']
#         state = request.POST['state']
#         city = request.POST['city']
#         pin_zip_code = request.POST['pin']

#         # Save the registration information
#         user = get_object_or_404(User, email=email)
#         obj = Registration(
#             full_name=full_name,
#             date_of_birth=date_of_birth,
#             gender=gender,
#             educational_qualification=educational_qualification,
#             upload_avatar=upload_avatar,
#             mobile_number=mobile_number,
#             email=email,
#             guardians_mobile=guardians_mobile,
#             training_mode=training_mode,
#             location=location,
#             guardians_name=guardians_name,
#             guardians_occupation=guardians_occupation,
#             hobbies=hobbies,
#             address=address,
#             country=country,
#             state=state,
#             city=city,
#             pin_zip_code=pin_zip_code,
#             user=user
#         )
#         obj.save()

#         # Send email confirmation
#         user.is_active = False  # Deactivate account until email is confirmed
#         user.save()

#         current_site = get_current_site(request)
#         mail_subject = 'Activate your account.'
#         message = render_to_string('activate.html', {
#             'user': user,
#             'domain': current_site.domain,
#             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#             'token': default_token_generator.make_token(user),
#         })
#         to_email = email
#         send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])

#         return render(request, 'registration_success.html')
#     else:
#         return render(request, 'register.html')


def register(request):
    if request.method == "POST":
        full_name = request.POST['myname']
        date_of_birth = request.POST['dob']
        gender = request.POST['gender']
        educational_qualification = request.POST['education']
        upload_avatar = request.FILES['avatar']
        mobile_number = request.POST['number']
        email = request.POST['email']
        guardians_mobile = request.POST['mobile']
        training_mode = request.POST['mode']
        location = request.POST['location']
        guardians_name = request.POST['guardian1']
        guardians_occupation = request.POST['guardian2']
        hobbies_list = request.POST.getlist('hobbies')
        hobbies = ', '.join(hobbies_list)
        address = request.POST['address']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        pin_zip_code = request.POST['pin']

        # Attempt to send email confirmation
        try:
            # Save the registration information
            user = get_object_or_404(User, email=email)
            obj = Registration(
                full_name=full_name,
                date_of_birth=date_of_birth,
                gender=gender,
                educational_qualification=educational_qualification,
                upload_avatar=upload_avatar,
                mobile_number=mobile_number,
                email=email,
                guardians_mobile=guardians_mobile,
                training_mode=training_mode,
                location=location,
                guardians_name=guardians_name,
                guardians_occupation=guardians_occupation,
                hobbies=hobbies,
                address=address,
                country=country,
                state=state,
                city=city,
                pin_zip_code=pin_zip_code,
                user=user
            )
            obj.save()

            # Send email confirmation
            user.is_active = False  # Deactivate account until email is confirmed
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('activate.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])
            success_message = "Registration successful! Please check your email to confirm your registration."
            return render(request, 'register.html', {'success_message': success_message})

        except Exception as e:
            # Handle any error that occurs during email sending or saving
            # error_message = f"Registration failed: {str(e)}"
            resend_link = reverse('resend_activation_link')  # Properly reverse the URL
            error_message = f'Registration Failed. <a href="{resend_link}">Resend Activation Link</a>'
            return render(request, 'register.html', {'error_message': error_message})

    else:
        return render(request, 'register.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        message = 'activation_success'
    else:
        message = 'activation_failure'
    return redirect(f'/signin?message={message}')
    # return redirect('signin', message=message)
    #     return render(request, 'activation_success.html')
    # else:
    #     return render(request, 'activation_invalid.html')
    
    
# def resend_activation_link(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         try:
#             user = User.objects.get(email=email)
#             if not user.is_active:
#                 current_site = get_current_site(request)
#                 mail_subject = 'Activate your account.'
#                 message = render_to_string('activate.html', {
#                     'user': user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                     'token': default_token_generator.make_token(user),
#                 })
#                 to_email = email
#                 send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])
#                 success_message = "A new activation link has been sent to your email."
#                 return render(request, 'resend_activation.html', {'success_message': success_message})
#             else:
#                 error_message = 'This account is already activated.Please log in!'
#                 return render(request, 'resend_activation.html', {'error_message': error_message})
#         except User.DoesNotExist:
#             error_message = "No account found with this email.Try Again!"
#             return render(request, 'resend_activation.html', {'error_message': error_message})
#     else:
#         return render(request, 'resend_activation.html')


def resend_activation_link(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            if not user.is_active:
                try:
                    current_site = get_current_site(request)
                    mail_subject = 'Activate your account.'
                    message = render_to_string('activate.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                    })
                    to_email = email
                    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])
                    success_message = "A new activation link has been sent to your email."
                    return render(request, 'resend_activation.html', {'success_message': success_message})
                except Exception as e:
                    error_message = 'An error occurred while processing your request. Please try again.'
                    return render(request, 'resend_activation.html', {'error_message': error_message})
            else:
                error_message = 'This account is already activated. Please log in!'
                return render(request, 'resend_activation.html', {'error_message': error_message})
        except User.DoesNotExist:
            error_message = "No account found with this email. Try Again!"
            return render(request, 'resend_activation.html', {'error_message': error_message})
    else:
        return render(request, 'resend_activation.html')


def registration_success(request):
    return render(request, 'registration_success.html')

def activation_success(request):
    return render(request, 'activation_success.html')

def activation_invalid(request):
    return render(request, 'activation_invalid.html')



# def signin(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         keep_me_logged_in = 'logged' in request.POST
#         if User.objects.filter(email=email).exists():
#             user_data = User.objects.get(email=email)
#             if user_data.check_password(password):
#                 login(request, user_data)
#                 request.session['username'] = user_data.username
#                 response = redirect('course_list')
#                 if keep_me_logged_in:
#                     response.set_cookie('login1',user_data.id,max_age=60)
#                 else:
#                     response.set_cookie('login', user_data.id)
#                 return response
#             else:
#                 return HttpResponse('Incorrect Password')
#         else:
#             return HttpResponse('Incorrect email')
#     else:
#         return render(request, 'signin.html')


# def signin(request):
#     errors = {}

#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         keep_me_logged_in = 'logged' in request.POST

#         if not email:
#             errors['email'] = 'Email is required'
#         elif not User.objects.filter(email=email).exists():
#             errors['email'] = 'Incorrect Email'
        
#         if not password:
#             errors['password'] = 'Password is required'
#         elif email and User.objects.filter(email=email).exists():
#             user_data = User.objects.get(email=email)
#             if not user_data.check_password(password):
#                 errors['password'] = 'Incorrect Password'
        
#         if not errors:
            # login(request, user_data)
            # request.session['username'] = user_data.username
            # response = redirect('course_list')
            # if keep_me_logged_in:
            #     response.set_cookie('login1', user_data.id, max_age=60)
            # else:
            #     response.set_cookie('login', user_data.id)
            # return response
    
#     return render(request, 'signin.html', {'errors': errors})


def signin(request: HttpRequest):
    errors = {}
    context = {}

    # Handling POST request for sign-in
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        keep_me_logged_in = 'logged' in request.POST

        # Validate email and password
        if not email:
            errors['email'] = 'Email is required'
        elif not User.objects.filter(email=email).exists():
            errors['email'] = 'Incorrect Email'

        if not password:
            errors['password'] = 'Password is required'
        elif email and User.objects.filter(email=email).exists():
             user_data = User.objects.get(email=email)
             if not user_data.check_password(password):
                 errors['password'] = 'Incorrect Password'
             elif not user_data.is_active:
                 if hasattr(user_data, 'registration'):
                    resend_link = reverse('resend_activation_link')
                    context['error_message'] = f'Account is not activated. Check your email for activation link or <a href="{resend_link}">Resend Activation Link</a>'
                 else:
                    register_link = reverse('register')
                    context['error_message'] = f'Account is not activated.<a href="{register_link}">Register Here!</a>'
                 context['errors'] = errors
                 return render(request, 'signin.html', context)
                #  resend_link = reverse('resend_activation_link')
                #  context['error_message']= f'Account is not activated. Check your email for activation link or <a href="{resend_link}">Resend Activation Link</a>'
                #  context['errors'] = errors
                #  return render(request, 'signin.html', context)
                #  errors['email'] = 'Account is not activated. Check your email for activation link or <a href="{% url \'resend_activation_link\' %}">Resend Activation Link</a>'

        # If no errors, attempt login
        if not errors:
            login(request, user_data)
            request.session['username'] = user_data.username
            response = redirect('course_list')
            if keep_me_logged_in:
                response.set_cookie('login1', user_data.id, max_age=60)
            else:
                response.set_cookie('login', user_data.id)
            return response

    # Handling activation messages
    message = request.GET.get('message', '')
    if message == 'activation_success':
        context['success_message'] = 'Activation successful! You can now log in.'
    elif message == 'activation_failure':
        resend_link = reverse('resend_activation_link')
        context['error_message'] = f'The activation link you used is invalid or has expired. <a href="{resend_link}">Resend Activation Link</a>'
        # context['error_message'] ='The activation link you used is invalid or has expired. <a href="{% url \'resend_activation_link\' %}">Resend Activation Link</a>'

    # Render the sign-in form with errors and activation messages
    context['errors'] = errors
    return render(request, 'signin.html', context)



def signout(request):
    del request.session['username']
    logout(request)
    response = redirect('home')
    response.delete_cookie('login')
    response.delete_cookie('login1')
    return response



def home(request):
    return render(request,'home.html')


@login_required(login_url='signin')
def course_list(request):
    if 'login' in request.COOKIES or 'login1' in request.COOKIES:
        courses = {
            "Software Programming Courses": [
                {"name": "Programming 101", "duration": "4 weeks", "fees": "$100"},
                {"name": "Advanced Programming", "duration": "6 weeks", "fees": "$150"},
                {"name": "JavaScript Basics", "duration": "3 weeks", "fees": "$80"},
                {"name": "Python for Data Science", "duration": "5 weeks", "fees": "$120"},
                {"name": "Java Programming", "duration": "2 weeks", "fees": "$60"},
                {"name": "C++ Essentials", "duration": "8 weeks", "fees": "$200"},
                {"name": "Ruby on Rails", "duration": "7 weeks", "fees": "$170"},
                {"name": "Swift Programming", "duration": "10 weeks", "fees": "$250"},
                {"name": "Kotlin for Android", "duration": "6 weeks", "fees": "$140"},
                {"name": "Full-Stack Web Development", "duration": "12 weeks", "fees": "$300"}
            ],
            "Software Testing Courses": [
                {"name": "Manual Testing", "duration": "4 weeks", "fees": "$100"}
            ],
            "Networking, Server, & Cloud": [
                {"name": "Networking Basics", "duration": "5 weeks", "fees": "$120"},
                {"name": "Advanced Networking", "duration": "8 weeks", "fees": "$200"},
                {"name": "Cloud Computing", "duration": "10 weeks", "fees": "$250"},
                {"name": "Server Management", "duration": "6 weeks", "fees": "$150"},
                {"name": "Cybersecurity", "duration": "7 weeks", "fees": "$170"},
                {"name": "AWS Certification", "duration": "8 weeks", "fees": "$200"},
                {"name": "Azure Fundamentals", "duration": "6 weeks", "fees": "$140"}
            ],
            "Other Courses": [
                {"name": "Project Management", "duration": "5 weeks", "fees": "$120"},
                {"name": "Data Analytics", "duration": "8 weeks", "fees": "$200"},
                {"name": "Digital Marketing", "duration": "6 weeks", "fees": "$150"},
                {"name": "Graphic Design", "duration": "7 weeks", "fees": "$170"}
            ]
        }

        selected_course = SelectedCourse.objects.filter(user=request.user).first()
        if selected_course:
            signed_up_courses = selected_course.courses.all()
        else:
            signed_up_courses = []

        user_name = request.user.username
        return render(request, 'dashboard.html', {
            'courses': courses,
            'signed_up_courses': signed_up_courses,
            'user_name': user_name,
        })
    else:
        return redirect('signin')




def save_selected_courses(request):
    if request.method == 'POST':
        user = request.user
        course_name = request.POST.get('course_name')
        course = Course.objects.get(name=course_name)
        selected_course, created = SelectedCourse.objects.get_or_create(user=user)
        selected_course.courses.add(course)
        selected_course.save()
    return redirect('course_list')


import logging
logger = logging.getLogger(__name__)
def delete_selected_course(request):
    if request.method == 'POST':
        try:
            user = request.user
            course_name = request.POST.get('course_name')
            course = Course.objects.get(name=course_name)
            selected_course = SelectedCourse.objects.get(user=user)
            selected_course.courses.remove(course)
            selected_course.save()
            return JsonResponse({'success': True})  
        except Course.DoesNotExist:
            logger.error(f"Course '{course_name}' does not exist.")
            return JsonResponse({'success': False, 'error': 'Course does not exist'}, status=400)
        except SelectedCourse.DoesNotExist:
            logger.error(f"No SelectedCourse object found for user '{user}'.")
            return JsonResponse({'success': False, 'error': 'SelectedCourse object not found'}, status=400)
        except Exception as e:
            logger.error(f"An error occurred while deleting the selected course: {e}")
            return JsonResponse({'success': False, 'error': 'An error occurred'}, status=500)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)



def save_courses():
    courses_data = [
        {"name": "Programming 101", "duration": "4 weeks", "fees": "$100"},
        {"name": "Advanced Programming", "duration": "6 weeks", "fees": "$150"},
        {"name": "JavaScript Basics", "duration": "3 weeks", "fees": "$80"},
        {"name": "Python for Data Science", "duration": "5 weeks", "fees": "$120"},
        {"name": "Java Programming", "duration": "2 weeks", "fees": "$60"},
        {"name": "C++ Essentials", "duration": "8 weeks", "fees": "$200"},
        {"name": "Ruby on Rails", "duration": "7 weeks", "fees": "$170"},
        {"name": "Swift Programming", "duration": "10 weeks", "fees": "$250"},
        {"name": "Kotlin for Android", "duration": "6 weeks", "fees": "$140"},
        {"name": "Full-Stack Web Development", "duration": "12 weeks", "fees": "$300"},
        {"name": "Manual Testing", "duration": "4 weeks", "fees": "$100"},
        {"name": "Networking Basics", "duration": "5 weeks", "fees": "$120"},
        {"name": "Advanced Networking", "duration": "8 weeks", "fees": "$200"},
        {"name": "Cloud Computing", "duration": "10 weeks", "fees": "$250"},
        {"name": "Server Management", "duration": "6 weeks", "fees": "$150"},
        {"name": "Cybersecurity", "duration": "7 weeks", "fees": "$170"},
        {"name": "AWS Certification", "duration": "8 weeks", "fees": "$200"},
        {"name": "Azure Fundamentals", "duration": "6 weeks", "fees": "$140"},
        {"name": "Project Management", "duration": "5 weeks", "fees": "$120"},
        {"name": "Data Analytics", "duration": "8 weeks", "fees": "$200"},
        {"name": "Digital Marketing", "duration": "6 weeks", "fees": "$150"},
        {"name": "Graphic Design", "duration": "7 weeks", "fees": "$170"}
    ]
    
    for course_data in courses_data:
        course = Course.objects.create(
            name=course_data['name'],
            duration=course_data['duration'],
            fees=course_data['fees']
        )
        course.save()



   
class Detail(DetailView):
    model = Registration
    template_name = 'profile.html'
    context_object_name = 'detail'

    def get_object(self, queryset=None):
        # Retrieve the User object based on the username provided in the URL
        user = User.objects.get(username=self.kwargs['username'])
        # Retrieve the associated Registration object for the user
        registration = Registration.objects.get(user=user)
        return registration
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the hobbies data from the related Registration object and split it into a list
        context['detail'].hobbies_list = context['detail'].hobbies.split(', ')
        return context
    

class UpdateData(UpdateView):
    model = Registration
    form_class = Form_Validation
    template_name = 'update_profile.html'


    def get_initial(self):
        initial = super().get_initial()
        # Retrieve the hobbies of the instance and split them into a list
        hobbies = self.object.hobbies.split(', ')
        # Set the initial value for the hobbies field as a list of selected hobbies
        initial['hobbies'] = hobbies
        return initial

    def form_valid(self, form):
        # Join the list of hobbies into a comma-separated string
        form.instance.hobbies = ', '.join(form.cleaned_data.get('hobbies', []))
        return super().form_valid(form)

    def get_success_url(self):
        # Reverse the 'Detail' URL pattern, passing the object's pk
        return reverse('Detail', kwargs={'username': self.object.user.username})


class ChangePassword(UpdateView):
    model=User
    form_class=ChangePassword
    template_name='change_password.html'
    success_url = reverse_lazy('signin')  
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        logout(self.request)  
        return response
    
    
# class ForgotPasswordView(View):
#     def get(self, request):
#         form = ForgotPasswordForm()
#         return render(request, 'forgot_password.html', {'form': form})

#     def post(self, request):
#         form = ForgotPasswordForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             try:
#                 user = User.objects.get(email=email)
#                 temporary_password = get_random_string(length=8)
#                 user.set_password(temporary_password)
#                 user.save()
#                 send_mail(
#                     'Your Temporary Password',
#                     f'Your temporary password is {temporary_password}. Please use this to log in and change your password.',
#                     'annlinprathisha@gmail.com',
#                     [email],
#                     fail_silently=False,
#                 )
#                 return redirect('reset_password')
#             except User.DoesNotExist:
#                 form.add_error('email', 'Email address not found')
#         return render(request, 'forgot_password.html', {'form': form})


class ForgotPasswordView(View):
    def get(self, request):
        form = ForgotPasswordForm()
        return render(request, 'forgot_password.html', {'form': form})

    def post(self, request):
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                try:
                    temporary_password = get_random_string(length=8)
                    user.set_password(temporary_password)
                    user.save()
                    send_mail(
                        'Your Temporary Password',
                        f'Your temporary password is {temporary_password}. Please use this to log in and change your password.',
                        'annlinprathisha@gmail.com',
                        [email],
                        fail_silently=False,
                    )
                    messages.success(request, 'A temporary password has been sent to your email.')
                    return redirect('reset_password')
                except Exception as e:
                    form.add_error('email', 'An error occurred while processing your request. Please try again.')
            except User.DoesNotExist:
                form.add_error('email', 'Email address not found')
        return render(request, 'forgot_password.html', {'form': form})
    

class ResetPasswordView(View):
    def get(self, request):
        form = ResetPasswordForm()
        message = messages.get_messages(request)
        return render(request, 'reset_password.html', {'form': form,'message': message})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            temporary_password = form.cleaned_data['temporary_password']
            new_password = form.cleaned_data['new_password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(temporary_password):
                    user.set_password(new_password)
                    user.save()
                    return redirect('signin')
                else:
                    form.add_error('temporary_password', 'Temporary password is incorrect')
            except User.DoesNotExist:
                form.add_error('email', 'Email address not found')
        return render(request, 'reset_password.html', {'form': form})
    
# class FirstLoginView(View):
#     def get(self, request):
#         form = FirstLoginForm()  
#         return render(request, 'first_login.html', {'form': form})

#     def post(self, request):
#         form = FirstLoginForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             try:
#                 user = User.objects.get(email=email)
#                 form.add_error('email', 'This email is already registered. Use "Forgot Password" to reset your password.')
#             except User.DoesNotExist:
#                 # If user does not exist, create a new user with a temporary password
#                 temporary_password = get_random_string(length=8)
#                 user = User.objects.create_user(username=username, email=email, password=temporary_password)
#                 user.save()
#                 send_mail(
#                     'Your Temporary Password',
#                     f'Your temporary password is {temporary_password}. Please use this to log in and create password.',
#                     'from@example.com',
#                     [email],
#                     fail_silently=False,
#                 )
#                 return redirect('create_password')
#         return render(request, 'first_login.html', {'form': form})
    
class FirstLoginView(View):
    def get(self, request):
        form = FirstLoginForm()  
        return render(request, 'first_login.html', {'form': form})

    def post(self, request):
        form = FirstLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                form.add_error('email', 'This email is already registered. Use "Forgot Password" to reset your password.')
            except User.DoesNotExist:
                try:
                    # If user does not exist, create a new user with a temporary password
                    temporary_password = get_random_string(length=8)
                    user = User.objects.create_user(username=username, email=email, password=temporary_password)
                    user.is_active = False
                    user.save()
                    send_mail(
                        'Your Temporary Password',
                        f'Your temporary password is {temporary_password}. Please use this to log in and create password.',
                        'annlinprathisha@gmail.com',
                        [email],
                        fail_silently=False,
                    )
                    messages.success(request, 'A temporary password has been sent to your email.')
                    return redirect('create_password')
                except Exception as e:
                    form.add_error('email', 'An error occurred while creating the user. Please try again.')
        return render(request, 'first_login.html', {'form': form})
    

class CreatePasswordView(View):
    def get(self, request):
        form = CreatePasswordForm()
        message = messages.get_messages(request)
        return render(request, 'create_password.html', {'form': form,'message': message})

    def post(self, request):
        form = CreatePasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            temporary_password = form.cleaned_data['temporary_password']
            new_password = form.cleaned_data['new_password']
            try:
                user = User.objects.get(username=username)
                if user.check_password(temporary_password):
                    user.set_password(new_password)
                    user.save()
                    return redirect('register')
                else:
                    form.add_error('temporary_password', 'Temporary password is incorrect')
            except User.DoesNotExist:
                form.add_error('email', 'Email address not found')
        return render(request, 'create_password.html', {'form': form})



def about(request):
    return render(request,'about.html')

# def contact(request):
#     return render(request,'contact.html')


# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             try:
#                 email=request.POST['email']
#                 subject=request.POST['subject']
#                 message=request.POST['message']
#                 from_mail='annlinprathisha@gmail.com'
#                 send_mail(subject,message,from_mail,[mail],fail_silently=False)
#                 return render(request, 'contact_success.html', {'message': 'Email sent successfully!'})
#             except Exception as e:
#                 return render(request, 'contact_failure.html', {'message': f'Failed to send email: {str(e)}'})
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})


def contact_view(request):
    message = ""
    message_type = ""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                from_mail='annlinprathisha@gmail.com'
                send_mail(subject,message,from_mail,[email],fail_silently=False)
                message = "Email sent successfully!"
                message_type = "success"
            except Exception as e:
                message = f"Failed to send email: {str(e)}"
                message_type = "error"
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'message': message, 'message_type': message_type})




    
    



