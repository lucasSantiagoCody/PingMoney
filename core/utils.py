from importlib import import_module
import os


def get_model(app_label:str, model:str):
    """
        app_label (str): The App's name in string
        model (str):  The Model's name in string

        >>>
            class Doctor(models.Model):
                ...

            get_model(app_label='app's name', 'Doctor')
        >>

    """

    try:
        # importing model module
        model_module = import_module(f"{app_label}.models")
        # getting model from model_module
        model_class = getattr(model_module, model)
        return model_class
    except:
        return None

def get_choice_in_field_choices(app_label:str, model:str, choice_field:str, choice_string:str):
    """
        choice_field (str) is the model class field 
        that has the choices options
        choice_string (str) choosed choice to save in database
    """

    model_class = get_model(app_label, model)
    choices_options = model_class._meta.get_field(choice_field).choices
    choice_value = None

    for choice_option in choices_options:
        if choice_string == choice_option[1]:
            choice_value = choice_option[0]
    if choice_value:
        return choice_value
        
    return None