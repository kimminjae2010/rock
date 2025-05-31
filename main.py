# 세션 상태 초기화
if 'win' not in st.session_state:
    st.session_state.win = 0
    st.session_state.lose = 0
    st.session_state.draw = 0
    st.session_state.streak_count = 0
    st.session_state.streak_type = None  # 'win', 'lose', or None

# ... 생략 (선택, 버튼 등)

# 게임 실행
if player_choice:
    ai_choice = random.choice(choices)

    st.markdown(f"<h1>🧑 당신의 선택: {player_choice} {emojis[player_choice]}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h1>🤖 AI의 선택: {ai_choice} {emojis[ai_choice]}</h1>", unsafe_allow_html=True)

    if player_choice == ai_choice:
        result = "😐 비겼습니다!"
        st.session_state.draw += 1
        st.session_state.streak_type = None
        st.session_state.streak_count = 0
    elif (player_choice == '가위' and ai_choice == '보') or \
         (player_choice == '바위' and ai_choice == '가위') or \
         (player_choice == '보' and ai_choice == '바위'):
        result = "🎉 당신이 이겼습니다!"
        st.session_state.win += 1
        if st.session_state.streak_type == "win":
            st.session_state.streak_count += 1
        else:
            st.session_state.streak_type = "win"
            st.session_state.streak_count = 1
    else:
        result = "😢 AI가 이겼습니다."
        st.session_state.lose += 1
        if st.session_state.streak_type == "lose":
            st.session_state.streak_count += 1
        else:
            st.session_state.streak_type = "lose"
            st.session_state.streak_count = 1

    st.subheader(result)

# 승률 표시
total_games = st.session_state.win + st.session_state.lose + st.session_state.draw
if total_games > 0:
    win_rate = st.session_state.win / total_games * 100
    st.markdown("---")
    st.markdown(f"<h1>📈 승률: {win_rate:.1f}%</h1>", unsafe_allow_html=True)

    # 전적 요약
    st.markdown("### 📊 전적 요약")
    st.write(f"- 🏆 승: {st.session_state.win}")
    st.write(f"- ❌ 패: {st.session_state.lose}")
    st.write(f"- 🤝 무: {st.session_state.draw}")

# 연승/연패 표시 (맨 아래)
if st.session_state.streak_type == "win":
    st.markdown(f"### 🔥 현재 **{st.session_state.streak_count}연승** 중!")
elif st.session_state.streak_type == "lose":
    st.markdown(f"### 💦 현재 **{st.session_state.streak_count}연패** 중!")
