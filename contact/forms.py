from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Escreva aqui 3",
            },
        ),
        label="Primeiro Nome",
        help_text="Texto de ajuda para o seu usuário",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields["first_name"].widget.attrs.update(
        #     {
        #         "placeholder": "Escreva aqui",
        #     }
        # )

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "category",
        )
        # widgets = {
        #     "first_name": forms.TextInput(
        #         attrs={
        #             "placeholder": "Escreva aqui",
        #         }
        #     )
        # }

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
