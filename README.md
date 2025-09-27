# **Padding Oracle Attack**

## *Desarrollado por Luis Cabarcas Romero (<lcabarcase@uninorte.edu.co>) y Ashley Mercado Defort (<agmercado@uninorte.edu.co>)*


# Padding Oracle Attack - AES-CBC

## Descripción
Implementación de un ataque de padding oracle contra AES-CBC con PKCS#7. Este laboratorio demuestra cómo explotar vulnerabilidades en el manejo de padding para recuperar texto plano sin conocer la clave de cifrado.

## Integrantes del Grupo
- **[Nombre Integrante 1]** - [ID/Email]
- **[Nombre Integrante 2]** - [ID/Email]

## Archivos del Proyecto
- `VulnerableServer.py` - Servidor vulnerable que simula el oracle de padding
- `Padding-Oracle-Attack.ipynb` - Implementación completa del ataque en Jupyter Notebook
- `informe.pdf` - Informe técnico detallado (2-3 páginas)

## Instalación
```bash
pip install pycryptodome
```

## Uso
```python
from VulnerableServer import VulnerableServer

# Crear servidor vulnerable
server = VulnerableServer()

# Cifrar mensaje
plaintext = b"Attack at dawn!!"
ciphertext = server.encrypt(plaintext)

# Ejecutar ataque
recovered = recover_message(server.decrypt, ciphertext)
print(f"Mensaje recuperado: {recovered}")
```

## Funciones Principales

### `recover_block(oracle, C_prev, C_curr)`
Recupera un bloque de texto plano usando el ataque padding oracle.
- **oracle**: función que retorna True/False según validez del padding
- **C_prev**: bloque anterior (16 bytes)
- **C_curr**: bloque a descifrar (16 bytes)
- **Retorna**: bloque de texto plano (16 bytes)

### `recover_message(oracle, ciphertext)`
Recupera el mensaje completo eliminando el padding PKCS#7.
- **oracle**: función de validación de padding
- **ciphertext**: mensaje cifrado completo (IV + bloques)
- **Retorna**: mensaje original sin padding

## Resultados
- **Eficiencia**: 96.2% del óptimo teórico
- **Tasa de éxito**: 75% (6/8 tests)
- **Consultas promedio**: 133 por byte (vs 128 teórico)
- **Rango por bloque**: 1512-2734 consultas

## Casos de Prueba
✅ Mensajes cortos y largos  
✅ Caracteres especiales  
✅ Patrones repetitivos  
❌ Algunos casos edge requieren análisis adicional  

## Tecnologías
- Python 3.10+
- PyCryptodome
- Jupyter Notebook
