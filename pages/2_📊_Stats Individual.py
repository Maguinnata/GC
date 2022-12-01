import streamlit as st
import pandas as pd
import plotly.express as px

########### CONFIG ###########

st.set_page_config(page_title='Game Changers',
                   page_icon= ':bar_chart:',
                   layout= 'wide',
                   )

########### CORES ###########
c_icebox= '#4169E1'
c_haven= '#87CEEB'
c_ascent= '#6959CD'
c_breeze= '#FFDEAD'
c_pearl='#00FFFF'
c_bind= '#D2691E'
c_fracture= '#006400'



########### BASE DE DADOS ###########

stats = pd.read_excel('Stats Individual GC.xlsx')

filtro1 = ['Mapas','Pickrate','Clutches W','Clutches Total','Pistol, 2º e 3º Round (CT)','Pistol, 2º e 3º Round (TR)']
stats_f1 = stats.drop(columns= filtro1).round(2)
stats_individual = stats_f1.groupby(['Time','Players']).mean().reset_index().round(2)




########### SIDEBAR ###########

st.sidebar.header('Filtros')

var1 = st.sidebar.selectbox(
    'Selecione uma Variável (Média)',
    options= stats_f1.columns.unique().drop(['Players','Time','W-TR','L-TR','W-CT','L-CT','W-Round','L-Round'])
)

stats_var1 = stats_f1.query(
    'ACS == @var1'
)

########### COMPOSIÇÃO ###########

tab1, tab2, = st.tabs(['▶️ Média','▶️ X vs Y'])

with tab1:
    g_stats_indiv = px.scatter(
        stats_individual.round(2),
        x= 'Time',
        y=var1,
        #barmode='overlay',
        text= 'Players',
        color= 'Time',
        size= 'ACS',
        width= 1150,
        height= 550,
        title='<b> Variável por Time </b>'
    )

    g_stats_indiv.update_layout(font=dict(size=15))

    st.plotly_chart(g_stats_indiv)

with tab2:
    var2 = st.selectbox(
        'Selecione uma Variável (Eixo Y)',
        options=stats_f1.columns.unique().drop(['Players', 'Time','W-TR','L-TR','W-CT','L-CT','W-Round','L-Round'])
    )

    stats_var2 = stats_f1.query(
        'ACS == @var2'
    )

    var3 = st.selectbox(
        'Selecione uma Variável (Eixo X)',
        options=stats_f1.columns.unique().drop(['Players', 'Time','W-TR','L-TR','W-CT','L-CT','W-Round','L-Round'])
    )

    stats_var3 = stats_f1.query(
        'ACS == @var3'
    )

    g_scatter_acs_kpr = px.scatter(stats_individual,
                                   y=var2,
                                   x=var3,
                                   text=stats_individual['Players'],
                                   color=stats_individual['Time'],
                                   size=stats_individual['ACS'],
                                   labels=dict(x='ACS', y='KpR'),
                                   width=1150,
                                   height=550,
                                   hover_data=['ACS'],
                                   )
    g_scatter_acs_kpr.update_layout(font=dict(size=15))
    st.plotly_chart(g_scatter_acs_kpr)

