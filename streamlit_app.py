import streamlit

streamlit.title('Moms New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('Avocado Toast')


streamlit.header('🍌🥭 Build Your Onw Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# lets put a picklist here 
streamlit.multiselect("Pick some fruits:" list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
