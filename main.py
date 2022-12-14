import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib
import plotly.express as px
import numpy as np
from matplotlib.backends.backend_agg import RendererAgg
import requests
from streamlit_lottie import st_lottie
from streamlit_folium import st_folium
import folium

st.set_page_config(
    page_title="Population And HealthCare Analysis",
    page_icon="๐ฅ",
    layout="wide",
)


# Lottie Icon
@st.cache
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url = "https://assets2.lottiefiles.com/packages/lf20_uwWgICKCxj.json"
lottie_json = load_lottieurl(lottie_url)
st_lottie(lottie_json, speed=1, height=300, key="initial")


# Preparation to display plot
# matplotlib.use("agg")
_lock = RendererAgg.lock

# Seaborn style setup
# sns.set_style("darkgrid")
row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
    (0.1, 2, 0.2, 1, 0.1)
)

# Title
row0_1.title("Population And HealthCare Analysis")

with row0_2:
    st.write("")

row0_2.subheader(
    "GrowingTenten \n ๐ ์ฑ์ฅ๋ฐ์ก์ํํ"
)

# Introduction
row1_spacer1, row1_1, row1_spacer2 = st.columns([0.1, 3.2, 0.1])

with row1_1:
    st.subheader(
        '''
        **๊ณ ๋ นํ, ๊ทธ๋ฆฌ๊ณ  ์ฝ๋ก๋ 19 ์ดํ ์๋ฃ ์ธํ๋ผ**
        '''
    )
    st.markdown(
        '''
        
        '''
    )
    st.markdown(
        '''
        ์ฝ๋ก๋19 ์ดํ๋ก ์๋ฃ ์ธํ๋ผ๋ ์ด๋ฃจ ๋งํ  ์ ์์ด ์ค์ํ ์ฌ์์ด ๋์๋ค. ์คํ์ ๋ฐ ์๊ธ ๋ณ์ ๋ถ์กฑ์ผ๋ก ์ธํด ~~
        ๊ทธ๋ฆฌ๊ณ  ๊ฐ์ํ๋๋ **์ธ๊ตฌ ๊ณ ๋ นํ**๋ก ์ธํด ์ง์ญ ๊ฐ ์๋ฃ ์ธํ๋ผ ๋ถ๊ท ํ ๋ฌธ์ ๊ฐ ์ ์  ์ฌ๊ฐํด์ง๊ณ  ์๋ค. 
        ์ด์ ๋ฐ๋ผ ์ฐ๋ฆฌ ์กฐ๋ ๋ฏธ๋ํ๋ก์ ํธ์์ ๋ถ์ํ์๋ **์ด ์ธ๊ตฌ์**(2008 - 2021)๋ฅผ ๋ฐํ์ผ๋ก ์๋ฃ๊ธฐ๊ด ๋ฐ์ดํฐ์ ์ ๊ทผํ๊ณ ์ ํ๋ค.
        '''
    )
    st.markdown(
        '''
        ์ฐ์  ์ง์ญ ๋ณ **์ธ๊ตฌ ์**์ ๋ฐ๋ฅธ **ํ์ฌ ์ด์ ์ค์ธ ์๋ฃ๊ธฐ๊ด ์**(2022.06 ๊ธฐ์ค)๋ฅผ ๋ถ์ํ๋ค. 
        ๋ชฉํ๋ ์ง์ญ ๋ณ ์ธ๊ตฌ ์์ ๋ฐ๋ฅธ ์๋ฃ๊ธฐ๊ด ๋น์จ์ ๋น๊ต ๋ถ์ํ๊ณ  ๋ํ์ ์ง๋๋ฅผ ํตํด ์๊ฐํํ๋ ๊ฒ์ด๋ค. 
        ์ธ๊ตฌ์์ ๋ฐ๋ฅธ **์ธํ๋ผ ๊ฒฉ์ฐจ**๊ฐ ๋ฐ์ํ  ๊ฒ์ด๋ผ๋ ๊ฐ์ค์ ๊ฒ์ฆํ๊ณ  ํ์ฌ ์๋ฃ ์ธํ๋ผ๊ฐ ๋ถ์กฑํ ์ง์ญ์ ์ฐพ๋๋ค. 
        ๋ํ์ฌ, ์๋ฃ์์ค ๊ฐ์๊ณผ ํ์ ๋ฐ์ดํฐ๋ฅผ ๋ถ์ํ์ฌ ์์ผ๋ก์ ์ธํ๋ผ ๊ฒฉ์ฐจ๋ฅผ ๊ฐ์ ์ํฌ ์ ์๋ ๋ฐฉ์์ ๋ชจ์ํด ๋ณธ๋ค.
        
        
        '''
    )
    st.markdown(
        '''
        
        '''
    )


