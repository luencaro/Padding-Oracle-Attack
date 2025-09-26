
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

BLOCK = 16

class VulnerableServer:
    """
    Simula un servicio que:
    - encrypt(m) -> IV || C
    - decrypt(data) -> True/False segun padding PKCS#7. Este
      comportamiento es vulnerable y NO debe usarse en produccion
    """
    def __init__(self):
        self.key = get_random_bytes(BLOCK)

    def encrypt(self, plaintext: bytes) -> bytes:
        iv = get_random_bytes(BLOCK)
        padded = pad(plaintext, BLOCK)
        c = AES.new(self.key, AES.MODE_CBC, iv).encrypt(padded)
        return iv + c  # IV || C

    def decrypt(self, data: bytes) -> bool:
        """
        Devuelve True si el padding del ultimo bloque descifrado es valido;
        False de lo contrario. data debe tener >= 2 bloques y longitud multiplo de 16.
        """
        try:
            if len(data) < 2*BLOCK or (len(data) % BLOCK != 0):
                return False
            blocks = [data[i:i+BLOCK] for i in range(0, len(data), BLOCK)]
            iv, cblocks = blocks[0], blocks[1:]
            pt = AES.new(self.key, AES.MODE_CBC, iv).decrypt(b"".join(cblocks))
            _ = unpad(pt, BLOCK)  # ValueError si padding incorrecto
            return True
        except ValueError:
            return False