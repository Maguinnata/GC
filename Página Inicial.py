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


c_chamber= '#D69F3D'
c_kayo= '#161A49'
c_fade= '#3E091B'
c_sova= '#435FB2'
c_viper= '#00BF4B'
c_sage= '#079B6A'
c_breach= '#855238'
c_astra= '#4C21AD'
c_raze= '#FFA954'
c_neon= '#113783'
c_omen= '#5C44E0'
c_jett= '#9CA9E5'
c_brimstone= '#C24E11'
c_skye= '#B2DD8B'
c_killjoy= '#F9DD31'
c_cypher= '#97A19B'
c_reyna= '#9D4293'
c_yoru= '#1C48FB'


########### BASE DE DADOS ###########

stats = pd.read_excel('Stats Individual GC.xlsx')
stats['Pickrate'] = stats['Pickrate']/2

agent_pr = pd.read_excel('Agent Pickrate GC.xlsx')
agent_pr_f = agent_pr.drop(columns='Matches')

########### COMPOSIÇÃO ###########

st.title('📊 Infos Gerais')
st.markdown('----')
st.write('Esse é um trabalho sobre o Game Changers Championship: Berlin, todo os dados foram retirados do site e bot rib.gg. '
         'O intuito é reunir todos os parâmetros (individuas e time) para verificarmos o desempenho de cada time que passou pelo campeonato.')
st.write('Feito por: Maguinnata :)')
st.markdown('----')
st.subheader('Mapas Jogados')

g_mapas = px.pie(stats,
                 values= 'Pickrate',
                 names= 'Mapas',
                 width= 1150,
                 height= 550,
                 color_discrete_sequence= [c_haven,c_icebox,c_ascent,c_breeze,c_pearl,c_fracture,c_bind],
                 hover_data=['Mapas'],
                 )

g_mapas.update_traces(textposition='inside', textinfo='percent+label')
g_mapas.update_layout(font= dict(size= 18), legend= dict(font=dict(size= 15)))
st.plotly_chart(g_mapas)

st.markdown('----')

st.subheader('Agent Pickrate')

g_agent_pr = px.histogram(agent_pr_f,
                          y= 'Percentage',
                          x= 'Agent',
                          width= 1150,
                          height= 550,
                          text_auto= True,
                          labels=dict(x='Agent', y='Pickrate'),
                          color= 'Agent',
                          color_discrete_sequence=[c_chamber,c_kayo,c_fade,c_sova,c_viper,c_sage,c_breach,c_astra,c_raze,
                                                   c_neon,c_omen,c_jett,c_brimstone,c_skye,c_killjoy,c_cypher,c_reyna,c_yoru]
                          )


g_agent_pr.update_traces(textposition='inside',textfont_size= 18,text='percent+label', overwrite=True,textangle= 0)
g_agent_pr.update_layout(font= dict(size= 15), legend= dict(font=dict(size= 15)))
g_agent_pr.update_xaxes(tickangle = 45)
st.plotly_chart(g_agent_pr)



