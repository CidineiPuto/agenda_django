from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "accept": "image/*",
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "category",
            "picture",
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name == last_name:
            msg = ValidationError(
                "Primeiro nome não pode ser igual ao segundo.", code="invalid"
            )

            self.add_error("last_name", msg)
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        # self.add_error(
        #     "first_name",
        #     ValidationError(
        #         "Mensagem",
        #         code="invalid",
        #     ),
        # )
        return first_name


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            self.add_error(
                "email",
                ValidationError(
                    "E-mail already exist",
                    code="invalid",
                ),
            )

        return email


class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text="Required.",
        error_messages={"min_length": "Please, add more than 2 letters."},
    )
    last_name = forms.CharField(
        min_length=2, max_length=30, required=True, help_text="Required."
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="Use the same password as before.",
        required=False,
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    "email",
                    ValidationError(
                        "E-mail already exist",
                        code="invalid",
                    ),
                )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
        )