# Select Hypothesis
row2_spacer1, row2_1, row2_spacer2 = st.columns((0.1, 3.2, 0.1))
with row2_1:
    hypo = st.selectbox(
        "Select Hypothesis ๐",
        [
            "๊ฐ์ค 1 : ์ด ์ธ๊ตฌ์ - ์๋ฃ๊ธฐ๊ด ์",
            "๊ฐ์ค 2 : ๊ณ ๋ นํ ๋น์จ - ์๋ฃ๊ธฐ๊ด ์",
            "๊ฐ์ค 3 : ์ธ๊ตฌ์ - ์๋ฃ๊ธฐ๊ด ๊ฐํ์",
            "๊ฐ์ค 4 : ๊ธฐ๋ณธ ์ธํ๋ผ - ์๋ฃ๊ธฐ๊ด ์",
            "๊ฐ์ค 5 : ๋ฏธ์ฉ ๋ชฉ์  ์๋ฃ๊ธฐ๊ด ๋น์จ"
        ]
    )


# Import Data
file_dict = {
    "๊ฐ์ค 1 : ์ด ์ธ๊ตฌ์ - ์๋ฃ๊ธฐ๊ด ์": "df_now_hos",
    "๊ฐ์ค 2 : ๊ณ ๋ นํ ๋น์จ - ์๋ฃ๊ธฐ๊ด ์": "mise_health",
    "๊ฐ์ค 3 : ์ธ๊ตฌ์ - ์๋ฃ๊ธฐ๊ด ๊ฐํ์": "misemise_china",
    "๊ฐ์ค 4 : ๊ธฐ๋ณธ ์ธํ๋ผ - ์๋ฃ๊ธฐ๊ด ์": "misemise_korea",
    "๊ฐ์ค 5 : ๋ฏธ์ฉ ๋ชฉ์  ์๋ฃ๊ธฐ๊ด ๋น์จ": "misemise_weather"
}


@st.cache
def get_hypo_data(hypo_name):
    file_name = f"data/{file_dict[hypo_name]}.csv"
    data = pd.read_csv(file_name)
    return data


st.markdown('***')

# Display Hypothesis
line1_spacer1, line1_1, line1_spacer2 = st.columns((0.01, 3.2, 0.01))


with line1_1:
    st.subheader("**{}**".format(hypo))

# Load Data
data_medical = pd.read_csv('data/medical_department.csv')
data = get_hypo_data(hypo)


# Display Data Set
row3_space1, row3_1, row3_space2 = st.columns(
    (0.01, 1, 0.01)
)

with row3_1, _lock:
    st.subheader("DataSet")
    with st.expander("DataSet ๋ณด๊ธฐ ๐"):
        st.markdown('**์๋ฃ๊ธฐ๊ด ๋ฐ์ดํฐ**')
        st.dataframe(data_medical)
        st.markdown('**๋ฏธ๋ํ๋ก์ ํธ_์ ๊ตญ์ด์ธ๊ตฌ์**')
        st.dataframe(data)

st.markdown(
    '''
    
    '''
)

# Data Visualization
row4_space1, row4_1, row4_space2 = st.columns(
    (0.01, 1, 0.01)
)

with row4_1, _lock:
    st.subheader("Data Visualization")
    fig, ax = plt.subplots(figsize=(25, 5))
    sns.countplot(
        data=data_medical, x='์๋๋ช',
        order=data_medical.loc[data_medical['ํํฉ'] == 1, '์๋๋ช'].value_counts(
        ).sort_values(ascending=False).index
    )

    ax.set_title("์ ๊ตญ ์๋ฃ๊ธฐ๊ด ํํฉ")
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(25, 5))
    sns.lineplot(data=data.sort_values(
        '์๋ฃ๊ธฐ๊ด์', ascending=False), x="์๋๋ช", y="์ด์ธ๊ตฌ์")
    st.pyplot(fig)

# Footers
footer_space1, footer_1, footer_space2 = st.columns(
    (0.01, 1, 0.01)
)

with footer_1, _lock:
    st.markdown("***")
    st.markdown(
        "**์ฑ์ฅ๋ฐ์ก์ํํ** - ์ด์ฌ๋ชจ, ์กฐ์์ฌ, ์ํ์ง, ๊น์๋ฏผ"
    )

    st.markdown(
        "**๋ฉ์์ด์ฌ์์ฒ๋ผ AI ์ค์ฟจ 7๊ธฐ ๋ฏธ๋ํ๋ก์ ํธ** : 2022๋ 10์ 19์ผ ~ 23์ผ"

    )
