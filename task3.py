import re

def normalize_phone(phone):
    r = r'\D'
    cleaned_phone = re.sub(r,'',phone)

    FULL_NUMBER_LEN = 12
    WITHOUD_CODE_LEN = 10

    if(cleaned_phone.startswith('380') and len(cleaned_phone) == FULL_NUMBER_LEN):
        return f'+{cleaned_phone}'
    elif len(cleaned_phone) == WITHOUD_CODE_LEN:
        return f"+38{cleaned_phone}"
    raise ValueError("Invalid phone number")


# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)