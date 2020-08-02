from .models import Poll
from django.forms import ModelForm,TextInput
class CreatePollForm(ModelForm):
    class Meta:
        model=Poll
        fields=['question','option_one','option_two','option_three']
        widgets={'option_one' : TextInput(attrs={'class':"form-control",'placeholder':''}),
                'option_two' : TextInput(attrs={'class':"form-control",'placeholder':''}),
                'option_three' : TextInput(attrs={'class':"form-control",'placeholder':''}),
        }
