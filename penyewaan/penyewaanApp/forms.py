from django import forms
from . models import Penyewa,Pasar

class penyewaForm(forms.ModelForm):
    class Meta():
        model=Penyewa
        fields="__all__" 

        # STYLING FORM
        widgets={
            'tempat':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'nama':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'tipe':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'blok':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'nomor':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'limit':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'harga':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Rp.500.000',
                    # 'value':'1000'
                    
                    }
            ),
        }