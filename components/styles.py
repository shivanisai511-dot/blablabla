import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
:root{--navy:#071B3A;--blue:#0B4DFF;--ink:#050A14;--white:#FFFFFF;--mist:#EEF5FF;--glass:rgba(255,255,255,.72)}
html,body,[class*="css"]{font-family:'Inter',sans-serif!important;color:var(--ink)}
.stApp{background:linear-gradient(135deg,#061833 0%,#0B3470 28%,#F4F8FF 68%,#FFFFFF 100%);background-attachment:fixed;}
.block-container{padding-top:1.2rem;max-width:1280px}.main .block-container{padding-bottom:4rem}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#06152D,#071B3A 55%,#02050B);border-right:1px solid rgba(255,255,255,.14)}
[data-testid="stSidebar"] *{color:white!important}
.hero{padding:54px 48px;border-radius:32px;background:linear-gradient(135deg,rgba(255,255,255,.94),rgba(238,245,255,.78));border:1px solid rgba(255,255,255,.68);box-shadow:0 28px 80px rgba(2,8,23,.25);position:relative;overflow:hidden}
.hero:after{content:"";position:absolute;right:-80px;top:-80px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,rgba(11,77,255,.30),rgba(11,77,255,0));}
.logo{font-weight:900;letter-spacing:.08em;color:#071B3A;font-size:20px}.eyebrow{text-transform:uppercase;letter-spacing:.18em;color:#0B4DFF;font-size:12px;font-weight:800}.title{font-size:68px;line-height:.92;font-weight:900;letter-spacing:-.07em;margin:10px 0;color:#061833}.subtitle{font-size:20px;color:#233957;max-width:760px;line-height:1.6}.section-title{font-size:32px;font-weight:900;letter-spacing:-.04em;color:#061833;margin:18px 0}.card{background:rgba(255,255,255,.78);backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,.72);border-radius:24px;padding:22px;box-shadow:0 18px 50px rgba(7,27,58,.16);transition:transform .18s ease,box-shadow .18s ease,border .18s ease;min-height:120px}.card:hover{transform:translateY(-3px);box-shadow:0 24px 70px rgba(7,27,58,.25);border:1px solid rgba(11,77,255,.25)}.stat-number{font-size:34px;font-weight:900;color:#071B3A}.stat-label{font-size:13px;text-transform:uppercase;letter-spacing:.12em;color:#52657f;font-weight:800}.sport-emoji{font-size:38px}.pill{display:inline-flex;align-items:center;gap:6px;border-radius:999px;background:#EEF5FF;color:#0B4DFF;padding:7px 12px;font-size:12px;font-weight:800;border:1px solid rgba(11,77,255,.12)}.dark-pill{background:#071B3A;color:white;border-radius:999px;padding:8px 13px;font-size:12px;font-weight:800;display:inline-block}.price{font-size:28px;font-weight:900;color:#071B3A}.small{color:#53657e;font-size:14px;line-height:1.55}.metric{font-size:24px;font-weight:900}.success{background:#EAFBF1;color:#0A7A3C}.warn{background:#FFF7E6;color:#A15C00}.danger{background:#FFECEC;color:#B42318}.stButton>button{border-radius:16px!important;border:0!important;background:linear-gradient(135deg,#071B3A,#0B4DFF)!important;color:white!important;font-weight:900!important;padding:.75rem 1.05rem!important;box-shadow:0 12px 28px rgba(11,77,255,.22);transition:all .16s ease;width:100%}.stButton>button:hover{transform:translateY(-2px);box-shadow:0 18px 42px rgba(11,77,255,.32);filter:saturate(1.1)}.stTextInput input,.stSelectbox [data-baseweb="select"],.stDateInput input,.stTimeInput input,.stNumberInput input,.stTextArea textarea{border-radius:15px!important;border:1px solid rgba(7,27,58,.16)!important;background:rgba(255,255,255,.86)!important}.dataframe{border-radius:18px;overflow:hidden}.divider{height:1px;background:linear-gradient(90deg,transparent,rgba(7,27,58,.2),transparent);margin:22px 0}.rank-row{display:flex;align-items:center;justify-content:space-between;padding:14px 16px;border-radius:18px;background:rgba(255,255,255,.72);border:1px solid rgba(255,255,255,.7);margin-bottom:10px}.rank{font-weight:900;font-size:22px;color:#0B4DFF}.footer{padding:20px;text-align:center;color:#62728a}.booking-confirm{border-radius:26px;padding:24px;background:linear-gradient(135deg,#071B3A,#0B4DFF);color:white;box-shadow:0 22px 60px rgba(7,27,58,.35)}
</style>
"""

def apply_styles():
    st.markdown(CSS, unsafe_allow_html=True)


# Visibility Patch
CSS += '''
<style>
p, label, div, span, li, .stMarkdown, .stText, .stCaption {
    color:#0a1730 !important;
    font-weight:500;
}
h1,h2,h3,h4,h5,h6{
    color:#061833 !important;
}
.card{
    background:rgba(255,255,255,.92)!important;
    border:1px solid rgba(0,0,0,.08)!important;
}
.hero{
    background:rgba(255,255,255,.96)!important;
}
[data-testid="stMetricValue"]{
    color:#061833 !important;
    font-weight:900 !important;
}
[data-testid="stMetricLabel"]{
    color:#1d3557 !important;
}
</style>
'''
