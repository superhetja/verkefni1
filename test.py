email = 'alli.r@ru.is'

try:
    atsymble = email.index('@')
    dot = email.index('.', atsymble)
    print('Rétt')
except ValueError:
    print('Rangur innsláttur')