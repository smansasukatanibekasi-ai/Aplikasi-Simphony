import streamlit as st
import requests
from datetime import datetime
import pandas as pd

# --- 1. PENGATURAN HALAMAN & BACKGROUND ---
st.set_page_config(page_title="SIMPHONY - SMAN 1 Sukatani", page_icon="🌱", layout="centered")

st.markdown("""
    <style>
    /* Background Utama */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=1920&auto=format&fit=crop");
        background-attachment: fixed;
        background-size: cover;
    }

    /* Wadah Konten (Glassmorphism agar tulisan terbaca) */
    .main .block-container {
        background-color: rgb(255, 255, 255); 
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
        margin-top: 50px;
    }

    /* Memperjelas teks */
    h1, h2, h3, p, span, label {
        color: #f2f7f4 !important;
    }

    /* Tombol Cantik */
    .stButton>button {
        background: linear-gradient(45deg, #2ecc71, #27ae60);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. FUNGSI KIRIM DATA (PIPEDREAM) ---
def kirim_ke_jembatan(kategori, pesan):
    # GANTI URL DI BAWAH INI DENGAN URL PIPEDREAM ANDA
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

# --- 3. SIDEBAR (NAVIGASI) ---
with st.sidebar:
    st.markdown("## 🌱 SIMPHONY")
    st.write("Harmony in Growth")
    st.write("---")
    # Variabel 'choice' didefinisikan di sini
    choice = st.radio("Pilih Menu:", ["🏠 Beranda", "💬 Teman Cerita", "📚 Sudut Tenang", "🆘 Pusat Bantuan", "ℹ️ Informasi Riset"])

# --- 4. LOGIKA HALAMAN ---
if choice == "🏠 Beranda":
    st.markdown("<h1 style='text-align: center;'>Selamat Datang di SIMPHONY</h1>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        # Ilustrasi yang lebih bersahabat
        st.image("https://img.freepik.com/free-vector/hand-drawn-mental-health-awareness-concept_23-2148531012.jpg")
    
    st.markdown("""
    ### Hai, Siswa SMAN 1 Sukatani! 
    Punya sesuatu yang mengganjal di pikiran? Masalah pertemanan, keluarga, atau merasa tidak nyaman karena *bullying*? 
    
    **SIMPHONY** adalah ruang amanmu. Di sini kamu bisa:
    1. **Bercerita secara Anonim** (Identitasmu rahasia).
    2. **Mendapatkan Ketenangan** melalui konten positif.
    3. **Mencari Bantuan** tanpa merasa dihakimi.
    """)

elif choice == "💬 Teman Cerita":
    st.header("💬 Teman Cerita")
    st.write("Tuangkan perasaanmu di sini. Kami mendengarkan.")
    
    kat = st.selectbox("Kategori Masalah:", ["Keluarga", "Circle Pertemanan", "Bullying", "Internal/Pribadi"])
    cerita = st.text_area("Apa yang ingin kamu ceritakan?", height=150)
    
    if st.button("Kirim Cerita secara Anonim"):
        if cerita:
            with st.spinner('Mengirim cerita...'):
                berhasil = kirim_ke_jembatan(kat, cerita)
                if berhasil:
                    st.success("Terima kasih sudah berbagi. Ceritamu sudah kami terima dengan aman.")
                else:
                    st.error("Maaf, terjadi gangguan koneksi. Coba lagi nanti ya.")
        else:
            st.warning("Ceritanya diisi dulu ya...")

elif choice == "📚 Sudut Tenang":
    st.header("📚 Sudut Tenang")
    st.info("Ambil nafas dalam-dalam... Kamu hebat sudah bertahan sampai hari ini.")
    st.write("Berikut video relaksasi untukmu:")
    st.video("https://www.youtube.com/watch?v=mUNv_E7E9fM")

elif choice == "🆘 Pusat Bantuan":
    st.header("🆘 Pusat Bantuan")
    st.write("Jika kamu merasa butuh bantuan segera, jangan ragu hubungi:")
    st.error("Guru BK SMAN 1 Sukatani: (Hubungi Ruang BK)")
    st.warning("Layanan Konseling Sebaya: (Segera Hadir)")
elif choice == "ℹ️ Informasi Riset":
    st.header("ℹ️ Informasi Pengembangan & Riset")
    st.write("Aplikasi ini dikembangkan berdasarkan penelitian ilmiah untuk menciptakan lingkungan sekolah yang lebih harmonis.")
    
    # Wadah Informasi Penelitian
    st.info("### Judul Penelitian")
    st.markdown("""
    **"The Patterns of Interaction that Occur in the Learning Environment: Case Study of SMA Negeri 1 Sukatani"**
    """)
    
    # Tim Peneliti dalam kolom agar rapi
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 📝 Tim Peneliti")
        st.markdown("""
        * **Anindya Kharisma Putri**
        * **Anggun Zulfa Qurrotul Aini**
        * **Denisa**
        """)
    
    with col2:
        st.write("### 👩‍🏫 Pembimbing")
        st.write("**Putri Komalasari, S.Pd**")

    st.write("---")
    
    # Informasi Pengembang
    st.write("### 💻 Pengembang Aplikasi")
    st.success("**Irvan Daviana, S.Pd**")
