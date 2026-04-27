import streamlit as st
import requests
import pandas as pd
import google.generativeai as genai
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# --- 1. KONFIGURASI AI & KONEKSI ---
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    ai_model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.warning("Konfigurasi AI sedang disiapkan...")

# --- 2. FUNGSI INTI (PIPEDREAM & AI) ---
def kirim_ke_pipedream(username, kategori, pesan):
    """Mengirim data ke Google Sheets melalui Pipedream"""
    try:
        url = st.secrets["https://eo5q5f9bo6e6ll1.m.pipedream.net"]
        payload = {
            "tanggal": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "username": username,
            "kategori": kategori,
            "pesan": pesan
        }
        response = requests.post(url, json=payload)
        return response.status_code == 200
    except:
        return False

def dapatkan_saran_ai(pesan_siswa):
    """Jawaban otomatis dari Gemini AI"""
    prompt = f"Berikan tanggapan empati singkat untuk siswa yang sedang merasa: '{pesan_siswa}' (Maks 3 kalimat)."
    try:
        return ai_model.generate_content(prompt).text
    except:
        return "Terima kasih sudah berbagi cerita. Kamu sangat berani!"

# --- 3. UI STYLING ---
st.set_page_config(page_title="SIMPHONY - SMAN 1 Sukatani", page_icon="🌱")

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=1920&auto=format&fit=crop");
        background-size: cover;
    }
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 3rem; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    h1, h2, h3, p { color: #1a5276 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. LOGIKA LOGIN ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = ""

if not st.session_state['logged_in']:
    st.title("🌱 Login SIMPHONY")
    u = st.text_input("Username (NISN)")
    p = st.text_input("Password", type="password")
    if st.button("Masuk"):
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            users_df = conn.read(worksheet="Users", ttl="1m")
            if not users_df[(users_df['Username'].astype(str) == str(u)) & (users_df['Password'].astype(str) == str(p))].empty:
                st.session_state['logged_in'] = True
                st.session_state['username'] = u
                st.rerun()
            else: st.error("Login Gagal.")
        except: st.error("Gagal terhubung ke database User.")

else:
    # --- 5. DASHBOARD UTAMA ---
    with st.sidebar:
        st.title("🌱 SIMPHONY")
        st.write(f"Halo, **{st.session_state['username']}**")
        st.divider()
        menu = st.radio("Menu Navigasi:", ["🏠 Beranda", "💬 Curhat Baru", "📩 Pesan & Balasan", "ℹ️ Info Riset", "🆘 Bantuan"])
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()

    if menu == "🏠 Beranda":
        st.title("Selamat Datang")
        st.write("SIMPHONY adalah ruang privatmu untuk bercerita tentang interaksi dan tantangan di sekolah.")
        st.image("https://img.freepik.com/free-vector/listening-concept-illustration_114360-5942.jpg", width=400)

    elif menu == "💬 Curhat Baru":
        st.header("💬 Teman Cerita")
        kat = st.selectbox("Kategori:", ["Keluarga", "Bullying", "Pertemanan", "Pribadi"])
        isi = st.text_area("Apa yang ingin kamu sampaikan hari ini?")
        if st.button("Kirim Cerita"):
            if isi:
                with st.spinner("Memproses..."):
                    saran = dapatkan_saran_ai(isi)
                    if kirim_ke_pipedream(st.session_state['username'], kat, isi):
                        st.success("Terkirim ke database via Pipedream!")
                        st.info(f"**Pesan Konselor AI:** {saran}")
                    else: st.error("Gagal kirim. Cek URL Pipedream.")
            else: st.warning("Isi dulu ceritanya ya.")

    elif menu == "📩 Pesan & Balasan":
        st.header("📩 Kotak Pesanku")
        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read(worksheet="Pesan", ttl="1m")
        pribadi = df[df['Username'].astype(str) == str(st.session_state['username'])]
        if pribadi.empty: st.info("Belum ada riwayat curhat.")
        else:
            for i, row in pribadi.iterrows():
                with st.expander(f"Curhat pada {row['Tanggal']}"):
                    st.write(f"**Pesan:** {row['Pesan']}")
                    st.success(f"**Balasan Guru BK:** {row.get('Jawaban_Admin', 'Sedang menunggu antrean balasan.')}")

    elif menu == "ℹ️ Info Riset":
        st.header("ℹ️ Informasi Pengembangan & Riset")
        st.markdown("### Judul Penelitian")
        st.info("**The Patterns of Interaction that Occur in the Learning Environment Case Study of SMA Negeri 1 Sukatani**")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("### 📝 Tim Peneliti")
            st.markdown("- **Anindya Kharisma Putri**\n- **Anggun Zulfa Qurrotul Aini**\n- **Denisa**")
        with col2:
            st.write("### 👩‍🏫 Pembimbing")
            st.markdown("**Putri Komalasari, S.Pd**")
            
        st.write("---")
        st.write("### 💻 Pengembang Aplikasi")
        st.success("**Irvan Daviana, S.Pd**")
        st.markdown("""
        Aplikasi **SIMPHONY** dikembangkan untuk memfasilitasi interaksi sosial yang sehat 
        di lingkungan SMAN 1 Sukatani, memberikan ruang bagi siswa untuk berbagi tanpa rasa takut.
        """)

    elif menu == "🆘 Bantuan":
        st.header("🆘 Pusat Bantuan")
        st.write("Jika butuh bantuan segera, silakan hubungi Ruang BK SMAN 1 Sukatani.")
