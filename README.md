# Detección de armas de fuego implementando Transfer Learning con YOLOv8: Sistema de Monitoreo Inteligente HawkAI

Este proyecto es un repositorio de código abierto que muestra una integración completa entre la detección y seguimiento de armas mediante el algoritmo de detección de objetos **YOLOv8** y **Streamlit**, un popular marco de aplicación web en Python para crear aplicaciones web interactivas. La iniciativa ofrece una interfaz amigable y personalizable que permite detectar y seguir armas en tiempo real dentro de transmisiones de video en vivo.

## HawkAI

![](https://github.com/robinsonrdms/guns_recognition/blob/main/Imagenes/HawkAi.png)



![](https://github.com/robinsonrdms/guns_recognition/blob/main/Imagenes/Gun_detection.jpeg)

## Requisitos

Python 3.10.8+
YOLOv8
best700
Streamlit

```bash
pip install ultralytics streamlit pafy
```

## Archivos

- Directorio Imágenes: Logo del Sistema y muestras de detección.
- Directorio TrainerNotebook: Archivo Proyecto.ipynb con código de entrenamiento y validación utilizado en Google Colab.
- Directorio Arquitecture: Esquemas de arquitectura del sistema.
- Directorio yolov8-streamlit-detection-tracking-master:
    app.py: Aplicación principal para ejecución.
    config.toml: Archivo de tema (Dark).
    exec.ipynb: Notebook para ejecución.
    helper.py: Librerías auxiliares.
    settings.py: Configuraciones.
    Directorio assets: Archivos requeridos por el frontend.
    Directorio images: Imágenes requeridas por el frontend.

## Instalación

- Clona el repositorio: git clone <https://github.com/robinsonrdms/guns_recognition.git>
- Cambiar al directorio del repositorio: `cd guns_recognition`
- Crear directorios `weights`, `videos` e `images` dentro del proyecto.
- Descargue los pesos YOLOv8 preentrenados desde (<https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt>) y guárdelos en el directorio `weights` en el mismo proyecto.
- Descargue los pesos best700 preentrenados desde (<https://drive.google.com/file/d/1a-GQIM1YYebr040aMaMtXOc6fvbNXaVw/view?usp=drive_link>) y guárdelos en el directorio `weights` en el mismo proyecto.
- Descargue los datasets desde (https://universe.roboflow.com/mcd-fz7gc/gundetectionmcd)


## Uso

- Ejecute la aplicación con el siguiente comando: `streamlit run app.py`
- La aplicación debería abrirse en una nueva ventana del navegador.

![](https://github.com/robinsonrdms/guns_recognition/blob/main/Imagenes/Front-End.JPG)

### Configuración del modelo Deep Learning

-  Escoger la tarea a realizar, que para este desarrollo solo podra ser "Detección" de objetos.
-  Elegir la confianza del modelo, es decir, el nivel de certeza necesario para considerar que un objeto ha sido detectado correctamente.
-  Utilizar un control deslizante para ajustar el umbral de confianza, con valores permitidos entre 25 y 100, según las preferencias del usuario.
-  Una vez configurado el modelo, seleccionar una fuente de datos para aplicar la detección de objetos.

Una vez realizada la configuración del modelo, seleccione una fuente.

### Detección en imágenes

-  La imagen predeterminada con su imagen de objetos detectados se muestra en la página principal.
-   Seleccione una fuente. (selección de botón de opción `Images`).
-   Sube una imagen haciendo clic en el botón "Browse files".
-   Haga clic en el botón "Detect objects" para ejecutar el algoritmo de detección de objetos en la imagen cargada con el umbral de confianza seleccionado.
-   La imagen resultante con los objetos detectados se mostrará en la página. Haga clic derecho sobre la imagen detectada y  selecciona "Guardar imagen como" para descargarla.

## Detección en videos

-   Crea una carpeta con el nombre `videos` en el mismo directorio
-  Aloja tus videos en esta carpeta
-  En `settings.py` edite las siguientes líneas.

```python
# video
VIDEO_DIR = ROOT / 'videos' # After creating the videos folder

# Suppose you have four videos inside videos folder
# Edit the name of video_1, 2, 3, 4 (with the names of your video files) 
VIDEO_1_PATH = VIDEO_DIR / 'video_1.mp4' 
VIDEO_2_PATH = VIDEO_DIR / 'video_2.mp4'
VIDEO_3_PATH = VIDEO_DIR / 'video_3.mp4'
VIDEO_4_PATH = VIDEO_DIR / 'video_4.mp4'

# Edit the same names here also.
VIDEOS_DICT = {
    'video_1': VIDEO_1_PATH,
    'video_2': VIDEO_2_PATH,
    'video_3': VIDEO_3_PATH,
    'video_4': VIDEO_4_PATH,
}

# Your videos will start appearing inside streamlit webapp 'Choose a video'.
```
- Haga clic en el botón 'Detect Video Objects' y la tarea seleccionada (detection) comenzará en el video seleccionado.

### Detección en RTSP

- Seleccione el botón de transmisión RTSP
- Ingrese la url rtsp dentro del cuadro de texto y presione el botón 'Detect Objects'

### Detección en URL de video de YouTube

- Seleccione la fuente como YouTube
- Copie y pegue la URL dentro del cuadro de texto.
- La tarea de detection comenzará en la URL del video de YouTube

## Agradecimientos

Esta aplicación se fundamenta en el potente algoritmo de detección de objetos YOLOv8, que puedes encontrar en el repositorio público en GitHub de Ultralytics (https://github.com/ultralytics/ultralytics). YOLOv8 es una versión avanzada de la serie YOLO (You Only Look Once), que ha demostrado un excelente desempeño en la detección rápida y precisa de objetos en imágenes y videos.

Para ofrecer una experiencia de usuario amigable y accesible, la aplicación ha sido desarrollada utilizando la biblioteca Streamlit, cuyo código fuente está disponible en GitHub (https://github.com/streamlit/streamlit). Streamlit es un marco de aplicación web en Python que se ha vuelto muy popular debido a su facilidad de uso y su capacidad para crear interfaces interactivas de manera sencilla.

### Descargo de responsabilidad

Es importante destacar que, dado que este proyecto tiene fines educativos, no está diseñado ni recomendado para su uso en entornos de producción. Si se desea llevar esta aplicación a un entorno de producción, se deben considerar y abordar algunos aspectos adicionales.

Es necesario realizar un proceso de optimización, seguridad y validación para garantizar un rendimiento confiable y seguro. Contar con un equipo de profesionales con experiencia en desarrollo web, seguridad informática y aprendizaje automático será crucial para llevar a cabo esta transición de manera exitosa.

**Estrella up ⭐ si te gusta este repositorio!**
