import streamlit as st
import pandas as pd 
import warnings
import locale

import streamlit.components.v1 as components
from paginas.configuracoes import pagina_configuracoes
from paginas.consultar_hana import pagina_consultar_hana
from paginas.seletor_padrao import pagina_seletor_padrao
from paginas.localizar_cliente import pagina_localizar_cliente
from paginas.selecionar_areas import pagina_selecionar_areas

from conf import config_cosern

if "engine" not in st.session_state:
    st.session_state.engine = None

# Chave para utilização da API do Google Maps
st.session_state['google_api_key'] = "AIzaSyBRCwdHEzalMqp7-9lBLFZ1ibfhMGrrbrM"
if not 'conexao_hana' in st.session_state:
    st.session_state['conexao_hana_status'] = ""
    
if 'config_empresa' not in st.session_state:
    st.session_state['empresa'] = 'Neoenergia Cosern'
    st.session_state['config_empresa'] = config_cosern

# Acrescentando um estilo personalizado (css)
with open("static/estilo.css") as estilo: 
   st.markdown(f"<style>{estilo.read()}</style>", unsafe_allow_html=True)

warnings.filterwarnings("ignore") 
#  -- Configurações Básicas: Fim

st.logo("static/logo.png", icon_image="static/logo-mini.png")
#st.set_page_config(page_title="SASI")

pg = st.navigation(
    {
        "Seleção": [
            st.Page(
                page=pagina_configuracoes,
                title="Configurações",
                icon=":material/settings:"
            ),
            st.Page(
                page=pagina_localizar_cliente,
                title="Localizar cliente(s)",
                icon=":material/search:"
            ),
            st.Page(
                page=pagina_consultar_hana,
                title="Consultar alvos",
                icon=":material/filter_alt:"
            ),
            st.Page(
                page=pagina_seletor_padrao,
                title="Analisar alvos",
                icon=":material/my_location:"
            ),
            st.Page(
                page=pagina_selecionar_areas,
                title="Selecionar áreas",
                icon=":material/travel_explore:"
            ),
        ],
        "Iluminação Pública": [
            st.Page(
                page="paginas/fiscalização_direcionada.py",
                title="Fiscalização direcionada",
                icon=":material/location_searching:"
            )
        ],
        "Regularização de Clandestinos": [
            st.Page(
                page="paginas/regularização_clandestinos.py",
                title="Potenciais clandestinos",
                icon=":material/wrong_location:"
            )
        ]
    }
)


pg.run()

