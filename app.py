from st_pages import Page, Section, add_page_title, show_pages
import seaborn as sns
import streamlit as st
import statsmodels as stas
import matplotlib.pyplot as  plt
import plotly.express as plotlye
import sklearn.preprocessing as splt




show_pages(
    [
        Page("example_app/streamlit_app_sections.py", "Home"),

        Page("example_app/example_one.py", "Clustering"),


        # The pages appear in the order you pass them
        Page("example_app/example_four.py", "Linear Regression"),
        Page("example_app/example_two.py", "Macroeconomics Indicators"),

        # Will use the default icon and name based on the filename if you don't
        # pass them
        Page("example_app/example_three.py"),
        # You can also pass in_section=False to a page to make it un-indented
        Page("example_app/example_five.py", "Example Five", "🧰", in_section=False),
    ]
)

add_page_title()

