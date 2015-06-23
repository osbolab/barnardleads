import phonenumbers


def format_phone(phone):
    if phone:
        return phonenumbers.format_number(phonenumbers.parse(phone.strip(), 'US'), phonenumbers.PhoneNumberFormat.NATIONAL)
    else:
        return ''


def generify_phone_search(search_term):
    try:
        phone_number = phonenumbers.parse(search_term.strip(), 'US')
        if phonenumbers.is_possible_number(phone_number):
            return phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    except phonenumbers.NumberParseException:
        return search_term