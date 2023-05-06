import pandas as pd
import streamlit as st

import streamlit.components.v1 as components

power_bi_embed_code = "https://app.powerbi.com/view?r=eyJrIjoiNTI3MDA2YWMtZGU1Mi00N2Q5LWI2ZmEtNDA0Y2M4YWIyZGE5IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9"

components.iframe(power_bi_embed_code, width=1440, height=900)
