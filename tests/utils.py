from tokenize import tokenize


def tokenize_and_invoke_checker(filename, checker_func):
    tokens = []

    with open(filename, 'rb') as f:
        tokens = list(tokenize(f.readline))

    # Remove ENCODING (line 0)
    while tokens[0].start[0] == 0:
        del tokens[0]

    # Separate tokens by individual, physical line
    lines = []
    current_line = []
    current_line_num = 1
    for token in tokens:
        if token.start[0] != current_line_num:
            lines.append(current_line)
            current_line = []
            current_line_num = token.start[0]
        current_line.append(token)
    lines.append(current_line)

    # Invoke the checker and collect output
    results = []
    for tokens in lines:
        result = checker_func(tokens[0].line, tokens)
        if result:
            results.append(f'{tokens[0].start[0]}:{result[0]}: {result[1]}')

    return results
