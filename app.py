import streamlit as st
import pandas as pd
import numpy as np

st.title("SIP Calculator")
Amount = st.number_input("Amount",100,100000,2500) 
st.write(f"selected amount:{Amount}")
Duration = st.slider("Duration",0,25,5)

st.write(f"You have select duration:{Duration}")

Interest= st.slider("Interst Rate",10,40,15)

st.write(f"Interest Rate : {Interest}")

def sip_return(amount, interest, duration):
    r = interest / 12 / 100
    n = duration * 12
    
    fv = amount * (((1 + r)**n - 1) / r) * (1 + r)
    return round(fv, 2)
fv=sip_return(Amount, Interest, Duration)
invested_amount = Amount * Duration * 12
returns = fv - invested_amount

# Output
st.subheader("📈 Investment Summary")

st.write(f"💰 Total Invested Amount: ₹{round(Amount * Duration * 12, 2)}")
st.write(f"📊 Estimated Returns: ₹{round(returns, 2)}")
st.write(f"🏦 Future Value: ₹{round(fv, 2)}")
