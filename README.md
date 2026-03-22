# myCRYPTO

Aplicación web de registro de movimientos de criptomonedas desarrollada con Flask como proyecto final del Bootcamp "Aprender a programar desde cero" de KeepCoding usando Python, Flask, Sqlite, pico.css, la API de CoinMarketCap y control de errores con pytest

## Descripción

myCRYPTO permite registrar compras, ventas e intercambios de criptomonedas, consultando precios en tiempo real a través de la API de CoinMarketCap. La aplicación muestra un listado de movimientos, un formulario de compra/venta/tradeo y el estado actual de la inversión.

### Monedas soportadas

EUR, BTC, ETH, USDT, BNB, XRP, USDC, SOL, TRON, DOGE

## Instalación

### 1. Clonar el repositorio
```
git clone https://github.com/FerAguayo/proyecto_final.git
```

### 2. Crear y activar el entorno virtual
```
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Instalar dependencias
```
pip install -r requirements.txt
```

### 4. Crear el fichero .env

Crear un fichero `.env` en la raíz del proyecto con el siguiente contenido:
```
FLASK_APP=main.py
FLASK_DEBUG=True
COINMARKETCAP_API_KEY=tu-api-key-aqui
```

Puedes obtener una API key gratuita en: https://coinmarketcap.com/api/

### 5. Crear la base de datos
```
python create_db.py
```

### 6. Ejecutar la aplicación
```
flask run
```

La aplicación estará disponible en http://127.0.0.1:5000


## 7. Tests
Puedes correr los test y comprobar que todo funciona usando el comando 
```
pytest
```