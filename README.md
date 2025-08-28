# 🔐 Secure Password Generator

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Un generador de contraseñas **seguras y aleatorias** hecho en **Python** 🐍.  

## 🚀 Funcionalidades
- Longitud configurable (por defecto 16).
- Incluir/excluir mayúsculas, números y símbolos.
- Uso directo desde la terminal.

## 📦 Instalación  

```bash
git clone https://github.com/nicosotomayor/secure-password-generator.git
cd secure-password-generator/src
```

## 💻 Uso  

Desde la carpeta `src/`, ejecuta:  

```bash
python main.py
```

## ⚙️ Opciones disponibles  
- `-l` o `--length` → definir la longitud de la contraseña (por defecto 16).  
- `-u` → incluir mayúsculas.  
- `-n` → incluir números.  
- `-s` → incluir símbolos.  

## 📋 Ejemplos  

1. Generar contraseña por defecto (16 caracteres):  
   ```bash
   python main.py
   ```

2. Generar contraseña de 24 caracteres con mayúsculas y números:  
   ```bash
   python main.py -l 24 -u -n
   ```

3. Generar contraseña de 32 caracteres con mayúsculas, números y símbolos:  
   ```bash
   python main.py -l 32 -u -n -s
   ```
   ```
