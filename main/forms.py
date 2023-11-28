from django import forms
from .models import User, Client, Response


class AuthUserForm(forms.Form):
    """
    Form for authenticating users.

    Attributes:
        login (CharField): The field for entering the username.
        password1 (CharField): The field for entering the password.
    """

    login = forms.CharField(max_length=255)
    password1 = forms.CharField(max_length=255)


    def __init__(self, *args, **kwargs):
        """
        Constructor for AuthUserForm.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        super().__init__(*args, **kwargs)


class UserForm(forms.ModelForm):
    """
    Form for creating or updating User model instances.

    Meta:
        model (User): The User model to use for this form.
        fields (list): The fields to include in the form.
    """

    class Meta:
        model = User
        fields = ['name', 'surname', 'password1', 'password2', 'country', 'email', 'phone']


class ClientForm(forms.ModelForm):
    """
    Form for creating or updating Client model instances.

    Meta:
        model (Client): The Client model to use for this form.
        fields (list): The fields to include in the form.
    """

    class Meta:
        model = Client
        fields = ['user_name', 'name', 'email', 'bucket']


class ResponseForm(forms.ModelForm):
    """
    Form for creating or updating Response model instances.

    Meta:
        model (Response): The Response model to use for this form.
        fields (str): A special value that indicates all fields in the model should be used.
    """

    class Meta:
        model = Response
        fields = '__all__'
