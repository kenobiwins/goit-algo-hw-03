from datetime import datetime, date

str_pattern_format = '%Y-%m-%d'

def string_to_date(date_string: str)-> date:
    try:    
        return datetime.strptime(date_string, str_pattern_format).date()
    except ValueError:
        raise ValueError(f"Invalid date format: '{date_string}'. Expected format: YYYY-MM-DD")


def get_days_from_today(date_str: str)->int:
    try:
        date = string_to_date(date_str)
        today = datetime.today().date()
        delta = today - date

        return delta.days
    except ValueError as e:
        print(f"Error: {e}")
        return None  
