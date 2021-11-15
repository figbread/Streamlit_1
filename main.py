import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("Streamlit超入門")
st.write("DataFrame")
# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })
# st.table(df.style.highlight_max(axis=0))

"""
こぐま
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

st.title("プログレスバーの表示")
"Start!"
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
"Done!"

st.write("Interactive Widgets")

left_columns, right_column = st.columns(2)
button = left_columns.button('右カラムに文字を表示')
if button:
    right_column.write("ここは右カラム")

expander1 = st.expander("このパッケージはなんですか")
expander1.write("Streamlitです")
expander2 = st.expander("利点はなんですか？")
expander2.write("学習コストが低いところです")


if st.checkbox('Show Chart'):
    df = pd.DataFrame(
        np.random.rand(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(df)

option = st.selectbox(
    'Choose your favorite number',
    list(range(1, 11))
)
"Your favorite number is", option

text = st.sidebar.text_input('Tell me your hobby')
condition = st.sidebar.slider("Tell me your current condition", 0, 100, 50)

"Your hobby is", text
"Your condition is", condition