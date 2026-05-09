# 🎬 CineRecommender

Proyecto interactivo que combina **análisis de datos**, **procesos ETL** y una **aplicación web en Streamlit** para explorar un catálogo de películas, con datos enriquecidos provenientes de TMDB (The Movie Database).

Este repositorio te permite:
- Cargar y actualizar datos de películas desde una API externa hacia una base de datos.
- Explorar y analizar la información de las películas mediante **Notebooks de Jupyter**.
- Consultar, filtrar y visualizar los resultados en una interfaz web amigable.

---

## 📷 Interfaz y Funcionalidades visuales

La aplicación ofrece una experiencia visual completa e intuitiva para buscar y descubrir películas:

- **Filtros Dinámicos**: Permite filtrar el catálogo por **categoría** (género), un slider para el **rango de años**, y un selector múltiple de **idiomas**.
- **Ordenamiento Inteligente**: Puedes ordenar los resultados de forma rápida por **Popularidad**, **Rating** (calificación) o **Fecha de lanzamiento**.
- **Exploración por Tarjetas**: Los resultados se muestran en atractivas tarjetas con el póster de la película, año, idioma principal y calificación. Además, incluye un sistema ágil de **paginación** para navegar por todo el catálogo.
- **Modal de Información Detallada**: Al hacer clic en "Details", se despliega una ventana interactiva con información profunda que incluye:
  - Póster ampliado, calificación exacta, duración y año.
  - Sinopsis (Overview) y Director.
  - Etiquetas visuales con el Reparto principal (Cast) y los Géneros (Categories).
  - Datos financieros precisos como Presupuesto (Budget) y Recaudación (Revenue).

<img width="495" height="592" alt="image" src="https://github.com/user-attachments/assets/ca0cbdc1-02f1-436e-9702-40e4acf4985b" />
<img width="609" height="629" alt="image" src="https://github.com/user-attachments/assets/8b48ce90-76dc-4690-bb23-1aa30e979049" />

---

## ✨ Qué incluye

### 🖥️ App (Streamlit)
La aplicación principal se encuentra en [`app.py`](./app.py). Permite a los usuarios interactuar con el catálogo de películas, aplicar filtros de búsqueda y ver detalles sobre cada título mediante una interfaz visual intuitiva.

Componentes principales (organizados de forma modular):
- Interfaz gráfica: Carpeta `ui/`
- Servicios y lógica de negocio: Carpeta `services/`
- Consultas a la base de datos: Carpeta `database/`
- Utilidades adicionales: Carpeta `utils/`

### 🔄 ETL y Carga de Datos
El directorio `etl/` contiene los scripts necesarios para la obtención y actualización del catálogo de películas usando la API de TMDB.
- `initial_load.py`: Para hacer la primera ingesta masiva de datos hacia tu base de datos.
- `update_catalog.py`: Para mantener tu base de datos al día con las películas más recientes.

### 📊 Data Analytics (Notebooks)
En la carpeta `notebooks/` se incluye el análisis de datos del proyecto:
- `data_analitics.ipynb`: Ideal para entender la estructura de las tablas, realizar análisis exploratorio (EDA) de los datos y ver estadísticas clave sobre el catálogo.

---

## ⚙️ Configuración y Despliegue Local

Sigue estos pasos para levantar el proyecto en tu entorno local:

### 1. Requisitos previos e instalación
Clona este repositorio y asegúrate de instalar todas las dependencias necesarias:
```bash
pip install -r requirements.txt
```

### 2. Base de Datos y Variables de Entorno
Crea tu base de datos y configura las credenciales. Debes crear un archivo `.env` en la raíz del proyecto y agregar las siguientes variables:

```env
# URL de conexión a tu base de datos (por ejemplo, PostgreSQL)
DATABASE_URL=tu_url_de_base_de_datos

# Token de la API de TMDB (consíguelo en https://developer.themoviedb.org/)
TMDB_API_TOKEN=tu_token_de_tmdb
```

### 3. Carga Inicial de Datos
Antes de ejecutar la aplicación, debes poblar la base de datos ejecutando el script de carga inicial:
```bash
python etl/initial_load.py
```
*(Nota: Ajusta la ruta del script si se encuentra en el directorio raíz o dentro de `etl/`)*

### 4. Ejecutar la Aplicación
Inicia el servidor de Streamlit con el siguiente comando:
```bash
streamlit run app.py
```
La aplicación estará disponible en tu navegador en `http://localhost:8501`.

---

## 📈 Mantenimiento de Datos

Si en el futuro deseas agregar películas recientes al catálogo sin tener que hacer una carga inicial completa, simplemente ejecuta el script de actualización:
```bash
python etl/update_catalog.py
```

---

## 📁 Estructura del Proyecto

```text
.
├── .gitignore
├── app.py                  # Archivo principal de la aplicación Streamlit
├── requirements.txt        # Dependencias del proyecto
├── database/               # Módulos de conexión y consultas a la base de datos
├── etl/                    # Scripts de extracción, transformación y carga (initial_load, update_catalog)
├── notebooks/
│   └── data_analitics.ipynb # Análisis exploratorio y detalles de las tablas
├── services/               # Lógica de la aplicación y manejo de datos
├── ui/                     # Componentes visuales (filtros, modales, tarjetas)
└── utils/                  # Funciones de procesamiento auxiliares
```

---

## 🧑‍💻 Autor

**Ramón Emilio López**
- **GitHub:** [@Daniel20051601](https://github.com/Daniel20051601)
- **LinkedIn:** [ramón-emilio-lopez-57a833211](https://www.linkedin.com/in/ram%C3%B3n-emilio-lopez-57a833211/)
