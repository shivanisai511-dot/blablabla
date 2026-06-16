from __future__ import annotations

import uuid
from datetime import date, timedelta

import pandas as pd
try:
    import plotly.express as px
except ModuleNotFoundError:
    px = None
import streamlit as st

from components.data import (
    COMMUNITY_POSTS,
    FACILITY_STATS,
    PLAYERS,
    SPORTS,
    USER_PROFILE,
    facilities_for_sport,
    get_facility,
    get_sport,
)
from components.styles import apply_styles
from components.ui import card, page_header, sidebar_nav, stat_card

st.set_page_config(page_title="SPORTSPACE", page_icon="⚡", layout="wide")

@st.cache_resource
def init_styles():
    apply_styles()

init_styles()


def init_state():
    defaults = {
        "page": "Landing",
        "selected_sport": None,
        "selected_university": None,
        "bookings": [],
        "community_posts": COMMUNITY_POSTS.copy(),
        "joined_communities": set(),
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def go(page: str):
    st.session_state.page = page
    st.rerun()


init_state()
sidebar_nav()


def landing_page():
    st.markdown(
        """
        <div class='hero'>
            <div class='logo'>SPORTSPACE</div>
            <div class='eyebrow'>Connecting Athletes with Universities</div>
            <h1 class='title'>Play Hard.<br/>Book Smarter.</h1>
            <p class='subtitle'>A sports-tech platform that helps athletes discover university facilities, book courts and grounds, join communities, and climb the leaderboard — all from one clean dashboard.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    c1, c2, c3, c4 = st.columns(4)
    with c1: stat_card("100+", "Universities")
    with c2: stat_card("500+", "Facilities")
    with c3: stat_card("10,000+", "Athletes")
    with c4: stat_card("20+", "Communities")
    st.write("")
    _, mid, _ = st.columns([1, 1.25, 1])
    with mid:
        if st.button("EXPLORE SPORTSPACE", key="explore_big"):
            go("Main Menu")
    st.markdown("<div class='footer'>Built for campus sport, weekend rivalries, and main-character goals.</div>", unsafe_allow_html=True)


def main_menu():
    page_header("Main Menu", "Choose where you want to go next. Every action is button-based and connected to the booking flow.")
    items = [
        ("Discover Sports", "Find sports, prices, and available university facilities.", "🔎"),
        ("My Bookings", "View confirmed bookings generated during this session.", "🎟️"),
        ("Community", "Find teammates, matches, and campus sports announcements.", "💬"),
        ("Leaderboard", "See top players, universities, and facilities.", "🏆"),
        ("Profile", "View your athlete summary and activity metrics.", "👤"),
    ]
    rows = [st.columns(3), st.columns(2)]
    idx = 0
    for row in rows:
        for col in row:
            if idx >= len(items):
                break
            title, desc, emoji = items[idx]
            with col:
                card(title, desc, emoji=emoji)
                if st.button(f"Open {title}", key=f"menu_{title}"):
                    go(title)
            idx += 1


def discover_sports():
    page_header("Discover Sports", "Pick a sport to view universities and book facilities.")
    for i in range(0, len(SPORTS), 2):
        cols = st.columns(2)
        for col, sport in zip(cols, SPORTS[i : i + 2]):
            with col:
                st.markdown(
                    f"""
                    <div class='card'>
                        <div class='sport-emoji'>{sport['emoji']}</div>
                        <h3 style='margin:0;color:#061833'>{sport['name']}</h3>
                        <p class='small'>{sport['description']}</p>
                        <span class='pill'>Popularity {sport['popularity']}%</span>
                        <span class='pill'>₹{sport['price']}/hour</span>
                        <span class='pill'>{sport['intensity']} intensity</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button("EXPLORE FACILITIES", key=f"explore_{sport['name']}"):
                    st.session_state.selected_sport = sport["name"]
                    go("Facilities")


def facilities_page():
    sport_name = st.session_state.selected_sport
    if not sport_name:
        st.warning("Please select a sport first.")
        if st.button("Go to Discover Sports"):
            go("Discover Sports")
        return
    sport = get_sport(sport_name)
    page_header(f"{sport['emoji']} {sport_name} Facilities", "Universities offering this sport with live sample pricing.")
    facilities = facilities_for_sport(sport_name)
    for i in range(0, len(facilities), 2):
        cols = st.columns(2)
        for col, fac in zip(cols, facilities[i : i + 2]):
            with col:
                st.markdown(
                    f"""
                    <div class='card'>
                        <h3 style='margin:0;color:#061833'>{fac['name']}</h3>
                        <p class='small'>{fac['address']}</p>
                        <span class='pill'>⭐ {fac['rating']}</span>
                        <span class='pill'>₹{fac['price']}/hour</span>
                        <p class='small'><b>Sports:</b> {', '.join(fac['sports'])}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button("BOOK FACILITY", key=f"book_{fac['name']}_{sport_name}"):
                    st.session_state.selected_university = fac["name"]
                    go("Booking")
    if st.button("← Back to Discover Sports"):
        go("Discover Sports")


def booking_page():
    sport_name = st.session_state.selected_sport
    uni_name = st.session_state.selected_university
    if not sport_name or not uni_name:
        st.warning("Please select a sport and university before booking.")
        if st.button("Start Booking Flow"):
            go("Discover Sports")
        return
    fac = get_facility(uni_name, sport_name)
    page_header("Confirm Booking", "Choose your date, time, and duration. SPORTSPACE calculates the total instantly.")
    left, right = st.columns([1.1, .9])
    with left:
        st.markdown(
            f"""
            <div class='card'>
                <h3 style='margin:0;color:#061833'>{sport_name} at {uni_name}</h3>
                <p class='small'>{fac['address']}</p>
                <span class='pill'>₹{fac['price']}/hour</span>
                <span class='pill'>⭐ {fac['rating']}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        booking_date = st.date_input("Select Date", value=date.today(), min_value=date.today(), max_value=date.today() + timedelta(days=30))
        time_slots = ["06:00 AM", "07:00 AM", "08:00 AM", "09:00 AM", "10:00 AM", "04:00 PM", "05:00 PM", "06:00 PM", "07:00 PM", "08:00 PM", "09:00 PM"]
        booking_time = st.selectbox("Select Time Slot", time_slots, index=7)
        duration = st.selectbox("Duration", [1, 2, 3, 4], format_func=lambda x: f"{x} hour{'s' if x > 1 else ''}")
    total = fac["price"] * duration
    with right:
        st.markdown(
            f"""
            <div class='booking-confirm'>
                <h2 style='margin:0;color:white'>Booking Summary</h2>
                <p><b>Sport:</b> {sport_name}</p>
                <p><b>University:</b> {uni_name}</p>
                <p><b>Date:</b> {booking_date}</p>
                <p><b>Time:</b> {booking_time}</p>
                <p><b>Duration:</b> {duration} hour(s)</p>
                <h1 style='color:white'>₹{total}</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("CONFIRM BOOKING", key="confirm_booking"):
            booking_id = "SS-" + uuid.uuid4().hex[:8].upper()
            st.session_state.bookings.append(
                {
                    "Booking ID": booking_id,
                    "Sport": sport_name,
                    "University": uni_name,
                    "Date": str(booking_date),
                    "Time": booking_time,
                    "Duration": f"{duration} hour(s)",
                    "Total Price": f"₹{total}",
                }
            )
            st.success(f"Booking confirmed! Your Booking ID is {booking_id}")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Book Another Sport"):
            go("Discover Sports")
    with c2:
        if st.button("View My Bookings"):
            go("My Bookings")


def my_bookings():
    page_header("My Bookings", "Your confirmed facility bookings for this session.")
    if not st.session_state.bookings:
        st.info("No bookings yet. Complete the Sport → University → Booking flow to see reservations here.")
        if st.button("Discover Sports"):
            go("Discover Sports")
        return
    df = pd.DataFrame(st.session_state.bookings)
    st.dataframe(df, use_container_width=True, hide_index=True)
    total_amount = sum(int(b["Total Price"].replace("₹", "")) for b in st.session_state.bookings if b["Total Price"].startswith("₹"))
    c1, c2, c3 = st.columns(3)
    with c1: stat_card(str(len(df)), "Total Bookings")
    with c2: stat_card(f"₹{total_amount}", "Total Spend")
    with c3: stat_card(str(sum(int(b["Duration"].split()[0]) for b in st.session_state.bookings if b["Duration"].startswith("Hour") or b["Duration"].startswith("1") or b["Duration"].startswith("2") or b["Duration"].startswith("3") or b["Duration"].startswith("4"))), "Hours Booked")


def community():
    page_header("Community", "Find players, join matches, and ask the campus sports network.")
    with st.expander("Ask The Community", expanded=True):
        title = st.text_input("Post title", placeholder="Need one goalkeeper tonight")
        body = st.text_area("Post details", placeholder="Share timing, location, skill level, and contact preference.")
        tag = st.selectbox("Sport tag", [s["name"] for s in SPORTS])
        if st.button("Post to Community"):
            if title.strip() and body.strip():
                st.session_state.community_posts.insert(0, {"title": title, "body": body, "tag": tag, "spots": 1})
                st.success("Posted to the community feed.")
                st.rerun()
            else:
                st.error("Please add both a title and details.")
    for idx, post in enumerate(st.session_state.community_posts):
        post_key = f"{post['title']}_{post['tag']}"
        is_joined = post_key in st.session_state.joined_communities
        st.markdown(
            f"""
            <div class='card'>
                <span class='pill'>{post['tag']}</span>
                <h3 style='margin:10px 0 4px;color:#061833'>{post['title']}</h3>
                <p class='small'>{post['body']}</p>
                <span class='dark-pill'>{post['spots']} spot(s) open</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if is_joined:
            st.markdown("<div style='background:#10B981;color:white;padding:10px;border-radius:8px;font-weight:bold;text-align:center'>✓ Already Joined</div>", unsafe_allow_html=True)
        else:
            if st.button("JOIN", key=f"join_community_{idx}_{post['title']}"):
                join_id = "CJ-" + uuid.uuid4().hex[:8].upper()
                st.session_state.bookings.append(
                    {
                        "Booking ID": join_id,
                        "Sport": post['tag'],
                        "University": "Community Activity",
                        "Date": str(date.today()),
                        "Time": "TBD",
                        "Duration": "Community",
                        "Total Price": "Community Join",
                    }
                )
                st.session_state.joined_communities.add(post_key)
                st.success(f"Joined successfully! ✓")
                st.rerun()
        st.write("")


@st.cache_data
def get_leaderboard_charts():
    df = pd.DataFrame(FACILITY_STATS)
    fig = px.bar(df, x="name", y="bookings", hover_data=["rating"], title="Top Facilities by Bookings")
    fig.update_layout(xaxis_title="Facility", yaxis_title="Bookings", height=420, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(255,255,255,.55)")
    
    df_uni = pd.DataFrame([{"University": f["name"], "Rating": f["rating"], "Booking Index": f["bookings"]} for f in FACILITY_STATS])
    fig2 = px.scatter(df_uni, x="Rating", y="Booking Index", size="Booking Index", text="University", title="Top Universities: Rating vs Booking Activity")
    fig2.update_traces(textposition="top center")
    fig2.update_layout(height=420, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(255,255,255,.55)")
    
    return fig, fig2

def leaderboard():
    page_header("Leaderboard", "Top players, universities, and facilities based on sample activity data.")
    left, right = st.columns([.9, 1.1])
    with left:
        st.subheader("Top Players")
        for p in PLAYERS:
            st.markdown(f"<div class='rank-row'><span><b class='rank'>#{p['rank']}</b> &nbsp; {p['name']} <span class='small'>({p['sport']})</span></span><b>{p['points']} pts</b></div>", unsafe_allow_html=True)
    with right:
        fig, fig2 = get_leaderboard_charts()
        st.plotly_chart(fig, use_container_width=True)
    fig, fig2 = get_leaderboard_charts()
    st.plotly_chart(fig2, use_container_width=True)


def calculate_total_hours(bookings):
    if not bookings:
        return 0
    total = 0
    for b in bookings:
        duration = b.get("Duration", "") if isinstance(b, dict) else ""
        parts = duration.split()
        if parts and parts[0].isdigit():
            total += int(parts[0])
    return total

def profile():
    page_header("Profile", "Your athlete activity summary.")
    bookings = st.session_state.bookings
    total_hours = calculate_total_hours(bookings) if bookings else 0
    c1, c2 = st.columns([.9, 1.1])
    with c1:
        st.markdown(
            f"""
            <div class='card'>
              <h2 style='margin:0;color:#061833'>{USER_PROFILE['name']}</h2>
              <p class='small'>Campus athlete · SPORTSPACE member</p>
              <p><b>Favourite Sports:</b> {', '.join(USER_PROFILE['favourite_sports'])}</p>
              <span class='pill'>Blue Lock Mode: ON</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        a, b, c = st.columns(3)
        with a: stat_card(str(len(bookings)), "Total Bookings")
        with b: stat_card(str(total_hours), "Hours Played")
        with c: stat_card(str(USER_PROFILE["communities_joined"]), "Communities Joined")
    st.subheader("Recent Activity")
    if bookings:
        st.dataframe(pd.DataFrame(bookings).tail(5), use_container_width=True, hide_index=True)
    else:
        st.info("No booking activity yet. Go discover a sport and make your first reservation.")


PAGES = {
    "Landing": landing_page,
    "Main Menu": main_menu,
    "Discover Sports": discover_sports,
    "Facilities": facilities_page,
    "Booking": booking_page,
    "My Bookings": my_bookings,
    "Community": community,
    "Leaderboard": leaderboard,
    "Profile": profile,
}

PAGES.get(st.session_state.page, landing_page)()
