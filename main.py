import streamlit as st
import random

st.set_page_config(page_title="가위바위보 게임", page_icon="✊✋✌️")

st.title("✊✋✌️ 가위바위보 게임")

if 'win' not in st.session_state:
    st.session_state.win = 0
    st.session_state.lose = 0
    st.session_state.draw = 0

choices = ['가위', '바위', '보']
emojis = {'가위': '✌️', '바위': '✊', '보': '✋'}

# 상단에 버튼 영역(왼쪽)과 승률/전적 영역(오른쪽)
left_col, right_col = st.columns([2, 1])

with left_col:
    st.write("플레이어 vs AI - 아래 버튼을 눌러 선택하세요!")
    with st.form("rps_form", clear_on_submit=True):
        st.markdown('<div style="display: flex; justify-content: start; gap: 20px;">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            r1 = st.form_submit_button(f"{emojis['가위']} 가위", type="primary")
        with col2:
            r2 = st.form_submit_button(f"{emojis['바위']} 바위", type="primary")
        with col3:
            r3 = st.form_submit_button(f"{emojis['보']} 보", type="primary")
        st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    total_games = st.session_state.win + st.session_state.lose + st.session_state.draw
    if total_games > 0:
        win_rate = st.session_state.win / total_games * 100
        st.markdown(
            """
            <div style="text-align: right; margin-right: 0; width: 100%; max-width: 300px;">
            """,
            unsafe_allow_html=True
        )
        st.markdown("### 📈 승률")
        st.markdown(f"<h2>{win_rate:.1f}%</h2>", unsafe_allow_html=True)
        st.markdown("### 📊 전적 요약")
        st.write(f"- 🏆 승: {st.session_state.win}")
        st.write(f"- ❌ 패: {st.session_state.lose}")
        st.write(f"- 🤝 무: {st.session_state.draw}")
        st.markdown("</div>", unsafe_allow_html=True)

# 플레이어 선택 처리
player_choice = None
if r1:
    player_choice = '가위'
elif r2:
    player_choice = '바위'
elif r3:
    player_choice = '보'

# 게임 실행 결과를 화면 하단에 출력하기 위해 별도 영역 저장
result = None
ai_choice = None

if player_choice:
    ai_choice = random.choice(choices)

    if player_choice == ai_choice:
        result = "😐 비겼습니다!"
        st.session_state.draw += 1
    elif (player_choice == '가위' and ai_choice == '보') or \
         (player_choice == '바위' and ai_choice == '가위') or \
         (player_choice == '보' and ai_choice == '바위'):
        result = "🎉 당신이 이겼습니다!"
        st.session_state.win += 1
    else:
        result = "😢 AI가 이겼습니다."
        st.session_state.lose += 1

# 화면 하단에 결과 출력
if result and ai_choice:
    st.markdown("---")
    st.markdown(f"<h1>🧑 당신의 선택: {player_choice} {emojis[player_choice]}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h1>🤖 AI의 선택: {ai_choice} {emojis[ai_choice]}</h1>", unsafe_allow_html=True)
    st.subheader(result)
