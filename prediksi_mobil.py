import pickle 
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav','rb'))

st.title('Estimasi Harga Mobil Bekas')

tahun = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
levy = st.number_input('Input tagihan pajak dll')
volumeengine = st.number_input('Input Cylinder mesin')

predict = ''

if st.button('Estimasi Harga') : 
    predict = model.predict(
        [[tahun, mileage, levy, volumeengine]]
    )
    st.write ('Perkiraan estimasi harga mobil bekas dalam Dollar : ', predict)