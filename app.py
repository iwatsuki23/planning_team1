import streamlit as st
st.title("WizWe Planning Team")

import streamlit as st
import numpy as np

# streamlitのメソッドでmarkdown形式で表示
st.write(
    """
    # 案件状況の可視化
    グラフのイメージ-数種類*
    """
    )

# 適当なデータ作成
data = np.arange(0, 10, 0.1)

# streamlitのメソッドでデータを直線グラフに
st.line_chart(data)

import streamlit as st
import numpy as np
import pandas as pd
st.subheader('案件ごとの進捗率')
chart_data = pd.DataFrame(
     np.random.randn(7, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.dataframe(chart_data)

import streamlit as st
import numpy as np
import pandas as pd
st.subheader('NPSのイメージ')
chart_data = pd.DataFrame(
     np.random.randn(7, 3),
     columns=['a', 'b', 'c'])

st.bar_chart(chart_data)
st.dataframe(chart_data)
