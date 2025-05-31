import streamlit as st
import random

st.set_page_config(page_title="가위바위보 게임", page_icon="✊✋✌️")

st.title("✊✋✌️ 가위바위보 게임")

# 🤖 AI 이모지 크게 표시 (중앙 정렬, h1 크기)
st.markdown("<h1 style='text-align: center;'>🤖</h1>", unsafe_allow_html=True)

st.write("플레이어 vs AI - 아래 버튼을 눌러 선택하세요!")

# 선택지 정의
choices = ['가위', '바위', '보']
emojis = {'가위': '✌️', '바위': '✊', '보': '✋'}

# CSS 스타일 추가
st.markdown("""
    <style>
    .rps-button {
        display: inline-block;
        font-size: 48px;
        padding: 30px 50px;
        margin: 10px;
        background-color: #f0f2f6;
        border: 2px solid #999;
        border-radius: 15px;
        cursor: pointer;
        text-align: center;
        transition: background-color 0.2s ease;
    }
    .rps-button:hover {
        background-color: #dbe4f0;
    }
    .rps-container {
        display: flex;
        justify-content: center;
        gap: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 버튼 동작 - 폼 사용으로 깔끔하게 처리
with st.form("rps_form", clear_on_submit=True):
    st.markdown('<div class="rps-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        r1 = st.form_submit_button(f"{emojis['가위']} 가위", type="primary")
    with col2:
        r2 = st.form_submit_button(f"{emojis['바위']} 바위", type="primary")
    with col3:
        r3 = st.form_submit_button(f"{emojis['보']} 보", type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

# 선택 결과 처리
player_choice = None
if r1:
    player_choice = '가위'
elif r2:
    player_choice = '바위'
elif r3:
    player_choice = '보'

# 결과 표시
if player_choice:
    ai_choice = random.choice(choices)

    st.markdown(f"<h1>🧑 당신의 선택: {player_choice} {emojis[player_choice]}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h1>🤖 AI의 선택: {ai_choice} {emojis[ai_choice]}</h1>", unsafe_allow_html=True)

    if player_choice == ai_choice:
        result = "😐 비겼습니다!"
    elif (player_choice == '가위' and ai_choice == '보') or \
         (player_choice == '바위' and ai_choice == '가위') or \
         (player_choice == '보' and ai_choice == '바위'):
        result = "🎉 당신이 이겼습니다!"
    else:
        result = "😢 AI가 이겼습니다."

    st.subheader(result)
