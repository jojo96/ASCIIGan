import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from numpy import load
from numpy import expand_dims
from matplotlib import pyplot
from PIL import Image
import numpy as np

st.write("Generate ASCII images using GAN")

uploaded_file = st.file_uploader("Choose an image...")

def load_image(filename, size=(512,512)):
	# load image with the preferred size
	pixels = load_img(filename, target_size=size)
	# convert to numpy array
	pixels = img_to_array(pixels)
	# scale from [0,255] to [-1,1]
	pixels = (pixels - 127.5) / 127.5
	# reshape to 1 sample
	pixels = expand_dims(pixels, 0)
	return pixels

if uploaded_file is not None:
    #src_image = load_image(uploaded_file)
    image = Image.open(uploaded_file)	
    model = load_model('./model_012000.h5')
    gen_image = model.predict(image)
    gen_image = (gen_image + 1) / 2.0

    im = Image.fromarray((gen_image[0]* 255).astype(np.uint8))
    st.image(uploaded_file, caption='ASCII Art', use_column_width=True)
    
    st.image(im, caption='ASCII Art', use_column_width=True)
    
