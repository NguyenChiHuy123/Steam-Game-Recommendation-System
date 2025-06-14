import pickle
import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Steam Game's Recommender",
    # page_icon="🗣️",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.title("Menu")
    st.divider()
    st.write("Recommended")


def recommend(game):
    index = new_df[new_df['Name'] == game].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    game_lists=[]
    game_image_list=[]
    for i in distances[1:13]:
        game_lists.append(new_df.iloc[i[0]].Name)
        game_image_list.append(game_image.iloc[i[0]].Headerimage)
    return game_lists,game_image_list
        
# uplode data
new_df = pickle.load(open(os.path.join("notebooks", "game_data.pkl"), 'rb'))
similarity = pickle.load(open(os.path.join("notebooks", "similarity.pkl"), 'rb'))
game_image = pd.read_csv(os.path.join("notebooks", "image_data.csv"))
game_name = new_df['Name'].values

st.title("Steam Game's Recommendation System")
# st.warning('There was only New Game Data Since 2021 to 2023')

st.image(r"D:\\Resys_Games\\Steam-Game-Recommendation-System\\store_home_share.jpg", 
         width=750)

st.divider()

option = st.selectbox(
    'Select or type The Game Name: ⬇️',
    game_name)

st.write('You selected:', option)
if st.button('🔍 Find!'):
    st.toast("🙃 Enjoy!")
    # st.balloons()

   # Hiển thị game được chọn
    st.subheader("🎮 Game you selected:")
    selected_index = new_df[new_df['Name'] == option].index[0]
    selected_image = game_image.iloc[selected_index].Headerimage
    st.image(selected_image, width=300)
    st.markdown(f"### {option}")

    st.divider()

    st.header("Here are The Top 12 Game You also like 🎮:")
    rec,img=recommend(option)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(img[0])
        st.subheader(rec[0])
    with col2:
        st.image(img[1])
        st.subheader(rec[1])
    with col3:
        st.image(img[2])
        st.subheader(rec[2])
        
    col4,col5,col6 =st.columns(3)
    with col4:
        st.image(img[3])
        st.subheader(rec[3])
    with col5:
        st.image(img[4])
        st.subheader(rec[4])
    with col6:
        st.image(img[5])
        st.subheader(rec[5])

    col7, col8, col9 = st.columns(3)
    with col7:
        st.image(img[6])
        st.subheader(rec[6])
    with col8:
        st.image(img[7])
        st.subheader(rec[7])
    with col9:
        st.image(img[8])
        st.subheader(rec[8])

    col10, col11, col12 = st.columns(3)
    with col10:
        st.image(img[9])
        st.subheader(rec[9])
    with col11:
        st.image(img[10])
        st.subheader(rec[10])
    with col12:
        st.image(img[11])
        st.subheader(rec[11])
    st.success("🗣️🔥 Match Found!")

