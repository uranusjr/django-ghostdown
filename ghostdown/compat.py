try:
    from django.template import Engine

    def get_template_from_string(s):
        return Engine().from_string(s)

except ImportError:
    # Old template loading private API in Django < 1.8.
    # Remove this when dropping 1.4 and 1.7 support.
    from django.template import loader

    def get_template_from_string(s):
        return loader.get_template_from_string(s)
