# Juego de Dados

Este repositorio contiene el código fuente para un juego de dados. El objetivo del juego es lanzar los dados y obtener la mayor puntuación posible.

## Requisitos

- Docker

## Instrucciones

1. Clona este repositorio en tu máquina local:
    ```sh
    git clone https://github.com/tu-usuario/juego-de-dados.git
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd juego-de-dados
    ```
3. Construye la imagen de Docker:
    ```sh
    docker build -t juego-de-dados .
    ```
4. Inicia un contenedor a partir de la imagen:
    ```sh
    docker run -p 8080:8080 juego-de-dados
    ```

El juego estará disponible en `http://localhost:8080`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.