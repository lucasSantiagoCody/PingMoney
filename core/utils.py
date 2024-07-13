from importlib import import_module


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