import secrets
import string

def gerar_senha_segura(comprimento=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for i in range(comprimento))
    return senha

senha_segura = gerar_senha_segura(12)
print(f"Senha Gerada: {senha_segura}")