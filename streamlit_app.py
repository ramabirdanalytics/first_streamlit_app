import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title("Jai Ganesh Om Sai Ram")
streamlit.header("Breakfast Menu")
streamlit.text("🍞 Idli & Dosa")
streamlit.text ("🥣 Upma Pesarat")

streamlit.title("Breakfast Menu")
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

fruits_selected= streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index),['Avocado','Banana','Grapefruit'])
streamlit.dataframe(my_fruit_list.loc[fruits_selected])

streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
      streamlit.error("Please select fruit to get information")
   else
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     streamlit.dataframe(fruityvice_normalized)
      
except URLError as e:
  streamlit.error()

streamlit.header("Fruityvice Fruit Advice!")
streamlit.text(fruityvice_response.json())

# Json Normalized

# Table format from Json

streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The Fruit Load List Contains:")
fruit_entered= streamlit.text_input('What fruit would you liketo add?')
streamlit.dataframe(my_data_row)
streamlit.write('Thanks for Adding ', fruit_entered)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
