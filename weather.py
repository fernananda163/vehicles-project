import pandas as pd

url = "https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html"

df = pd.read_html(url)[0]

df.columns = ['date_time', 'temperature', 'description']

print(df.head())