from django import forms

from main.models import Reservation


class ReservationForm(forms.ModelForm):

    date = forms.DateField(input_formats=['%d/%m/%Y', '%d-%m-%Y', '%d.%m.%Y'],
                           widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'date',
                                                         'placeholder': 'dd.mm.yyyy', 'data-rule': 'minlen:4',
                                                         'data-msg': 'Please enter at least 4 chars' })
                           )

    def clean_name(self):
        name = self.data['name']
        return name.title()

    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'date', 'time', 'count', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Your Name',
                                           'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}),

            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'name': 'email',
                                             'placeholder': 'Your Email', 'data-rule': 'email',
                                             'data-msg': 'Please enter a valid email'}),

            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'Your Phone'}),

            'time': forms.TimeInput(attrs={'class': 'form-control', 'id': 'time', 'placeholder': 'Your Time' }),

            'count': forms.NumberInput(attrs={'class': 'form-control', 'id': "people", 'placeholder': "# of people", 'data-rule': "minlen:1", 'data-msg': "Please enter at least 1 chars"}),

            'message': forms.Textarea(attrs={'class': 'form-control', 'name': "message", 'rows': "5", 'placeholder': "Message"})
        }
