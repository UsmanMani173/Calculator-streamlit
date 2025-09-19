import streamlit as st
import math
def sum(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  try:
    return x/y
  except ZeroDivisionError:
    return "Can not divide by zero!!"
def power(x,y):
  return math.pow(x,y)

def square_root(x):
  try:
    return math.sqrt(x)
  except ValueError:
      return "Can not find square root of negative number!!"
def logarithm(x):
  try:
    return math.log(x)
  except ValueError:
    return "Non-positive numbers ka log nahi hota"
def sine(x):
  return math.sin(math.radians(x))
def cosine(x):
  return math.cos(math.radians(x))
def tangent(x):
  return math.tan(math.radians(x))

#--------------Session State-------------------
if "expresion" not in st.session_state:
  st.session_state.expresion=""

#--------------Helper Function-------------------
def press(value):
  st.session_state.expresion += str(value)

def clear():
  st.session_state.expresion=""

def calculator():
  try:
    st.session_state.expresion = str(eval(st.session_state.expresion))
  except Exception:
    st.session_state.expresion = "Error"
#--------------Scientific Function-------------------
def sci_function(func):
  try:
    value = float(st.session_state.expresion)

    if func =="sqrt":
      st.session_state.expresion = str(square_root(value))  
    elif func =="log":
      st.session_state.expresion = str(logarithm(value))
    elif func =="sin":
      st.session_state.expresion = str(sine(value))
    elif func =="cos":
      st.session_state.expresion = str(cosine(value)) 
    elif func =="tan":
      st.session_state.expresion = str(tangent(value))
    elif func =="pow":
      st.session_state.expresion = str(pow(value,2))
      
  except ValueError:
    st.session_state.expresion = "Error"

#--------------Streamlit UI Code-------------------
st.set_page_config(page_title="Calculator App",page_icon=":calculator:",layout="centered")
st.title("My Calculator")

st.text_input("Screen",value=st.session_state.expresion,key="display",disabled=False)

#--------------Numaric keypad-------------------

buttons = [
  ["sqrt","log","x^2"]
  ,["sin","cos","tan"]
  ,["7","8","9","/"]
  ,["4","5","6","(*)"]
  ,["1","2","3","--"]
  ,["0",".","=","++"]
  
  ]

func_map = {
    "sqrt": "sqrt",
    "log": "log",
    "sin": "sin",
    "cos": "cos",
    "tan": "tan",
    "x^2": "pow",
    
}

for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        if btn in func_map:
            cols[i].button(str(btn), on_click=lambda f=func_map[btn]: sci_function(f), use_container_width=True)
        elif btn == "=":
            cols[i].button(str(btn), on_click=calculator, use_container_width=True)
        else:
            cols[i].button(str(btn), on_click=lambda b=btn: press(b), use_container_width=True)
st.button("Clear", on_click=clear, use_container_width=True)





