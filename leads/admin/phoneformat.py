import phonenumbers


def generify_phone_search(search_term):
    try:
        phone_number = phonenumbers.parse(search_term.strip(), 'US')
        if phonenumbers.is_possible_number(phone_number):
            return phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    except phonenumbers.NumberParseException:
        pass

    return search_term
