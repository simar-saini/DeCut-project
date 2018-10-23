from django.shortcuts import render,redirect
from .forms import signup_form,LoginForm
from .models import signup_model,SessionToken
from django.contrib.auth.hashers import check_password,make_password
# Create your views here.

def dashboard(request):
    response_data={}
    if request.method == "POST":
        print('post called login')
        form = LoginForm(request.POST)
        if form.is_valid():
            print('form valid login')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = signup_model.objects.filter(username=username).first()
            print('user')
            if (user):
                print('user match')
                # Check for the password
                if check_password(password, user.password):

                    print('User is valid')
                    token = SessionToken(user=user)
                    token.create_token()
                    token.save()
                    response = redirect('sucess/')
                    response.set_cookie(key='session_token', value=token.session_token)
                    return response
                else:
                    response_data['message'] = 'Incorrect Password! Please try again!'

    elif request.method == "GET":
        form = LoginForm()

    return render(request,'decut/decut.html',{'form': form})


def feed_view(request):
    return render(request, 'decut/sucess.html')


# For validating the session
def check_validation(request):
    if request.COOKIES.get('session_token'):
        session = SessionToken.objects.filter(session_token=request.COOKIES.get('session_token')).first()
        if session:
            return session.user
    else:
        return None


def signup_view(request):
    if request.method == "POST":
        print("post called")
        form = signup_form(request.POST)
        print("form post")
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            details=form.cleaned_data['details']
            # saving data to DB
            user = signup_model(details=details ,password=make_password(password), email=email, username=username)
            user.save()
            print("user save")
    elif request.method == "GET":
        print("get called")
        form = signup_form()

    return render(request,'decut/signup2.html',{'form':form})


