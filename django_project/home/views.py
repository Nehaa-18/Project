from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import CustomUser  # Assuming you have a CustomUser model
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from home.models import CustomUser

# Create your views here.
@never_cache  # Add this decorator to prevent caching
def index(request):
    return render(request,'index.html')
#@never_cache
#def logout_view(request):
    #if request.user.is_authenticated:
        #logout(request)
    #return redirect('index')
@never_cache
def about(request):
    return render(request,'about.html')

@never_cache
def contact(request):
    return render(request,'contact.html')

@never_cache
def product(request):
    return render(request,'product.html')

@never_cache
def cart(request):
    return render(request,'cart.html')

@never_cache
def account(request):
    return render(request,'account.html')

@never_cache
def order(request):
    return render(request,'order.html')

@never_cache
def wishlist(request):
    return render(request,'wishlist.html')

@never_cache
def accountorg(request):
    return render(request,'accountorg.html')

@never_cache
def rent(request):
    return render(request,'rent.html')

@never_cache
def movingequip(request):
    return render(request,'movingequip.html')

@never_cache
def addequip(request):
    return render(request,'addequip.html')


@never_cache
@login_required(login_url='login')
def admindash(request):
     if request.user.is_superuser:
        users = CustomUser.objects.exclude(is_superuser=True)
        return render(request, "admindash.html", {"users": users})
        return redirect("home")
     

@never_cache
def dashboard(request):
    return render(request,'dashboard.html')


@never_cache
@login_required(login_url='login')
def dashboardOrg(request):
    if 'username' in request.session:
        response = render(request, 'dashboardOrg.html')
        if response:
            response['Cache-Control'] = 'no-store,must-revalidate'
            return response
        else:
            return HttpResponse("An error occurred in rendering the response.")
    else:
        return redirect('login')
    

@never_cache
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']  # Make sure this matches your form field name
        usertype = request.POST['usertype']

        if password != confirm_password:
            # Handle password mismatch error
            return render(request, 'registration.html', {'error_message': 'Passwords do not match'})

        # Create a new user object
        user = CustomUser.objects.create_user(username=username, email=email, password=password, usertype=usertype)
        # You may want to do additional processing here if needed
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('login')  # Redirect to login page after successful registration
        
    return render(request,'registration.html')




from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
@never_cache
def login(request):
    if request.method == 'POST':
        loginusername = request.POST.get('username')
        password = request.POST.get('password')

        if loginusername and password:  # Use 'loginusername' here
            # Check if the entered credentials are for the admin
            if loginusername == "admin" and password == "Ajce24@mca":
                users = CustomUser.objects.exclude(is_superuser='1')  # Exclude superusers
                user_count = users.count()
                context = {
                    "users": users,
                    "user_count": user_count
                }
                return render(request, 'admindash.html', context)
            else:
                # For regular users, attempt to authenticate
                user = authenticate(request, username=loginusername, password=password)

                if user is not None:
                    auth_login(request, user)
                    request.session['username'] = user.username
                    if user.usertype == 'User':
                        return redirect('dashboard')
                    elif user.usertype == 'Company':
                        return redirect('dashboardOrg')
                    else:
                        return redirect('admindash')
                else:
                    error_message = "Invalid username or email"
                    return render(request, 'login.html', {'error_message': error_message})
        else:
            error_message = "email and password are required"
            return render(request, 'login.html', {'error_message': error_message})
    response = render(request, 'login.html')
    response['Cache-Control'] = 'no-store,must-revalidate'
    return response


@never_cache
@login_required(login_url='login')
def dashboard(request):
    if 'username' in request.session:
        response = render(request,'dashboard.html')
        response['Cache-Control'] = 'no-store,must-revalidate'
        return response
    else:
        return redirect('login')
    
@never_cache
@login_required(login_url='login')
def dashboardOrg(request):
    if 'username' in request.session:
        response = render(request,'dashboardOrg.html')
        response['Cache-Control'] = 'no-store,must-revalidate'
        return response
    else:
        return redirect('login')
    
@never_cache
def handlelogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

