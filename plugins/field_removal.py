import tokenize

TWI101 = 'TWI101 Unsafe field removal. See http://twil.io/f8-field-removal'
DANGER_METHOD = 'RemoveField'


def checker(physical_line, tokens):
    if DANGER_METHOD not in physical_line:
        return

    for token_type, text, start, _, _ in tokens:
        if token_type == tokenize.NAME and text == DANGER_METHOD:
            return (start[1], TWI101)


checker.name = 'deved_field_removal'
checker.version = '0.1.0'
