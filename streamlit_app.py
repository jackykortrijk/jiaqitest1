import pandas as pd
import streamlit as st

#应用标题
#st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="国元金工数据库展示", page_icon="random", layout="wide", initial_sidebar_state='auto')

#标题文本设置
st.title('基金ETF数据库')

#添加筛选条件
st.subheader('基金筛选条件：')
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        agree = st.checkbox('显示指数实时折溢价情况')
        fee = st.checkbox('显示基金管理费率（%）')
        set_date = st.checkbox('显示上市日期')
    