# CLIENTES-APP (Cliente de Sockets en Python)

Aplicación cliente desarrollada en **Python** que utiliza sockets TCP para comunicarse con un servidor central, con soporte opcional para ejecución mediante contenedores **Docker**[cite: 2, 3, 4].

---

## Tabla de Contenidos
1. [Requisitos del Sistema](#-requisitos-del-sistema)
2. [Estructura del Proyecto](#-структура-del-proyecto)
3. [Parámetros de Ejecución (IP y Puerto)](#-parámetros-de-ejecución-ip-y-puerto)
4. [Instrucciones de Despliegue y Uso](#-instrucciones-de-despliegue-y-uso)
   - [Despliegue Local](#1-despliegue-local)
   - [Despliegue con Docker](#2-despliegue-con-docker)

---

## 1. Requisitos del Sistema
* **Python** (versión 3.12)[cite: 4].
* **Docker** (opcional, para entornos contenedorizados)[cite: 4].
* Conexión de red local o accesibilidad al servidor destino.

---

## 2. Estructura del Proyecto
* `client.py`: Script principal del cliente para la conexión por sockets y envío de tramas de datos[cite: 2].
* `copia.py`: Versión alternativa o de respaldo del script cliente[cite: 3].
* `Dockerfile`: Configuración para empaquetar el entorno de ejecución en Python 3.2-slim[cite: 4].

---

## 3. Parámetros de Ejecución (IP y Puerto)

El sistema de comunicación utiliza los siguientes parámetros predeterminados de red, los cuales se pueden configurar mediante argumentos de la terminal:

* **IP del Servidor (`SERVER_HOST`):** 
  * Por defecto: `127.0.0.1` (localhost)
  * Se recibe como el **primer argumento** (`sys.argv[1]`)[cite: 2, 3].
* **Puerto del Servidor (`SERVER_PORT`):** 
  * Fijo en el código: `5000`[cite: 2, 3]
* **Identificador del Nodo / Cliente (`client_name`):** 
  * Se recibe como el **segundo argumento** (`sys.argv[2]`)[cite: 2, 3]. Por defecto es `"Cliente"`[cite: 2, 3].

---

## 4. Instrucciones de Despliegue y Uso

### 1. Despliegue Local
Abre una terminal en la ruta de tu proyecto en Visual Studio Code y ejecuta el script pasando opcionalmente la IP del servidor y el nombre del nodo:

```bash
# Sintaxis general: python client.py <IP_SERVIDOR> <NOMBRE_CLIENTE>
python client.py 127.0.0.1 Nodo-01