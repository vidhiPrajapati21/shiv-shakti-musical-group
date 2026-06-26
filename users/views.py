from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        print("=" * 50)
        print("Username:", username)

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("Authenticated User:", user)

        if user is not None:

            login(request, user)

            print("LOGIN SUCCESS")
            print("Redirecting to Dashboard...")
            print("=" * 50)

            return redirect('dashboard')

        else:

            print("LOGIN FAILED")
            print("=" * 50)

            return render(
                request,
                'login.html',
                {
                    'error': 'Invalid Username or Password'
                }
            )

    return render(request, 'login.html')


def user_logout(request):

    logout(request)

    return redirect('login')