from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Dict, List
import streamlit as st

SPORTS: List[Dict] = [
    {"name":"Football","emoji":"⚽","description":"Full-size turf battles for squads chasing peak performance.","popularity":96,"price":1200,"intensity":"High"},
    {"name":"Cricket","emoji":"🏏","description":"Premium nets and open grounds for match practice and tournaments.","popularity":94,"price":1500,"intensity":"Medium"},
    {"name":"Box Cricket","emoji":"🥎","description":"Compact floodlit arenas for fast, energetic short-format cricket.","popularity":88,"price":900,"intensity":"Medium"},
    {"name":"Basketball","emoji":"🏀","description":"Indoor and outdoor courts for pickup games, training, and leagues.","popularity":90,"price":1000,"intensity":"High"},
    {"name":"Volleyball","emoji":"🏐","description":"Well-marked courts built for team play, drills, and weekend matches.","popularity":81,"price":850,"intensity":"Medium"},
    {"name":"Tennis","emoji":"🎾","description":"Hard courts with coaching-friendly slots and competitive match play.","popularity":84,"price":1100,"intensity":"Medium"},
    {"name":"Badminton","emoji":"🏸","description":"Indoor wooden courts for singles, doubles, and casual rallies.","popularity":92,"price":750,"intensity":"Medium"},
    {"name":"Pickleball","emoji":"🏓","description":"Fast-growing social sport with beginner-friendly university courts.","popularity":73,"price":700,"intensity":"Low"},
    {"name":"Swimming","emoji":"🏊","description":"Lane-booking access to clean, monitored university pools.","popularity":79,"price":950,"intensity":"Medium"},
    {"name":"Athletics","emoji":"🏃","description":"Tracks and field zones for sprinting, endurance, jumps, and training.","popularity":76,"price":650,"intensity":"High"},
]

UNIVERSITIES: List[Dict] = [
    {"name":"IIT Hyderabad","address":"Kandi, Sangareddy, Telangana","rating":4.8,"base":1.05,"sports":["Football","Cricket","Basketball","Badminton","Athletics","Tennis"]},
    {"name":"IIT Bombay","address":"Powai, Mumbai, Maharashtra","rating":4.9,"base":1.18,"sports":["Football","Cricket","Basketball","Swimming","Tennis","Badminton"]},
    {"name":"IIT Delhi","address":"Hauz Khas, New Delhi","rating":4.7,"base":1.15,"sports":["Football","Box Cricket","Basketball","Volleyball","Badminton","Athletics"]},
    {"name":"IIT Madras","address":"Sardar Patel Road, Chennai, Tamil Nadu","rating":4.9,"base":1.12,"sports":["Football","Cricket","Swimming","Tennis","Badminton","Athletics"]},
    {"name":"BITS Pilani","address":"Vidya Vihar, Pilani, Rajasthan","rating":4.6,"base":1.00,"sports":["Cricket","Football","Basketball","Volleyball","Tennis","Pickleball"]},
    {"name":"VIT","address":"Katpadi, Vellore, Tamil Nadu","rating":4.5,"base":0.96,"sports":["Football","Box Cricket","Basketball","Badminton","Swimming","Volleyball"]},
    {"name":"SRM","address":"Kattankulathur, Chennai, Tamil Nadu","rating":4.4,"base":0.92,"sports":["Cricket","Box Cricket","Football","Basketball","Badminton","Pickleball"]},
    {"name":"NIT Trichy","address":"Tiruchirappalli, Tamil Nadu","rating":4.7,"base":0.98,"sports":["Football","Cricket","Volleyball","Athletics","Badminton","Tennis"]},
]

COMMUNITY_POSTS = [
    {"title":"Need 2 football players","body":"7 PM turf match at IIT Madras. Midfielders preferred, chaos tolerated.","tag":"Football","spots":2},
    {"title":"Weekend cricket match","body":"Friendly 8-over match this Saturday. Bring your A-game and one terrible joke.","tag":"Cricket","spots":5},
    {"title":"Looking for badminton partner","body":"Intermediate doubles practice near VIT indoor court.","tag":"Badminton","spots":1},
    {"title":"Basketball tournament registrations open","body":"3v3 university league registrations close Friday night.","tag":"Basketball","spots":12},
]

PLAYERS = [
    {"rank":1,"name":"Arjun Rao","sport":"Football","points":2460},
    {"rank":2,"name":"Meera Iyer","sport":"Badminton","points":2325},
    {"rank":3,"name":"Kabir Singh","sport":"Basketball","points":2190},
    {"rank":4,"name":"Ananya Nair","sport":"Swimming","points":2045},
    {"rank":5,"name":"Rohan Das","sport":"Cricket","points":1988},
]

FACILITY_STATS = [
    {"name":"IIT Bombay Sports Complex","bookings":412,"rating":4.9},
    {"name":"IIT Madras Aquatics + Courts","bookings":389,"rating":4.9},
    {"name":"IIT Delhi Arena","bookings":344,"rating":4.7},
    {"name":"VIT Indoor Sports Hub","bookings":310,"rating":4.5},
    {"name":"BITS Pilani Courts","bookings":286,"rating":4.6},
]

USER_PROFILE = {
    "name": "Demo Athlete",
    "favourite_sports": ["Football", "Badminton", "Basketball"],
    "communities_joined": 4,
}

import streamlit as st

@st.cache_data
def get_sport(name: str) -> Dict:
    return next(s for s in SPORTS if s["name"] == name)

@st.cache_data
def facilities_for_sport(sport_name: str) -> List[Dict]:
    sport = get_sport(sport_name)
    facilities = []
    for uni in UNIVERSITIES:
        if sport_name in uni["sports"]:
            facilities.append({
                **uni,
                "price": int(round(sport["price"] * uni["base"] / 10) * 10),
            })
    return facilities

@st.cache_data
def get_facility(name: str, sport_name: str) -> Dict:
    return next(f for f in facilities_for_sport(sport_name) if f["name"] == name)

def next_available_dates(days: int = 10):
    today = date.today()
    return [today + timedelta(days=i) for i in range(days)]
