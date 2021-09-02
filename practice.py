import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit  超入門")
st.write("Dataframe")

df = pd.DataFrame({
  "1列目" : [1, 2, 3, 4],
  "2列目" : [10, 20, 30, 40]
})

st.write(df)

st.dataframe(df, width=100, height=100)
st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
python環境が、Python 3.8.5 64-bit('pythonenv': conda)
/opt/anaconda3/envs/pythonenv/bin/python
#まず、VScodeのターミナルで、
streamlit run practice.py #practice.py はファイル名
```

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

df1 = pd.DataFrame(
  np.random.rand(20, 3),
  columns=["a", "b", "c"]
)

st.line_chart(df1)
st.area_chart(df1)

df2 = pd.DataFrame(
  np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
  columns=["lat", "lon"]
)

st.map(df2)

from PIL import Image
if st.checkbox("Show Image"):
  st.write("Display.Image")
  img = Image.open("sample.png")
  st.image(img, caption= "TeX文書", use_column_width=True)

option = st.selectbox(
    "Please tell me your favorite number",
    list(range(1, 11))
)

"your favorite number is ", option, " !!"

st.write("Interactive Widgets")

# text = st.text_input("Please tell me your hobby")
# "your hobby is ", text, " !!"

# condition = st.slider("How's it going?", 0, 100, 50)
# "condition is" , condition


# text = st.sidebar.text_input("Please tell me your hobby")
# "your hobby is ", text, " !!"

# condition = st.sidebar.slider("How's it going?", 0, 100, 50)
# "condition is" , condition

left_columns, right_columns = st.columns(2)

button = left_columns.button("右カラムに文字を表示")

if button:
  right_columns.write("右カラム")

# text = st..text_input("Please tell me your hobby")
# "your hobby is ", text, " !!"

# condition = st..slider("How's it going?", 0, 100, 50)
# "condition is" , condition

import time

st.write("プレグスバーの表示")
"Strat!!"

latest_iteration = st.empty() #latest_iteration には文字が入っていない
bar = st.progress(0) #progressbarが表される。

for i in range(100):
  latest_iteration.text(f"Iteration{i+1}") # fは値を文字列に入れたい時に使う
  bar.progress(i + 1)
  time.sleep(0.1)
  # print(i)

"Done!!!!!!!!!!"



expander1 = st.expander("Question1")
expander1.write("Answer1")
expander1.write("Answer1-2")
expander2 = st.expander("Question2")
expander2.write("Answer2")
expander3 = st.expander("Question3")
expander3.write("Answer3")



print("完了")