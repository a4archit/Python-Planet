import streamlit as st 
import numpy as np



st.header(":orange[Matrix mall]")
st.divider()

EXAMPLE_MATRIX = np.array([
    [1,0,2],
    [3,1,2],
    [6,2,1]
])


st.write(f"""#### Single matrix
You can continue with single matrix, with *n*-dimensions.
\n**Note:** Your matrix pattern:\n
Elements separate by comma`,` and
rows separate by clicking `enter`.

Example:\n
    1,0,2
    3,1,2
    6,2,1
""")

inputs = st.text_area(
    "Input matrix",
    height=5,
    placeholder="Enter your matrix here"
)


# converting user input to numpy matrix
dummy_list = []
for row in inputs.split('\n'):
    dummy_list.append([int(element) for element in row.split(',')])

input_matrix = np.array(dummy_list)

st.write("GIven Matrix is")
st.write(input_matrix)

# transpose
st.write("Transpose of the matrix is")
st.write(input_matrix.transpose())
 
# 


