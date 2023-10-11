"""
    * Segurança da Informação - 2023.2
    * Implementação do algoritmo criptográfico RC4
    
    * O algoritmo consiste em realizar um XOR da mensagem original com uma chave, de modo que texto_cifrado = mensagem XOR chave
    * Dois algoritmos compõem o RC4:
        - KSA
        - PRGA
"""

from utils import get_unicode, format_to_hex

def KSA(T_box):
    """
        Key Scheduling Algorithm
        Recebe uma chave e retorna um vetor de permutação
    """
    # print(T_box)
    S_box = [i for i in range(256)]
    j = 0

    for i in range(256):
        j = (j + S_box[i] + T_box[i % len(T_box)]) % 256

        tmp = S_box[i]
        S_box[i] = S_box[j]
        S_box[j] = tmp

    # print(S_box)
    return S_box


def PRGA(S_box):
    """
        Pseudo-Random Generation Algorithm
        Recebe um vetor de permutação e retorna um gerador de números pseudo-aleatórios
    """
    i = 0
    j = 0

    while True:
        i = (i + 1) % 256
        j = (j + S_box[i]) % 256

        tmp = S_box[i]
        S_box[i] = S_box[j]
        S_box[j] = tmp

        K = S_box[(S_box[i] + S_box[j]) % 256]
        # print(K)
        yield K  

def RC4(key):
    """
        Recebe uma chave e retorna um gerador de números pseudo-aleatórios
    """
    S = KSA(key)
    return PRGA(S)


def encrypt(plainkey, message):
    """
        Recebe uma chave e uma mensagem e retorna a mensagem cifrada
    """
    text = get_unicode(message)
    T_box = get_unicode(plainkey)
    keystream = RC4(T_box)

    result = ""
    for c in text:
        result += format_to_hex(c ^ next(keystream))
    return result

def decrypt(plainkey, ciphertext):
    """
        Recebe uma chave e uma mensagem cifrada e retorna a mensagem original
    """
    key = get_unicode(plainkey)
    ciphertext = bytes.fromhex(ciphertext)
    keystream = RC4(key)

    result = ""
    for c in ciphertext:
        result += chr(c ^ next(keystream))
    return result

if __name__ == '__main__':
    choice = input("Você gostaria de Encriptar (E) ou Descriptar (D) uma mensagem? ")
    message = input("Digite a mensagem: ")
    key = input("Digite a chave: ")

    if choice == "E":
        print("Mensagem encriptada: ", encrypt(key, message))
    elif choice == "D":
        print("Mensagem descriptada: ", decrypt(key, message))
    else:
        print("Opção inválida")
