import tokenize

TWI101 = 'TWI101 Unsafe field removal. See http://twil.io/f8-field-removal'
DANGER_METHODS = ['RemoveField', 'RenameField']


def checker(physical_line, tokens):
    for danger_method in DANGER_METHODS:
        if danger_method in physical_line:
            for token_type, text, start, _, _ in tokens:
                if token_type == tokenize.NAME and text in DANGER_METHODS:
                    return (start[1], TWI101)


checker.name = 'deved_field_removal'
checker.version = '0.1.0'
