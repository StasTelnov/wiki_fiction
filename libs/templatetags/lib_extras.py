from django import template
register = template.Library()


@register.filter
def attrs(field, attrs):
    attrs = attrs.replace(" ", "")
    res = {}

    for attr in attrs.split(','):
        attr = attr.split(':')
        res[attr[0]] = attr[1]

    return field.as_widget(attrs=res)


@register.filter
def add_class(field, classes):
    classes = classes + ' ' + field.field.widget.attrs.get('class', '')
    return field.as_widget(attrs={'class': classes})
