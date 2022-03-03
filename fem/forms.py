from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

GENDER = (
    ("MALE", 'MALE'),
    ("FEMALE", 'FEMALE')
)

YEAR = (
    (1, '1st Year'),
    (2, '2nd Year'),
    (3, '3rd Year'),
    (4, '4th Year'),
    (5, '5th Year')
)

BRANCH = (
    ("CSE", 'CSE'),
    ("ECE", 'ECE'),
    ("ECM", 'ECM'),
    ("BBA", 'BBA'),
    ("EEE", 'EEE'),
    ("BCA", 'BCA'),
    ("LAW", 'LAW'),
    ("MBA", 'MBA'),
    ("MECH", 'MECH'),
    ("CIVIL", 'CIVIL'),
    ("CSIT", 'CSIT'),
    ("BT", 'BT'),
    ("AI&DS", 'AI&DS'),
    ("HOTEL MANG.", 'HOTEL MANG.'),
    ("FINE ARTS", 'FINE ARTS'),
    ("ARCH.T", 'ARCH.T'),
    ("OTHER", 'OTHER')
)

COLLEGE = (
    ("College name", 'College name'),
    ("KL Vijayawada", 'KL Vijayawada'),
    ("KL Hyderabad", 'KL Hyderabad'),
    ("Other", 'Other'),
)


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter College Id', 'id': 'username'}
                                                      ), required=True, max_length=50)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter First Name', 'id': 'first_name'}
                               ), required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'id': 'last_name'}
                                                       ), required=True, max_length=50)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Personal Email', 'id': 'email'}
                                                    ), required=True, max_length=50)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'id': 'password1'}
                                   ), required=True, max_length=50)
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Confirm Password', 'id': 'password2'}
                                   ), required=True, max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'id': 'phone', 'placeholder': 'Enter Phone Number'}
                                                   ), required=True, max_length=10, min_length=10)
    college_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter College Name', 'id': 'college_name'}), required=True)
    branch = forms.CharField(widget=forms.Select(choices=BRANCH, attrs={'id': 'branch'}), required=True)
    college = forms.CharField(widget=forms.Select(choices=COLLEGE, attrs={'id': 'college', 'onChange': 'myFun()'}),
                              required=True)
    year_of_study = forms.CharField(widget=forms.Select(choices=YEAR, attrs={'id': 'year_of_study'}), required=True)
    gender = forms.CharField(widget=forms.Select(choices=GENDER, attrs={'id': 'gender'}), required=True)
    send_otp = forms.CharField(widget=forms.TextInput(attrs={'id': 'otp', 'placeholder': 'Enter OTP'}), required=True, max_length=4)

    class Meta:
        model = Profile
        fields = ['phone', 'college_name', 'branch', 'year_of_study', 'gender']