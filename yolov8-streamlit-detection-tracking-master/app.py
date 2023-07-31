import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# Python In-built packages
from pathlib import Path
import PIL

# External packages
import streamlit as st

# Local Modules
import settings
import helper


# Setting page layout
st.set_page_config(
    page_title="Gun Detection using YOLOv8",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Main page heading
st.title("Gun Detection using YOLOv8")

print("Modelo de detección")
print(settings.DETECTION_MODEL)

logo_path = str(settings.IMAGES_DIR / "logo2.png")
my_logo = helper.add_logo(logo_path=logo_path, width=300, height=70)
st.sidebar.image(my_logo)

# Sidebar
#st.sidebar.header("Deep Learning Model Config")
st.sidebar.header("Configuración")

# Model Options
#model_type = st.sidebar.radio(
    #"Select Task", ['Detection', 'Segmentation'])
#    "Seleccione la Tarea", ['Detección']
#    )

confidence = float(st.sidebar.slider(
    "Seleccione el \% de confianza", 25, 100, 40)) / 100

#helper.add_logo()

# Selecting Detection Or Segmentation
model_path = Path(settings.DETECTION_MODEL)
#if model_type == 'Detección':
#    model_path = Path(settings.DETECTION_MODEL)
#elif model_type == 'Segmentation':
#    model_path = Path(settings.SEGMENTATION_MODEL)


# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

#st.sidebar.header("Image/Video Config")
st.sidebar.header("Configuración de Imagen/Video")
source_radio = st.sidebar.radio(
    "Seleccione Fuente", settings.SOURCES_LIST)

st.markdown('<style>.ea3mdgi1{display:none}</style>', unsafe_allow_html=True)

source_img = None
# If image is selected
if source_radio == settings.IMAGE:
    source_img = st.sidebar.file_uploader(
        "Elegir Imagen...", type=("jpg", "jpeg", "png", 'bmp', 'webp')
    )

    col1, col2 = st.columns(2)

    with col1:
        try:
            if source_img is None:
                default_image_path = str(settings.DEFAULT_IMAGE)
                default_image = PIL.Image.open(default_image_path)
                st.image(default_image_path, caption="Image por Default",
                         use_column_width=True)
            else:
                uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="Imagen Cargada",
                         use_column_width=True)
        except Exception as ex:
            st.error("Error occurred while opening the image.")
            st.error(ex)

    with col2:
        if source_img is None:
            default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(
                default_detected_image_path)
            st.image(default_detected_image_path, caption='Imagen detectada',
                     use_column_width=True)
        else:
            if st.sidebar.button('Detect Objects'):
                res = model.predict(uploaded_image,
                                    conf=confidence
                                    )
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                st.image(res_plotted, caption='Detected Image',
                         use_column_width=True)
                try:
                    with st.expander("Detection Results"):
                        for box in boxes:
                            st.write(box.data)
                except Exception as ex:
                    # st.write(ex)
                    st.write("No image is uploaded yet!")

elif source_radio == settings.VIDEO:
    helper.play_stored_video(confidence, model)

elif source_radio == settings.WEBCAM:
    helper.play_webcam(confidence, model)

elif source_radio == settings.RTSP:
    helper.play_rtsp_stream(confidence, model)

elif source_radio == settings.YOUTUBE:
    helper.play_youtube_video(confidence, model)

else:
    st.error("Please select a valid source type!")
