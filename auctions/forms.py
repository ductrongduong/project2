from django import forms

from .models import Category, Bid, Comment, Listing


# Model form for a new listing
class NewListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid','price_step', 'image', 'category', 'end_at']
        widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control'}),
                    'description': forms.Textarea(attrs={'rows':2, 'maxlength': 1000, 'class': 'form-control'}),
                    'starting_bid': forms.NumberInput(attrs={'class': 'form-control'}),
                    'price_step' : forms.NumberInput(attrs={'class': 'form-control'}),
                    'image': forms.URLInput(attrs={'class': 'form-control'}),
                    # 'photo' : forms.(attrs={'class': 'form-control'}),
                    # 'photo' : forms.ImageField(label='Company Logo',required=False, widget=forms.FileInput),
                    'category': forms.Select(attrs={'class': 'form-control'}),
                    'end_at': forms.DateTimeInput(attrs={'type': 'datetime-local'})
                    }
        labels = {
            'image': 'Image URL'
        }

# Model form for a new bid on a listing
class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
        widgets= {
            'amount': forms.NumberInput(attrs={'class': 'form-control'})
        }

# Model form for a new comment on a listing
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {
            'comment': ''
        }
        widgets = {"comment": forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'maxlength': '5000'})}

