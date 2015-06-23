import phonenumbers


def format_phone(phone):
    if phone:
        return phonenumbers.format_number(phonenumbers.parse(phone.strip(), 'US'), phonenumbers.PhoneNumberFormat.NATIONAL)
    else:
        return ''