def get_unicode(text):
    """
        Recebe uma string e retorna um array de unicode
    """
    return [ord(c) for c in text]

def format_to_hex(value):
    """
        Recebe um valor inteiro e retorna uma string com o valor em hexadecimal
    """
    return hex(value)[2:].upper().zfill(2)