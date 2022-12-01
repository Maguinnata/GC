import streamlit as st
import pandas as pd
import plotly.express as px

########### CONFIG ###########

st.set_page_config(page_title='Game Changers',
                   page_icon= ':bar_chart:',
                   layout= 'wide',
                   )

c_icebox= '#4169E1'
c_haven= '#87CEEB'
c_ascent= '#6959CD'
c_breeze= '#FFDEAD'
c_pearl='#00FFFF'
c_bind= '#D2691E'
c_fracture= '#006400'

########### BASE DE DADOS ###########

stats = pd.read_excel('Stats Individual GC.xlsx')
filtro2 = ['Players','ACS','K','D','A','KD','ADR','FK','FD','Clutches W','Clutches Total','KAST%','HS%','L-Round','W-Round','Pistol, 2º e 3º Round (CT)','Pistol, 2º e 3º Round (TR)']
stats_f2 = stats.drop(columns= filtro2)
wr_mapas = stats_f2.groupby(['Mapas','Time']).sum().round(2).reset_index()

tr_wr = (wr_mapas['W-TR']/(wr_mapas['W-TR']+wr_mapas['L-TR']))*100
ct_wr = (wr_mapas['W-CT']/(wr_mapas['W-CT']+wr_mapas['L-CT']))*100

filtro3 = ['Players','ACS','K','D','A','KD','ADR','FK','FD','Clutches W','Clutches Total','KAST%','HS%','L-Round','W-Round','W-TR','L-TR','W-CT','L-CT']
stats_f3= stats.drop(columns= filtro3)
pistols_ct = stats_f3.groupby(['Time', 'Pistol, 2º e 3º Round (CT)',]).count().reset_index()
pistols_tr = stats_f3.groupby(['Time', 'Pistol, 2º e 3º Round (TR)',]).count().reset_index()

###################### COMPOSIÇÃO ######################
tab1, tab2, = st.tabs(['▶️ ATK & DEF','▶️ Pistol, 2º e 3º Round'])

with tab1:
    ########### CT ###########
    st.subheader('Win rate Lado Defensivo')

    g_wr_ct = px.histogram(
        x=wr_mapas['Time'],
        y=ct_wr.round(2),
        #barmode='group',
        color= wr_mapas['Mapas'],
        color_discrete_sequence= [c_ascent,c_bind,c_breeze,c_fracture,c_haven,c_icebox,c_pearl,],
        text_auto=True,
        width=1150,
        height=550,
        labels=dict(x='Mapas', y='%')
        )
    g_wr_ct.update_traces(textposition='inside',textfont_size= 15,text='percent+label', overwrite=True,textangle= 0)
    g_wr_ct.update_layout(font=dict(size=15))

    st.plotly_chart(g_wr_ct)
    #st.markdown('##')
    st.markdown('----')
    #st.markdown('##')

    ########### TR ###########
    st.subheader('Win rate Lado Atacante')

    g_wr_tr = px.histogram(
        x=wr_mapas['Time'],
        y=tr_wr.round(2),
        # barmode='group',
        color=wr_mapas['Mapas'],
        color_discrete_sequence=[c_ascent, c_bind, c_breeze, c_fracture, c_haven, c_icebox, c_pearl, ],
        text_auto=True,
        width=1150,
        height=550,
        labels=dict(x='Mapas', y='%')
        )
    g_wr_ct.update_traces(textposition='inside', textfont_size= 15, text='percent+label', overwrite=True, textangle= 0,)
    g_wr_ct.update_layout(font=dict(size=15))

    st.plotly_chart(g_wr_tr)
    #st.markdown('##')
    st.markdown('----')
    #st.markdown('##')

    ########### MAPAS JOGADOS ###########
    st.subheader('Mapas Jogados por cada Time')

    g_pr_m = px.histogram(
        x= wr_mapas['Time'],
        y= wr_mapas['Pickrate'],
        color= wr_mapas['Mapas'],
        color_discrete_sequence=[c_ascent, c_bind, c_breeze, c_fracture, c_haven, c_icebox, c_pearl, ],
        text_auto= True,
        width= 1150,
        height= 550
    )
    g_pr_m.update_traces(textangle= 0,textposition='inside', textfont_size= 15, text='percent+label', overwrite=True)
    g_pr_m.update_layout(font=dict(size=15))
    st.plotly_chart(g_pr_m)

with tab2:
    st.subheader('Pistols CT')

    g_pistol_ct = px.scatter(
        y= pistols_ct['Pistol, 2º e 3º Round (CT)'],
        x= pistols_ct['Time'],
        color= pistols_ct['Time'],
        size= pistols_ct['Pickrate'],
        labels=dict(x= 'Times', y= 'QTD'),
        text= pistols_ct['Pickrate'],
        width= 1150,
        height= 550
    )
    g_pistol_ct.update_layout(font=dict(size=15))
    st.plotly_chart(g_pistol_ct)

    #st.markdown('##')
    st.markdown('----')
    #st.markdown('##')

    st.subheader('Pistols TR')

    g_pistol_tr = px.scatter(
        y=pistols_tr['Pistol, 2º e 3º Round (TR)'],
        x=pistols_tr['Time'],
        color=pistols_tr['Time'],
        size=pistols_tr['Pickrate'],
        labels=dict(x='Times', y='QTD'),
        text=pistols_tr['Pickrate'],
        width=1150,
        height=550
    )
    #g_pistol_tr.update_yaxes(categoryorder= 'total descending')
    g_pistol_tr.update_layout(font=dict(size=15))
    st.plotly_chart(g_pistol_tr)