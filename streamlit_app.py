import streamlit
import pandas

streamlit.title("Jai Ganesh Om Sai Ram")
streamlit.header("Breakfast Menu")
streamlit.text("🍞 Idli & Dosa")
streamlit.text ("🥣 Upma Pesarat")

streamlit.title("Breakfast Menu")
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some Fruits: ", list(my_fruit_list.index))
fruits_selected= streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index),['Avocado','Banana','Grapefruit'])
streamlit.dataframe(my_fruit_list.loc[fruits_selected])
