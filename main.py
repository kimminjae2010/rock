import streamlit as st
import random

st.set_page_config(page_title="가위바위보 게임", page_icon="✊✋✌️")

st.title("✊✋✌️ 가위바위보 게임")
st.write("플레이어 vs AI")

# 선택 옵션
choices = ['가위', '바위', '보']
player_choice = st.selectbox("당신의 선택은?", choices)

# AI 선택 및 결과 계산
if st.button("대결 시작!"):
    ai_choice = random.choice(choices)

    st.write(f"🤖 AI의 선택: **{ai_choice}**")
    st.write(f"🧑 당신의 선택: **{player_choice}**")

    if player_choice == ai_choice:
        result = "😐 비겼습니다!"
    elif (player_choice == '가위' and ai_choice == '보') or \
         (player_choice == '바위' and ai_choice == '가위') or \
         (player_choice == '보' and ai_choice == '바위'):
        result = "🎉 당신이 이겼습니다!"
    else:
        result = "😢 AI가 이겼습니다."

    st.subheader(result)
