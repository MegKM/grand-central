# def add_photo(request, foodmenuitem_id):
#     foodmenuitem = FoodMenuItem.objects.get(pk=foodmenuitem_id)
#     photo_file = request.FILES.get('photo-file', None)
#     if photo_file:
#         s3 = boto3.client('s3')
#         key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
#         print(key)
#         try:
#             bucket = os.environ['S3_BUCKET']
#             s3.upload_fileobj(photo_file, bucket, key)
#             url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
#             FoodPhoto.objects.create(url=url, food=foodmenuitem, name=foodmenuitem)
#         except Exception as e:
#             print('An error occurred uploading file to S3')
#             print(e)
#     return redirect('food_menu_item_detail', pk=foodmenuitem_id)

# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#         user_form = UserCreationForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form = user_form.save()
#             profile_form.save()
#             login(request, user_form)
#             return redirect('home')
#         else:
#             if 'username' in user_form.errors:
#                 username_errors = user_form.errors['username']
#                 if 'This field may only contain letters, numbers, and @/./+/-/_ characters.' in username_errors:
#                     error_message = 'Invalid characters in username. Please use only letters, numbers, and @/./+/-/_ characters.'
#                 elif 'A user with that username already exists.' in username_errors:
#                     error_message = 'Username is already taken. Please choose a different one.'
#                 else:
#                     error_message = 'Invalid username. Please choose a different one.'
#             elif 'password1' in user_form.errors or 'password2' in user_form.errors:
#                 error_message = 'Invalid password - passwords do not match or are weak.'
#             else:
#                 error_message = 'Invalid sign up - try again'
#     user_form = UserCreationForm()
#     profile_form = ProfileForm()
#     context = {
#         'user_form': user_form, 
#         'profile_form': profile_form,
#         'error_message': error_message}
#     return render(request, 'registration/signup.html', context)

def add_size_price(self):
    total_price = self.price
    for size_option in self.size_option.all():
        if size_option.price > 0:
            total_price += size_option.price
            return total_price
        else:
            return total_price

SIDES_OPTIONS = (
    ('CO', 'Chips only'),
    ('SO', 'Salad only'),
    ('VO', 'Vegtables only'),
    ('CS', 'Chips & Salad'),
    ('CV', 'Chips & Vegetables'),
    ('SR', 'Steamed Rice'),
    ('BB', 'Baked Beans'),
    ('SP', 'Spaghetti')
)

ADDED_OPTIONS = (
    ('AC', 'Add chicken'),
    ('AB', 'Add bacon'),
    ('AA', 'Add chips'),
    ('CS', 'Add chips and salad'),
    ('CV', 'Add chips and vegtables'),
)
SIZE_OPTIONS = (
    ('SM', 'Small'),
    ('LG', 'Large'),
    ('HA', 'Half'),
    ('FU', 'Full')
)
GRAVY_OPTIONS = (
    ('PG', 'Pepper Gravy'),
    ('MG', 'Mushroom Gravy'),
    ('GR', 'Gravy')
)
COOK_OPTIONS = (
    ('PE', 'Poached Eggs'),
    ('FE', 'Fried Eggs'),
    ('SE', 'Scrambled Eggs'),
    ('GF', 'Grilled Fish'),
    ('FF', 'Fried Fish')
)
SAUCE_OPTIONS = (
    ('SC', 'Sweet chilli'),
    ('SM', 'Spicy Mayo'),
    ('DM', 'Dijon Mustard'),
    ('TS', 'Tomato Sauce')
)
REMOVABLE_OPTIONS = (
    ('EG', 'Egg'),
    ('BE', 'Beetroot'),
    ('ON', 'Onion'),
    ('LE', 'Lettuce'),
    ('CO', 'Coleslaw'),
)

# class Customer(AbstractUser):
#     class Role(models.TextChoices):
#         GUEST = "GUEST", 'Guest'
#         USER = "USER", 'User'

#     base_role = Role.USER

#     role = models.CharField(max_length = 50, choices = Role.choices)

#     def save(self, *args, **kwargs):
#         if not self.pk: 
#             self.role = self.base_role
#             return super().save(*args, **kwargs)

# class UserCreationForm(UserCreationForm):
#     email = EmailField(label=_("Email address"), required=False, 
#         help_text=_("Enter email to hear about upcoming events."))

#     class Meta:
#         model = User
#         fields = ("first_name", "last_name" "email", "password1", "password2")

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user