@never_cache
def logout(request):
    auth.logout(request)
    return redirect("/")



from .models import Wishlist, Product
@never_cache
def add_to_wishlist(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlist.products.add(product)
        return redirect('wishlist')
    else:
        # Handle cases where the user is not authenticated
        # You may want to redirect them to the login page or show a message
        return redirect('login')
@never_cache
def remove_from_wishlist(request, product_id):
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.get(user=request.user)
        product = Product.objects.get(pk=product_id)
        wishlist.products.remove(product)
        return redirect('wishlist')
    else:
        # Handle cases where the user is not authenticated
        # You may want to redirect them to the login page or show a message
        return redirect('login')
@never_cache
def view_wishlist(request):
    if request.user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        return render(request, 'wishlist.html', {'wishlist': wishlist})
    else:
        # Handle cases where the user is not authenticated
        # You may want to redirect them to the login page or show a message
        return redirect('login')
    






from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
#from .models import MyUser
from django.template.loader import render_to_string
@never_cache
def deactivate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if user.is_active:
        user.is_active = False
        user.save()
         # Send deactivation email
        subject = 'Account Deactivation'
        message = 'Your account has been deactivated by the admin.'
        from_email = 'nehaa2024b@mca.ajce.in'  # Replace with your email
        recipient_list = [user.email]
        html_message = render_to_string('deactivation_mail.html', {'user': user})

        send_mail(subject, message, from_email, recipient_list, html_message=html_message)

        messages.success(request, f"User '{user.username}' has been deactivated, and an email has been sent.")
    else:
        messages.warning(request, f"User '{user.username}' is already deactivated.")
    return redirect('admindash')
@never_cache
def activate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if not user.is_active:
        user.is_active = True
        user.save()
        subject = 'Account activated'
        message = 'Your account has been activated.'
        from_email = 'nehaa2024b@mca.ajce.in'  # Replace with your email
        recipient_list = [user.email]
        html_message = render_to_string('activation_mail.html', {'user': user})

        send_mail(subject, message, from_email, recipient_list, html_message=html_message)
    else:
        messages.warning(request, f"User '{user.username}' is already active.")
    return redirect('admindash')
# @never_cache
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         if username == "admin" and password == "Ajce24@mca":
#             # For the superuser, redirect to admin_index.html with user list and count
#             users = CustomUser.objects.exclude(is_superuser='1')  # Exclude superusers
#             user_count = users.count()
#             context = {
#                 "users": users,
#                 "user_count": user_count
#             }
#             return render(request, 'admindash.html', context)
#         else:
#             # For regular users, attempt to authenticate
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 request.session['username'] = user.username
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Invalid credentials!!')  # Set the error message
#                 return render(request, 'login.html')

#     return render(request, 'login.html')



from django import forms
from django.shortcuts import render, redirect
from .models import Product
from decimal import Decimal
from decimal import Decimal,InvalidOperation # Import Decimal

# def addequip(request):
#     if request.method == 'POST':
#         # Extract form data from the request
#         name = request.POST['name']
#         # Convert rating and price_per_day to Decimal
#         rating = request.POST['rating'] 
#         availability = request.POST['availability']
#         description = request.POST['description']
#         price_per_day = request.POST['price_per_day']
#         category = request.POST['category']
        
#         # Assuming you have a file input with name "image"
#         image = request.FILES['image']

#         # Create a new Product object and save it to the database
#         product = Product(
#             name=name,
#             rating=rating,
#             availability=availability,
#             description=description,
#             price_per_day=price_per_day,
#             category=category,
#             image=image
#         )
#         product.save()

#         # Redirect to a success page or do something else
#         return redirect('admindash')

#     # If the request method is not POST, render the form page
#     return render(request, 'addequip.html')

   




# def addequip(request):
#     if request.method == 'POST':
        
#         name = request.POST.get('name')
#         # Convert rating and price_per_day to Decimal
#         rating = Decimal(request.POST.get('rating')) if request.POST.get('rating') else Decimal('0')
#         availability = request.POST.get('availability')
#         description = request.POST.get('description')
#         price_per_day = Decimal(request.POST.get('price_per_day')) if request.POST.get('price_per_day') else Decimal('0')
#         category = request.POST.get('category')
        
#         # Assuming you have a file input with name "image"
#         image = request.FILES('image')
#         if name and rating and availability and description and price_per_day and category and image:
#             addequip = addequip(name=name,rating=rating,availability=availability,description=description,price_per_day=price_per_day,category=category,image=image)
#             addequip.save()  # Save the bus data to the database
#             return redirect('admindash')  # Redirect to a list view or another page

#     return render(request,'addequip.html')

# 



from django.shortcuts import render, redirect
from decimal import Decimal, InvalidOperation
from .models import Product
from django.http import HttpResponseRedirect
def addequip(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        price_per_day = request.POST.get('price_per_day')
        category = request.POST.get('category')
        availability = request.POST.get('availability')
        image = request.FILES.get('image')

        try:
            if rating is not None:
                rating = Decimal(rating)
            if price_per_day is not None:
                price_per_day = Decimal(price_per_day)
        except (InvalidOperation, TypeError, ValueError):
            return render(request, 'error.html', {'message': 'Invalid input for rating or price.'})

        if name and description and category and image:
            product = Product(
                name=name,
                description=description,
                rating=rating if rating is not None else Decimal('0'),
                price_per_day=price_per_day if price_per_day is not None else Decimal('0'),
                category=category,
                availability=availability,
                image=image
            )
            product.save()
            return HttpResponseRedirect('admindash')
    
    # Add a return statement for the case where the conditions aren't met
    return render(request, 'addequip.html')




def view_equip(request):
    # Query the database to get all bus objects
    equips = Product.objects.all()

    # Create a context dictionary to pass the bus data to the template
    context = {
        'equips': equips
    }

    # Render the template and pass the context
    return render(request, 'view_equip.html',context)






from django.shortcuts import render
from .models import CustomUser

def usertypecount(request):
    user_count = CustomUser.objects.filter(usertype='User').count()
    company_count = CustomUser.objects.filter(usertype='Company').count()
    
    context = {
        'user_count': user_count,
        'company_count': company_count,
    }
    
    return render(request, 'usertypecount.html', context)




from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        # Extract updated data from the request
        name = request.POST.get('name')
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        price_per_day = request.POST.get('price_per_day')
        category = request.POST.get('category')
        availability = request.POST.get('availability')
        image = request.FILES.get('image')

        try:
            if rating is not None:
                rating = Decimal(rating)
            if price_per_day is not None:
                price_per_day = Decimal(price_per_day)
        except (InvalidOperation, TypeError, ValueError):
            return render(request, 'error.html', {'message': 'Invalid input for rating or price.'})

        # Update the product model with the new data
        product.name = name
        product.description = description
        product.rating = rating if rating is not None else Decimal('0')
        product.price_per_day = price_per_day if price_per_day is not None else Decimal('0')
        product.category = category
        product.availability = availability
        if image:
            product.image = image

        # Save the updated product
        product.save()
        return redirect('admindash')
    
    return render(request, 'edit_product.html', {'product': product})




from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('admindash')

    return render(request, 'delete_product.html', {'product': product})





@login_required
def account(request):
    if request.method == 'POST':
        # Get the current user
        user = request.user

        # Update user's profile data with the new values from the form
        user.first_name = request.POST['first-name']
        user.last_name = request.POST['last-name']
        user.username = request.POST['username']
        user.email = request.POST['email']

        # Additional fields like phone number and address can be saved in a separate user profile model
        user_profile = user.userprofile
        user_profile.phone_number = request.POST['phone-number']
        user_profile.address = request.POST['address']

        user.save()
        user_profile.save()

        return redirect('account')  # Redirect to the profile view after saving changes

    # If it's a GET request, pre-fill the form fields with the current user's data
    user = request.user
    user_profile = user.userprofile
    context = {
        'user': user,
        'user_profile': user_profile
    }
    return render(request, 'account.html', context)
