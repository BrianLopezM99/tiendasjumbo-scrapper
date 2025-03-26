# Jumbo Scraper API

Este proyecto es una API desarrollada en Python para hacer scraping de la web de [Tiendas Jumbo](https://www.tiendasjumbo.co) y obtener información de productos.

## Descripción

La API proporciona un único endpoint que recibe una URL como entrada y retorna un JSON con los primeros 15 productos encontrados en la página, incluyendo su nombre, precio y precio promocional (si aplica).

## Endpoints

### 1. Verificar si la API está viva
- **GET** `http://127.0.0.1:5000/`
- Respuesta: `La API está funcionando correctamente.`

### 2. Obtener datos de productos
- **POST** `http://127.0.0.1:5000/get_data_from_url`
- **Header:** `Content-Type: application/json`
- **Body:**
  ```json
  {
    "url": "https://www.jumbocolombia.com/supermercado/despensa/aceite"
  }
  ```
- **Respuesta:**
  ```json
  {
    "url": "https://www.jumbocolombia.com/...",
    "products": [
      {
        "name": "Atún En Aceite Van Camps x 160g x 4und",
        "price": "$ 25.492",
        "promo_price": "$ 20.392"
      },
      {
        "name": "Atún En Aceite Van Camps x 160g x 4und",
        "price": "$ 25.492",
        "promo_price": "$ 20.392"
      }
    ]
  }
  ```

## Cómo Ejecutar

1. Clona el repositorio:
    ```bash
    git clone https://github.com/BrianLopezM99/tiendasjumbo-scrapper.git
    cd tiendasjumbo-scrapper
    ```
2. Construye la imagen de Docker:
    ```bash
    docker build -t tiendasjumbo-scrapper .
    ```
3. Ejecuta el contenedor:
    ```bash
    docker run -p 5000:5000 tiendasjumbo-scrapper
    ```
4. Verifica que la API está activa:
    ```bash
    curl http://127.0.0.1:5000/
    ```

## Notas
- Este proyecto utiliza `Flask` y `Playwright` para realizar el scraping y levantar el servicio.
- Asegúrate de que la URL enviada como parámetro sea válida y provenga del dominio `https://www.tiendasjumbo.co/`.

## Licencia
Este proyecto está licenciado bajo la [MIT License](LICENSE).

