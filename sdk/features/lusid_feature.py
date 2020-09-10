def lusid_feature(feature_code):
    if type(feature_code) != str:
        raise ValueError("lusid_feature error: Decorator requires a string input parameter.")

    if feature_code == "":
        raise ValueError("lusid_feature error: Some decorated methods have no value passed. "
                         "Please make sure each lusid_feature decorator has a value code passed.")

    def wrap_method(decorated_method):
        def get_decorated_method(*decorated_method_args):
            return decorated_method(*decorated_method_args)
        get_decorated_method.decorator_value = feature_code  # <-- store the feature
        return get_decorated_method

    return wrap_method



