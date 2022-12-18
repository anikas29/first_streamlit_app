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
#now filtered the table data based on the fruits a customer will choose, so we pre-populate the list
#put this list of selected fruits into a variable called fruits_selected
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple', 'Grapefruit'])

#now use the fruits in the fruits_selected list to pull rows from the full dataset, and assign the data to a variable called fruits_to_show
fruits_to_show = my_fruit_list.loc[fruits_selected] #this is from pandas.dataframe.loc, which accesses the group of rows and columns by label or boolean array (loc)

#Display the table on the page
streamlit.dataframe(fruits_to_show)
