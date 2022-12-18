import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach, & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Choose the Fruit Name column as the Index so that the customer can choose the fruits by name
my_fruit_list = my_fruit_list.set_index('Fruit')

#Create a user-interactive widget called a Multi-Select (a pick list), that will allow users to pick the fruits they want in their smoothies
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#Display the table on the page
streamlit.dataframe(my_fruit_list)
