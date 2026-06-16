from __future__ import annotations
import streamlit as st


def card(title: str, body: str = "", meta: str = "", emoji: str = ""):
    st.markdown(f"""
    <div class='card'>
      <div class='sport-emoji'>{emoji}</div>
      <h3 style='margin:6px 0 6px;color:#061833'>{title}</h3>
      <p class='small'>{body}</p>
      {f"<span class='pill'>{meta}</span>" if meta else ""}
    </div>
    """, unsafe_allow_html=True)


def stat_card(number: str, label: str):
    st.markdown(f"<div class='card'><div class='stat-number'>{number}</div><div class='stat-label'>{label}</div></div>", unsafe_allow_html=True)


def page_header(title: str, subtitle: str):
    st.markdown(f"<div class='eyebrow'>SPORTSPACE</div><div class='section-title'>{title}</div><p class='subtitle' style='font-size:17px'>{subtitle}</p>", unsafe_allow_html=True)


def nav_button(label: str, page: str, key: str):
    if st.sidebar.button(label, key=key):
        st.session_state.page = page
        st.rerun()


def sidebar_nav():
    st.sidebar.markdown("<div class='logo' style='color:white'>SPORTSPACE</div>", unsafe_allow_html=True)
    st.sidebar.caption("Connecting Athletes with Universities")
    st.sidebar.markdown("---")
    nav_button("🏠 Landing", "Landing", "nav_landing")
    nav_button("🧭 Main Menu", "Main Menu", "nav_menu")
    nav_button("🔎 Discover Sports", "Discover Sports", "nav_discover")
    nav_button("🎟️ My Bookings", "My Bookings", "nav_bookings")
    nav_button("💬 Community", "Community", "nav_community")
    nav_button("🏆 Leaderboard", "Leaderboard", "nav_leaderboard")
    nav_button("👤 Profile", "Profile", "nav_profile")
    st.sidebar.markdown("---")
    st.sidebar.caption("Blue Lock energy. Campus sports utility.")
