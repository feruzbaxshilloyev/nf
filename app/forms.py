from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import ContactMessage, Profile, User
from .models import Comment


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Kommentariya yozing...',
                'rows': 4,
                'class': 'form-control',
            }),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=False)
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address'],
                birth_date=self.cleaned_data['birth_date']
            )
        return user


class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = Profile
        fields = ['avatar', 'phone', 'address', 'birth_date']
