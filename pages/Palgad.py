# VAJALIKUD LISAD KIRJUTAMISEKS
import streamlit as st
import pandas as pd
import duckdb


# VAJALIKUD LISAD GRAAFIKUTE TEGEMISEKS
import matplotlib.pyplot as plt
import seaborn as sns


# LEHE ESIMENE PEALKIRI
st.write("# Palgad tööstusharude lõikes")

# DEFINEERIME, KUST ANDMED TULEVAD
data = pd.read_csv("emta_data.csv") 


# MUUTUJA DEFINEERIMINE
TAX_PERCENTAGE = 0.338 


# DEFINEERIME TEGEVUSALA KESKMISE PALGA

salary_stats = duckdb.sql(f""" 
    SELECT 
        tegevusala,
        ROUND(avg(toojoumaksud / {TAX_PERCENTAGE} / tootajate_arv / 3), 2) AS keskmine_palk
    FROM data
    WHERE aasta = 2026 AND kvartal = 1 AND tegevusala IS NOT NULL
    GROUP BY tegevusala
    ORDER BY keskmine_palk DESC
    """).df()

"""
"""
"""
"""

# ESIMESE GRAAFIKU PEALKIRI

st.write("### Tegevusala keskmine palk töötaja kohta")

"""
"""

# TEGEVUSALA KESKMINE PALK TÖÖTAJA KOHTA

st.write(salary_stats)

"""
"""
"""
"""

# TEISE GRAAFIKU PEALKIRI

st.write("### Tegevusala keskmine palk töötaja kohta / interaktiivne")

"""
"""

# TEGEVUSALA KESKMINE PALK GRAAFIK

st.bar_chart(salary_stats, x="tegevusala", y="keskmine_palk", sort=False, horizontal=True)