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
   fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
   if not fruit_choice:
      streamlit.error("Please select fruit to get information")
   else:
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
      # Json Normalized
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      # Table format from Json
     streamlit.dataframe(fruityvice_normalized)
      
except URLError as e:
  streamlit.error()

streamlit.header("Fruityvice Fruit Advice!")
streamlit.text(fruityvice_response.json())


streamlit.header("Fruit Load List Contains")
#snowflake Related Functions
def get_fruit_load_list():
     with my_cnx.cursor() as my_cur:
         my_cur.execute("Select * from fruit_load_list")
         return  my_cur.fetchall()
# Add a button to load the Fruits
if streamlit.button('Get Fruit Load List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows = get_fruit_load_list()
      streamlit.dataframe(my_data_rows)
   
