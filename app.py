import streamlit as st

# --- PENGATURAN HALAMAN ---
st.set_page_config(page_title="SIMPHONY - SMAN 1 Sukatani", page_icon="🌱", layout="wide")

# --- CUSTOM CSS (Background & Gaya Visual) ---
st.markdown("""
    <style>
    /* Background untuk seluruh aplikasi */
    .stApp {
        background-image: url("https://www.pexels.com/video/scenic-aerial-view-of-swiss-alpine-landscape-35108054/");
        background-attachment: fixed;
        background-size: cover;
    }
    
    /* Kotak konten utama agar transparan dan elegan */
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem 3rem;
        border-radius: 15px;
        margin-top: 2rem;
    }

    /* Gaya sidebar */
    [data-testid="stSidebar"] {
        background-color: #1a1c24; /* Warna abu-abu sangat gelap */
        color: white; /* Agar tulisan di sidebar jadi putih */
    }

    /* Warna font pada tombol kirim agar cerah dan kontras */
    .stButton>button {
        background-color: #01579b;
        color: blue !important;
        font-white: bold;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 1rem;
    }
    
    .stButton>button:hover {
        background-color: #0288d1;
        color: blue !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- JUDUL & NAVIGASI SAMPING (SIDEBAR) ---
st.sidebar.title("🌱 SIMPHONY")
st.sidebar.write("SMA Negeri 1 Sukatani")

menu = ["🏠 Beranda", "💬 Teman Cerita (Anonim)", "📚 Sudut Tenang", "🆘 Pusat Bantuan", "🎮 Pohon Simphony"]
choice = st.sidebar.selectbox("Pilih Menu", menu)

st.title("🌱 SIMPHONY")
st.subheader("Students Interacting and Motivating Each Other through Positive Harmonious Opportunities for Networking and Youth")

# --- LOGIKA HALAMAN ---

# 1. HALAMAN BERANDA
if choice == "🏠 Beranda":
    st.write("### Selamat Datang di Ruang Amanmu!")
    st.image("https://images.unsplash.com/photo-1516062423079-7ca13cdc7f5a?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80")
    st.info("Aplikasi ini dirancang untuk membantumu berinteraksi tanpa rasa takut akan diskriminasi atau bullying[cite: 111, 114].")

# 2. HALAMAN FORUM ANONIM
elif choice == "💬 Teman Cerita (Anonim)":
    st.write("### 📢 Ceritakan Keluh Kesahmu")
    st.write("Identitasmu tetap rahasia. Jangan ragu untuk berbagi pengalamanmu.")
    
    kategori = st.selectbox("Kategori Masalah", ["Keluarga", "Circle Pertemanan", "Bullying", "Faktor Internal"])
    pesan = st.text_area("Apa yang sedang kamu rasakan?", placeholder="Tuliskan di sini...")
    
    if st.button("Kirim Cerita"):
        if pesan:
            st.success("Cerita berhasil dikirim secara anonim. Tetap kuat ya!")
        else:
            st.warning("Tuliskan ceritamu terlebih dahulu.")

# 3. HALAMAN EDUKASI
elif choice == "📚 Sudut Tenang":
    st.write("### 📖 Artikel Motivasi & Tips")
    st.write("Edukasi untuk membantumu membangun hubungan sosial yang lebih baik.")
    st.markdown("- [Membangun Kepercayaan Diri](https://www-helpguide-org.translate.goog/mental-health/wellbeing/how-to-build-confidence?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc&_x_tr_hist=true)")
    st.markdown("- [Cara Berkomunikasi dengan Orang Tua'](https://rri.co.id/entikong/berita-lain/798309/tips-berkomunikasi-dengan-orangtua)")
    st.write("### 📖 Video Motivasi")
    st.video("https://youtu.be/BI2_FVJOO1M?si=5j7lHJOL99HaxrpX")

# 4. HALAMAN BANTUAN
elif choice == "🆘 Pusat Bantuan":
    st.write("### 📞 Kontak Konselor Profesional")
    st.write("Jika kamu butuh penanganan lebih lanjut, hubungi guru BK atau konselor kami:")
    st.table({
        "Nama": ["Ibu Riastuty Nuswo Utami, S.Pd., M.Pd.", "Konselor Pendamping"],
        "Spesialisasi": ["Masalah Keluarga & Bullying", "Pengembangan Diri"],
        "WA": ["0812xxxx", "0813xxxx"]
    })

# 5. HALAMAN GAMIFIKASI
elif choice == "🎮 Pohon Simphony":
    st.write("### 🎮 Pohon Simphony")
    st.write("Rawat pohonmu dengan terus berpikiran positif dan berani berinteraksi!")
    st.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=150)
    st.progress(60, text="Progres Pertumbuhan: Level 3")
