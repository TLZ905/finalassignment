import streamlit as st
import numpy as np
import pandas as pd

st.header("Final Assignment")
st.write(pd.DataFrame({
    'No': ['0', '1', '2'],
    'Species': ['Iris-sentosa', 'Iris-versicolor', 'Iris-virginica']
}))

from PIL import Image
image = Image.open('sunrise.jpg')

st.image(image, caption='Sunrise by the mountains')
