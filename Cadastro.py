import streamlit as st
import pandas as pd
import datetime

st.set_page_config(
    page_title='Cadastro de Clientes',
    page_icon='🪷',
    layout='wide'
)

def gravar_dados(nome, data_nasc, tipo):
    if nome and data_nasc <= datetime.date.today():
        st.session_state['sucesso'] = True
    else:
        st.session_state['sucesso'] = False

min_date = datetime.date(1920, 1, 1)
max_date = datetime.date(2030, 12, 31)

st.title("Cadastro de Clientes")
st.divider()

st.write('Novo cadastro: ')
nome = st.text_input('Nome: ', key='nome_cliente')
dt_nasc = st.date_input('Data de nascimento: ', format='DD/MM/YYYY', key='data_nascimento',  min_value=min_date, max_value=max_date)
tipo = st.selectbox('Tipo: ', 
                    ['Pessoa Física', 'Pessoa Jurídica'], 
                    key='tipo_cliente')

btn_cadastrar = st.button('Cadastrar', on_click=gravar_dados, args=[nome, dt_nasc, tipo])

if btn_cadastrar:
    if st.session_state['sucesso']:
        with open('clientes.csv', 'a', encoding='utf-8') as file:
            file.write(f'{nome},{dt_nasc},{tipo}\n')
        st.success('Cliente cadastrado com sucesso!', icon='✅')
    else:
        st.error('Houve algum problema no cadastro!', icon='❌')
