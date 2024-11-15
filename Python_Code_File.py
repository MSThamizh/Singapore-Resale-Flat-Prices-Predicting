import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Resale Flat Price Prediction
def predict_resale_flat_price(month,town,flat_type,storey_range,floor_area_sqm,flat_model,
                              lease_commence_date, year,remaining_lease_months):    
    with open("model.pkl","rb") as ft:
        ml = pickle.load(ft)
        user_data = {
        'month': [month],
        'town': [town],
        'flat_type': [flat_type],
        'storey_range': [storey_range],
        'floor_area_sqm': [floor_area_sqm],
        'flat_model': [flat_model],
        'lease_commence_date': [lease_commence_date],
        'year': [year],
        'remaining_lease_months': [remaining_lease_months]
        }
        user_df = pd.DataFrame(user_data)
        y_pred = ml.predict(user_df)

    return np.exp(y_pred[0])

# Straemlit Part
st.set_page_config(layout= "wide")
st.title(":blue[**SINGAPORE RESALE FLAT PRICES PREDICTING**]")
st.write("""This app uses a machine learning model to predict the resale price of HDB flats in Singapore 
         based on key features like Town, Flat Type, Storey Range, Floor Area, , Flat Model, 
         Remaining Lease and lease commence date.""")

month_options = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
year_options = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
town_options = {'ANG MO KIO': 0, 'BEDOK': 1, 'BISHAN': 2, 'BUKIT BATOK': 3, 'BUKIT MERAH': 4,
                     'BUKIT PANJANG': 5, 'BUKIT TIMAH': 6, 'CENTRAL AREA': 7, 'CHOA CHU KANG': 8,
                     'CLEMENTI': 9, 'GEYLANG': 10, 'HOUGANG': 11, 'JURONG EAST': 12, 'JURONG WEST': 13,
                     'KALLANG/WHAMPOA': 14, 'MARINE PARADE': 15, 'PASIR RIS': 16, 'PUNGGOL': 17, 
                     'QUEENSTOWN': 18, 'SEMBAWANG': 19, 'SENGKANG': 20, 'SERANGOON': 21, 
                     'TAMPINES': 22, 'TOA PAYOH': 23, 'WOODLANDS': 24, 'YISHUN': 25}
flat_type_options = {'2 ROOM': 1, '3 ROOM': 2, '4 ROOM': 3, '5 ROOM': 4, 'EXECUTIVE': 5, '1 ROOM': 0, 
                     'MULTI-GENERATION': 6}
storey_range_options = {'10 TO 12':1.09861229, '01 TO 03':-1.64791843 , '04 TO 06':0, '07 TO 09':0.69314718,
                        '19 TO 21':1.79175947, '22 TO 24':1.94591015, '16 TO 18':1.60943791, 
                        '34 TO 36':2.39789527, '28 TO 30':2.19722458, '37 TO 39':2.48490665, 
                        '49 TO 51':2.74653072, '25 TO 27':2.07944154, '40 TO 42':2.56494936, 
                        '31 TO 33':2.30258509, '46 TO 48':2.7080502, '43 TO 45':2.63905733}
flat_model_options = {'Improved':5, 'New Generation':12, 'DBSS':4, 'Standard':17, 'Apartment':3,
                      'Simplified':16, 'Model A':8, 'Premium Apartment':13, 'Adjoined flat':2,
                      'Model A-Maisonette':9, 'Maisonette':7, 'Type S1':19, 'Type S2':20,
                      'Model A2':10, 'Terrace':18, 'Improved-Maisonette':6, 'Premium Maisonette':15,
                      'Multi Generation':11, 'Premium Apartment Loft':14, '2-room':0, '3Gen':1}
lease_commence_date_options = [1979, 1978, 1980, 1981, 1976, 1977, 2011, 2012, 1996, 1988, 1985, 1986, 1974, 
                               1984, 1983, 1987, 1982, 2000, 2001, 2005, 1989, 2010, 1972, 1993, 1973, 1992, 
                               1990, 1998, 2004, 1997, 1971, 1975, 1970, 1969, 2013, 2008, 1999, 2003, 2002, 
                               1995, 2006, 1967, 1968, 2007, 1991, 1966, 2009, 1994, 2014, 2015, 2016, 2017, 
                               2018, 2019, 2020, 2021]

col1,col2,col3= st.columns(3)

with col1:
    month= st.selectbox(":violet[**Select the Month**]",sorted(month_options), key='One') 
    flat_type_selection = st.selectbox(":violet[**Select the Flat Type**]",sorted(flat_type_options.keys()),
                                  key='Four') 
    flat_type = flat_type_options[flat_type_selection]
    flat_model_selection = st.selectbox(":violet[**Select the Flat Model**]",
                                        sorted(flat_model_options.keys()), key='Seven') 
    flat_model = flat_model_options[flat_model_selection]

with col2:
    year= st.selectbox(":violet[**Select the Year**]",sorted(year_options), key='Two') 
    storey_range_selection = st.selectbox(":violet[**Select the Storey Range**]",
                                          sorted(storey_range_options.keys()), key='Five') 
    storey_range = storey_range_options[storey_range_selection]
    lease_commence_date= st.selectbox(":violet[**Select the Lease Commence Date**]",
                                      sorted(lease_commence_date_options), key='Eight') 

with col3:
    town_selection = st.selectbox(":violet[**Select the Town**]",sorted(town_options.keys()),
                                  key='Three') 
    town = town_options[town_selection]
    floor_area_sqm = np.log(st.number_input(label="**:violet[Enter the Value for Floor Area sqm]**", 
                                     min_value=31.0, max_value=366.7, value=31.0, step=1.0, 
                                     format="%.1f", key='Six'))    
    remaining_lease_months = st.number_input(label="**:violet[Enter the Value for Remaining Lease (Months)]**", 
                                             min_value=495, max_value=1173, value=495, step=5, key='Nine')
    
button= st.button(":red[***PREDICT THE RESALE FLAT PRICE***]",use_container_width=True)
if button:
    price= predict_resale_flat_price(month,town,flat_type,storey_range,floor_area_sqm,flat_model,
                            lease_commence_date, year,remaining_lease_months)              
    st.write("## :green[**The Resale Flat Price is :**]",price)