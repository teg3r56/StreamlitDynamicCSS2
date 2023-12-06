import streamlit.components.v1 as components
from streamlit-dynamic-css import streamlit_dynamic_css
import os
import json

def streamlit_dynamic_css(selector, css_string):
    _RELEASE = True  # Set to False if you're in development mode
    _frontend_dir = os.path.join(os.path.dirname(__file__), 'frontend/build') if _RELEASE else 'http://localhost:3000'

    component_value = components.html(
        json.dumps({"selector": selector, "cssString": css_string}),
        url=_frontend_dir,
        height=30 
    )
    return component_value

def streamlit_flexbox_test():
    _RELEASE = True  # Set this flag
    _frontend_dir = os.path.join(os.path.dirname(__file__), 'frontend/build') if _RELEASE else 'http://localhost:3000'
    components.html(open(os.path.join(_frontend_dir, 'index.html')).read(), height=400)
