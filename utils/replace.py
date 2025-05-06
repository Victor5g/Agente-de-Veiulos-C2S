import locale

def format_value_to_brl(value: float) -> str:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(value, grouping=True, symbol=None)