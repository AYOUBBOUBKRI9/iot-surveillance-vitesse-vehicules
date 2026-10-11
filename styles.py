import streamlit as st
def appliquer_style():

    st.markdown("""
    <style>

    /* ===========================
       Fond général
    ============================ */

    .stApp{

        background-color:#F5F7FA;

    }

    /* ===========================
       Sidebar
    ============================ */

    section[data-testid="stSidebar"]{

        background-color:#1E293B;

    }

    section[data-testid="stSidebar"] *{

        color:white;

    }

    /* ===========================
       Titre
    ============================ */

    h1{

        color:#1F4E79;

        text-align:center;

        font-weight:bold;

    }

    h2{

        color:#1F4E79;

    }

    h3{

        color:#1F4E79;

    }

    /* ===========================
       DataFrame
    ============================ */

    div[data-testid="stDataFrame"]{

        border-radius:10px;

        border:1px solid #D0D7DE;

    }

    /* ===========================
       Boutons
    ============================ */

    .stButton>button{

        background:#1F4E79;

        color:white;

        border-radius:10px;

    }

    /* ===========================
       Metrics
    ============================ */

    div[data-testid="metric-container"]{

        background:white;

        border-radius:15px;

        padding:15px;

        box-shadow:0px 3px 8px rgba(0,0,0,0.12);

    }

    </style>
    """, unsafe_allow_html=True)