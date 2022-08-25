'''
justify.py
Justifica texto dependiendo del ancho ingresado, distribuyendo los espacios.

Raul Juarez
raul.jrz@gmail.com
011 1534426513
'''
import re, textwrap

def items_len(l):
    return sum([ len(x) for x in l] )

lead_regularExpression = re.compile(r'(^\s+)(.*)$')

def justify_line(the_line, width, is_last_paragraph_line=0):
    # detect and save leading whitespace
    m = lead_regularExpression.match(the_line)
    if m is None:
        left, right, nWidth = '', the_line, width
    else:
        left, right, nWidth = m.group(1), m.group(2), width - len(m.group(1))

    items = right.split()
    # add required space to each words, exclude last item
    for loop in range(len(items) - 1):
        items[loop] += ' '

    if not is_last_paragraph_line:
        # number of spaces to add
        left_count = nWidth - items_len(items)
        while left_count > 0 and len(items) > 1:
            for loop in range(len(items) - 1):
                items[loop] += ' '
                left_count -= 1
                if left_count < 1:
                    break

    response = left + ''.join(items)
    return response

# Principal
def justify(paragraph, width, debug=0):
    lines = list()
    if type(paragraph) == type(lines):
        lines.extend(paragraph)
    elif type(paragraph) == type(''):
        lines.append(paragraph)
    elif type(paragraph) == type(tuple()):
        lines.extend(list(paragraph))
    else:
        raise('Tipo no soportado: '+type(paragraph))

    prepared_paragraph = ' '.join(lines)

    splitted = textwrap.wrap(prepared_paragraph, width)
    if debug:
        print(f"Texto acotado al ancho de {width} caracteres, sin espacios.")
        print('\n%s\n' % '\n'.join(splitted))

    justify_text = list()
    justify_text = ''
    while len(splitted) > 0:
        line = splitted.pop(0)
        if len(splitted) == 0:
            is_last_paragraph_line = 1
        else:
            is_last_paragraph_line = 0
        text_with_space = justify_line(line, width, is_last_paragraph_line)
        justify_text += "\n"+ text_with_space
#        justify_text.append(text_with_space)

    return justify_text


if __name__ == '__main__':
    input ='La historia de la ópera tiene   una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera.' 

    output = justify(input, width=30, debug=0)
    print(output)
#   print('\n%s\n' % '\n'.join(output))

