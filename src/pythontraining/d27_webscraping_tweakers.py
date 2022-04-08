import pandas as pd

# url = "https://tweakers.net/smartphones/vergelijken/"
url = "https://www.knmi.nl/nederland-nu/weer/waarnemingen"

dfs = pd.read_html(url)

df = dfs[0].set_index("Station")
print(df)