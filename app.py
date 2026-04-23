import streamlit as st
import requests
from datetime import datetime
import pandas as pd

# --- 1. PENGATURAN HALAMAN & BACKGROUND ---
st.set_page_config(page_title="SIMPHONY - SMAN 1 Sukatani", page_icon="🌱", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
        background-attachment: fixed;
        background-size: cover;
    }
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem 3rem;
        border-radius: 20px;
        margin-top: 2rem;
    }
    /* Warna font tombol utama agar cerah */
    .stButton>button {
        background-color: #01579b;
        color: white !important;
        font-weight: bold;
        border-radius: 12px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. FUNGSI KIRIM DATA (VIA PIPEDREAM) ---
def kirim_ke_jembatan(kategori, pesan):
    # Masukkan URL dari Pipedream Anda di sini
    url_pipedream = "https://eo5q5f9bo6e6ll1.m.pipedream.net" 
    
    data = {
        "tanggal": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "kategori": kategori,
        "pesan": pesan
    }
    
    try:
        response = requests.post(url_pipedream, json=data)
        return response.status_code == 200
    except:
        return False

# --- 3. NAVIGASI SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=100)
    st.title("Menu SIMPHONY")
    choice = st.radio("Pilih Halaman:", ["🏠 Beranda", "💬 Teman Cerita", "📚 Sudut Tenang", "🆘 Pusat Bantuan"])

# --- 4. LOGIKA HALAMAN ---

if choice == "🏠 Beranda":
    st.title("🌱 SIMPHONY")
    st.subheader("Selamat Datang di Ruang Aman Siswa SMAN 1 Sukatani")
    st.write("---")
    st.image("https://images.unsplash.com/photo-1516062423079-7ca13cdc7f5a?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80")
    st.info("Aplikasi ini adalah wadah anonim untuk berbagi cerita dan mencari dukungan mental tanpa rasa takut.")

elif choice == "💬 Teman Cerita":
    st.header("💬 Teman Cerita (Anonim)")
    st.write("Apapun yang kamu tulis di sini akan terjaga kerahasiaannya.")
    
    kat = st.selectbox("Pilih Kategori:", ["Keluarga", "Pertemanan (Circle)", "Bullying", "Masalah Pribadi"])
    cerita = st.text_area("Apa yang ingin kamu sampaikan hari ini?", height=200)
    
    if st.button("Kirim Cerita"):
        if cerita:
            with st.spinner('Menghubungkan ke sistem...'):
                hasil = kirim_ke_jembatan(kat, cerita)
                if hasil:
                    st.success("✅ Cerita berhasil dikirim secara aman. Kamu tidak sendirian!")
                else:
                    st.error("❌ Gagal mengirim. Pastikan URL Pipedream sudah benar.")
        else:
            st.warning("Tulis ceritamu dulu ya...")

elif choice == "📚 Sudut Tenang":
    st.header("📚 Sudut Tenang")
    st.write("Kumpulan motivasi untukmu:")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

elif choice == "🆘 Pusat Bantuan":
    st.header("🆘 Pusat Bantuan")
    st.write("Butuh teman bicara langsung? Konselor kami siap membantu.")
    st.success("Ibu Guru BK: 0812-xxxx-xxxx")
