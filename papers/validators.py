from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def between_validator(min_val, max_val, allow_equal=True):
    def validator(value):
        if allow_equal:
            if not min_val <= value <= max_val:
                raise ValidationError(_('Ensure this value is less than or equal to %s '
                                      'and grater than or equal to %s.') % (min_val, max_val))
        elif not min_val < value < max_val:
            raise ValidationError(_('Ensure this value is less than %s '
                                  'and grater than %s.') % (min_val, max_val))

    return validator
