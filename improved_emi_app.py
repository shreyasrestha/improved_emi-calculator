import streamlit as st
import pandas as pd 
import numpy as np
def calculate_emi(p,n,r):
  nume=(1+(r/100))**n
  deno=((1+(r/100))**n)-1
  emi=p*(r/100)*(nume/deno)
  return emi
def calculate_outstanding_balance(p,n,r,m):
  balance=(p*((1+(r/100))**n)-((1+(r/100))**m))/(((1+(r/100))**n)-1)
  return balance
st.title("calculating the outstanding balance ")
principal=st.slider("choose principal amount",1000,1000000)
tenure=st.slider("Choose loan period",1,30)
roi=st.slider("Choose the rate of interest",1.0,15.0)
m=st.slider("Choose Period after which the Outstanding Loan Balance is calculated (in months)",(1-(tenure*12)))
n=tenure*12
r=roi/12
if st.button("calculate EMI"):
  calc_emi=calculate_emi(principal,n,r)
  st.write("EMI=",round(calc_emi,3))
if st.button("calculate outstanding loan balance"):
  calc_olb=calculate_outstanding_balance(principal,n,r,m)
  st.write(f"The outstanding loan balance={round(calc_olb,3)}")