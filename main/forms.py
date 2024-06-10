from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form__input',
        'placeholder': 'Имя',
        'required': 'required'
    }))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': 'form__input',
        'placeholder': '+ (   ) -- -- -- --',
        'required': 'required'
    }))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form__input',
        'placeholder': 'Город',
        'required': 'required'
    }))




class BigContactForm(forms.Form):

    house_area = forms.CharField(max_length=10,widget=forms.TextInput(attrs={
        'class' : 'form-quistions__input',
        'placeholder' : ".....м²",
        'required' : 'required',
    }))

    floors = forms.ChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4+')],
        widget=forms.RadioSelect(attrs={
            'class': 'form-quistions__checkbox',
        })
    )

    MATERIAL_CHOICES = [
        ('brick', 'Кирпич'),
        ('tree', 'Дерево'),
        ('gas-block', 'Газоблок'),
        ('other', 'Другое'),
    ]
    
    materials = forms.MultipleChoiceField(
        choices=MATERIAL_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-quistions__checkbox form-quistions__checkbox--base'
        })
    )
    
    house_height = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-quistions__input',
            'placeholder': '0-9 м',
            'required': 'required'
        })
    )

    # Вопрос 1: Отделка фасадов
    FACING_CHOICES = [
        ('facing-brick', 'Кирпич облицовочный'),
        ('tree', 'Дерево'),
        ('decorative-plaster', 'Декоративная штукатурка'),
        ('other', 'Другое'),
    ]
    
    facades = forms.MultipleChoiceField(
        choices=FACING_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-quistions__checkbox form-quistions__checkbox--base'
        })
    )
    
    # Вопрос 2: Фундамент
    FOUNDATION_CHOICES = [
        ('tape', 'Ленточный'),
        ('monolithic-slab', 'Монолитная плита'),
        ('belt-drill', 'Ленточный бурозабивной'),
        ('screw', 'Винтовой'),
    ]
    
    foundation = forms.MultipleChoiceField(
        choices=FOUNDATION_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-quistions__checkbox form-quistions__checkbox--base'
        })
    )

    # Вопрос о гараже, бане, терассе и бассейне
    GARAGE_CHOICES = [
        ('in-house', 'В доме'),
        ('open-parking', 'Открытая парковка'),
        ('not-needed', 'Не нужен'),
        ('separately', 'Отдельно'),
        ('parking-with-canopy', 'Парковка с навесом'),
    ]

    BATH_CHOICES = [
        ('bath-in-house', 'В доме'),
        ('bath-no', 'Не нужна'),
        ('bath-separately', 'Отдельно'),
    ]
    
    TERRACE_CHOICES = [
        ('terrace-with-house', 'Слита с домом'),
        ('terrace-separately', 'Отдельно от дома'),
    ]
    
    POOL_CHOICES = [
        ('pool-in-house', 'В доме'),
        ('pool-close-street', 'На улице крытый'),
        ('pool-open-street', 'На улице открытый'),
        ('pool-no', 'Не нужен'),
    ]

    garage = forms.MultipleChoiceField(
        choices=GARAGE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-quistions__checkbox form-quistions__checkbox--base'})
    )

    bath = forms.MultipleChoiceField(
        choices=BATH_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-quistions__checkbox form-quistions__checkbox--base'})
    )
    
    terrace = forms.MultipleChoiceField(
        choices=TERRACE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-quistions__checkbox form-quistions__checkbox--base'})
    )

    pool = forms.MultipleChoiceField(
        choices=POOL_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-quistions__checkbox form-quistions__checkbox--base'})
    )

    land_area = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-quistions__input',
            'placeholder': '0-999 соток',
            'required': 'required'
        }),
        min_value=0,
        max_value=999,
        label='Предполагаемая площадь земельного участка (соток)'
    )


    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form__input',
            'placeholder': 'Имя',
            'autocomplete': 'off',
            'required': 'required'
        }),
        max_length=100,
        label=''
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form__input',
            'placeholder': '+ (   ) -- -- -- --',
            'autocomplete': 'off',
            'required': 'required'
        }),
        max_length=20,
        label=''
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form__input',
            'placeholder': 'E-mail',
            'autocomplete': 'off',
            'required': 'required'
        }),
        max_length=100,
        label=''
    )