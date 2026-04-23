import streamlit as st
import requests
from datetime import datetime
import pandas as pd

# --- PENGATURAN UI ---
st.set_page_config(page_title="SIMPHONY", page_icon="🌱", layout="centered")

st.markdown("""
    <style>
    /* 1. Background Utama */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=1920&auto=format&fit=crop");
        background-attachment: fixed;
        background-size: cover;
    }

    /* 2. Wadah Utama (Membuat Tulisan Terbaca Jelas) */
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.85); /* Putih dengan transparansi 85% */
        padding: 3rem;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-top: 30px;
        margin-bottom: 30px;
        color: #2c3e50; /* Warna teks gelap agar kontras */
    }

    /* 3. Percantik Judul */
    h1, h2, h3 {
        color: #1a5276 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* 4. Percantik Tombol */
    .stButton>button {
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        color: white !important;
        border: none;
        padding: 10px 24px;
        border-radius: 12px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA HALAMAN BERANDA ---
if choice == "🏠 Beranda":
    st.markdown("<h1 style='text-align: center;'>🌱 SIMPHONY</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic;'>Your Safe Space to Grow and Glow</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Gunakan Ilustrasi yang lebih menenangkan
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://img.freepik.com/free-vector/listening-concept-illustration_114360-5942.jpg", 
                 caption="Kami di sini untuk mendengarkanmu tanpa menghakimi.")
    
    st.write("""
    ### Kenapa SIMPHONY ada untukmu?
    Terkadang, beban di sekolah, rumah, atau lingkaran pertemanan terasa berat. **SIMPHONY** hadir sebagai teman setiamu di SMAN 1 Sukatani untuk:
    * **Menampung ceritamu secara anonim.**
    * **Memberikan ruang tenang saat pikiran sedang kacau.**
    * **Menghubungkanmu dengan bantuan profesional jika dibutuhkan.**
    """)
    st.info("Klik menu di samping kiri untuk mulai bercerita.")

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
