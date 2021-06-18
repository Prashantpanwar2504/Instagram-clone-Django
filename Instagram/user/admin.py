from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from authentication.forms import UserForm, CustomUserChangeForm

# Register your models here.

User = get_user_model()
# admin.site.register(User)


# Model Admin
class CustomUserAdmin(UserAdmin):
    # this add_form comes from this UserAdmin
    # now we need to tell the name of the form we want to use
    add_form = UserForm
    # create a form
    form = CustomUserChangeForm
    # now we need to tell for which model we are creating ModelAdmin
    model = User
    # creating the add_fieldsets
    add_fieldsets = (
        ('Personal Details', {'fields': ('email', 'full_name', 'username', 'picture', 'password1', 'password2')}),
        # fields we need to fill while creating user through admin panel
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Optional', {'fields': ('bio', 'website')}),

    )
    # Creating the fieldsets
    fieldsets = (
        ('Personal Details', {'fields': ('email', 'full_name', 'username', 'picture')}), # fields we want to show or change on admin panel
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Optional', {'fields': ('bio', 'website')}),

    )


# Now Register the Model Admin
admin.site.register(User, CustomUserAdmin)
