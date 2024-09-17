import pandas as pd
import streamlit as st

#应用标题
#st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="国元金工数据库展示", page_icon="random", layout="wide", initial_sidebar_state='auto')

#标题文本设置
st.title('基金ETF数据库')

#添加筛选条件
st.subheader('基金筛选条件：')