from django import template
from datetime import datetime

register = template.Library()

@register.filter
def l2l_dt(value):
    # Filter receives a date object or a string. If a string is received
    # it will be in the following format: "%Y-%m-%dT%H:%M:%S" 

    # Filter returns the date in this format: "%Y-%m-%d %H:%M:%S"
    # Result will appear similiar to "2024-06-25 11:10:32"

    time_format = "%Y-%m-%d %H:%M:%S"
    return_value = None

    if (not type(value) is str) and (not type(value) is datetime):
        # Value to be filtered must be a string or a datetime object
        raise TypeError("Only datetime objects or strings permitted")

    if type(value) is str:
        # Convert string to datetime object before converting back to string in 
        # desired format
        try:
            return_value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
        except ValueError as err:
            raise ValueError(f"Error converting '{value}' to datetime with format '%Y-%m-%dT%H:%M:%S': {err}")
    else:
        # Value is already a datetime object, leave as is
        return_value = value

    # Format datetime object to string in desired format
    formatted_date_time = return_value.strftime(time_format)

    return formatted_date_time