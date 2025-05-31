import streamlit as st
import random

st.set_page_config(page_title="가위바위보 게임", page_icon="✊✋✌️")

st.title("✊✋✌️ 가위바위보 게임")
st.write("플레이어 vs AI - 버튼을 눌러 선택하세요!")

# 선택지
choices = ['가위', '바위', '보']
emojis = {'가위': '✌️', '바위': '✊', '보': '✋'}

# 버튼 레이아웃
col1, col2, col3 = st.columns(3)

player_choice = None

with col1:
    if st.button(f"{emojis['가위']} 가위"):
        player_choice = '가위'
with col2:
    if st.button(f"{emojis['바위']} 바위"):
        player_choice = '바위'
with col3:
    if st.button(f"{emojis['보']} 보"):
        player_choice = '보'

# 게임 로직
if player_choice:
    ai_choice = random.choice(choices)

    st.write("---")
    st.write(f"🤖 AI의 선택: **{ai_choice} {emojis[ai_choice]}**")
    st.write(f"🧑 당신의 선택: **{player_choice} {emojis[player_choice]}**")

    if player_choice == ai_choice:
        result = "😐 비겼습니다!"
    elif (player_choice == '가위' and ai_choice == '보') or \
         (player_choice == '바위' and ai_choice == '가위') or \
         (player_choice == '보' and ai_choice == '바위'):
        result = "🎉 당신이 이겼습니다!"
    else:
        result = "😢 AI가 이겼습니다."

    st.subheader(result)
