import streamlit as st
import requests
import pandas as pd
import google.generativeai as genai
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# --- 1. SETTINGS & AI ---
st.set_page_config(page_title="SIMPHONY - SMAN 1 Sukatani", page_icon="🌱")

if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    ai_model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. CSS STYLING ---
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=1920&auto=format&fit=crop");
        background-size: cover;
    }
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 3rem; border-radius: 20px;
    }
    h1, h2, h3, p { color: #1a5276 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIKA CORE ---
def login_user(u, p):
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read(worksheet="Users", ttl="1m")
        match = df[(df['Username'].astype(str) == str(u)) & (df['Password'].astype(str) == str(p))]
        return not match.empty
    except Exception as e:
        st.error(f"Koneksi GSheet Error: {e}")
        return False

def kirim_pipedream(user, kat, isi):
    url = st.secrets["https://eo5q5f9bo6e6ll1.m.pipedream.net"]
    payload = {
        "tanggal": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "username": user, "kategori": kat, "pesan": isi
    }
    try:
        res = requests.post(url, json=payload)
        return res.status_code == 200
    except: return False

# --- 4. SESSION STATE ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['user'] = ""

# --- 5. HALAMAN ---
if not st.session_state['logged_in']:
    st.title("🌱 Login SIMPHONY")
    u_input = st.text_input("Username")
    p_input = st.text_input("Password", type="password")
    if st.button("Masuk"):
        if login_user(u_input, p_input):
            st.session_state['logged_in'] = True
            st.session_state['user'] = u_input
            st.rerun()
        else:
            st.error("Gagal Login. Cek Username/Password.")
else:
    # --- DASHBOARD ---
    with st.sidebar:
        st.title("🌱 SIMPHONY")
        st.write(f"User: {st.session_state['user']}")
        menu = st.radio("Menu", ["🏠 Beranda", "💬 Curhat", "📩 Balasan", "ℹ️ Info Riset"])
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()

    if menu == "🏠 Beranda":
        st.title("Selamat Datang")
        st.write("Ruang privat aman untuk siswa SMAN 1 Sukatani.")
        st.image("https://img.freepik.com/free-vector/listening-concept-illustration_114360-5942.jpg", width=350)

    elif menu == "💬 Curhat":
        st.header("💬 Curhat Baru")
        kat = st.selectbox("Kategori", ["Bullying", "Keluarga", "Teman", "Pribadi"])
        msg = st.text_area("Ceritakan di sini...")
        if st.button("Kirim"):
            if msg:
                if kirim_pipedream(st.session_state['user'], kat, msg):
                    st.success("Terkirim ke Guru BK!")
                    try:
                        ai_res = ai_model.generate_content(f"Berikan semangat singkat untuk: {msg}").text
                        st.info(f"Pesan AI: {ai_res}")
                    except: pass
                else: st.error("Gagal kirim.")

    elif menu == "📩 Balasan":
        st.header("📩 Kotak Pesan")
        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read(worksheet="Pesan", ttl="1m")
        mine = df[df['Username'].astype(str) == str(st.session_state['user'])]
        if mine.empty: st.info("Belum ada pesan.")
        else:
            for i, r in mine.iterrows():
                with st.expander(f"Curhat {r['Tanggal']}"):
                    st.write(f"**Isi:** {r['Pesan']}")
                    st.success(f"**Balasan:** {r.get('Jawaban_Admin', 'Menunggu balasan...')}")

    elif menu == "ℹ️ Info Riset":
        st.header("ℹ️ Info Riset")
        st.info("The Patterns of Interaction that Occur in the Learning Environment Case Study of SMA Negeri 1 Sukatani")
        st.write("**Peneliti:** Anindya K, Anggun Z, Denisa")
        st.write("**Pembimbing:** Putri Komalasari, S.Pd")
        st.write("**Dev:** Irvan Daviana, S.Pd")
