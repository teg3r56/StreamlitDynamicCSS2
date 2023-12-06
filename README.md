# streamlit-dynamic-css

Streamlit component that allows for custom CSS to be sized dynamically to Integral Streamlit elements

## Installation instructions 

```sh
pip install streamlit-dynamic-css
```

## Usage instructions

```python
import streamlit as st

from streamlit_dynamic_css import streamlit_dynamic_css

value = streamlit_dynamic_css()

st.write(value)
