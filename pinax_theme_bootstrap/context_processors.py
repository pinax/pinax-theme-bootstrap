from django.conf import settings

LAYOUT_SETTING = 'BOOTSTRAP_LAYOUT'
LAYOUT_CONTAINER_CLASSES = {
    'fixed': 'container',
    'fluid': 'container-fluid'
}
DEFAULT_LAYOUT = 'fixed'

def bootstrap_layout(request):
    """
    Set the bootstrap_container_class value in the template context based
    on the BOOTSTRAP_LAYOUT setting value:
        - fixed: container
        - fluid: container-fluid
    """
    layout = getattr(settings, LAYOUT_SETTING, DEFAULT_LAYOUT)
    try:
        bootstrap_container_class = LAYOUT_CONTAINER_CLASSES[layout]
    except KeyError:
        # An invalid value was provided
        raise ValueError(
            "'%s' is not a valid value for %s. Choices are: '%s'"
            % (layout, LAYOUT_SETTING, LAYOUT_CONTAINER_CLASSES.keys())
        )
    return {'bootstrap_container_class': bootstrap_container_class}