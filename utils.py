import locale
import numpy as np
import pandas as pd
import sqlalchemy
import streamlit as st
import urllib

def formatar_numero(valor: float, cifrao: bool=False, casas_decimais: int=0) -> str:
    """ Retorna um número como uma string no formato brasileiro, inclusive para moeda R$ X.YYY,ZZ """
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    if cifrao:
        return locale.format_string(f'R$ %.{casas_decimais}f', valor, True)
    else: 
        return locale.format_string(f'%.{casas_decimais}f', valor, True)
    
def coalesce(*args):
    return next((x for x in args if pd.notna(x)), np.nan)
    
def create_engine(username, password, host, port, tenant_database):

    engine = sqlalchemy.create_engine(url=f"hana+hdbcli://{username}:{urllib.parse.quote(password)}@{host}:{port}/{tenant_database}")
    try:
        engine.connect()
        st.toast("Successfully connected!")
        return engine
    except Exception as err:
        st.toast(f"\nUnexpected {err=}, {type(err)=}.")
        return
