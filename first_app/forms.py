from django import forms


class NewPlaceForm(forms.Form):
    name = forms.CharField(label="Назва місця", max_length=50, required=True)
    location = forms.CharField(label="Локація", max_length=50, required=False)
    description = forms.CharField(label="Опис", required=False)
    types = (
        ("1", "Поїсти"),
        ("2", "Розваги"),
        ("3", "Цікавий простір"),
        ("4", "Погуляти"),
    )
    type = forms.ChoiceField(label="Тип місця", choices=types, required=False)
    rating = forms.IntegerField(
        label="Рейтинг", required=True, min_value=1, max_value=5
    )
