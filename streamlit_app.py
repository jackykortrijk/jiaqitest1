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
        
    with col3:
        genre = st.radio("机构持有人占比", ('高占比（70%以上）', '中占比（40%-70%）', '低占比（70%以下）'))
    
    with col5:
        values = st.slider('基金规模（亿元）：\n', 0.0, 1000.0, (10.0, 500.0))
        
st.help(values)
st.write('values变量是什么：', values)
st.write('获取values第一个值：', values[0])

#文件加载
ETF_data = pd.read_csv('C:\streamlittest\A股列表.csv', index_col=0, encoding='UTF-8')