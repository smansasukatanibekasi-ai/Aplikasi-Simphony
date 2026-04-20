import streamlit as st

# --- PENGATURAN HALAMAN ---
st.set_page_config(page_title="SIMPHONY - SMAN 1 Sukatani", page_icon="🌱", layout="centered")

# --- CUSTOM CSS (Supaya Tampilan Lebih Enjoyable) ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        height: 100px;
        font-size: 20px;
        border-radius: 15px;
        border: none;
        background-color: #ffffff;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #e1f5fe;
        border: 1px solid #0288d1;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI NAVIGASI ---
if 'page' not in st.session_state:
    st.session_state.page = 'Beranda'

def kustom_navigasi(halaman):
    st.session_state.page = halaman

# --- LOGIKA HALAMAN ---

# 1. HALAMAN BERANDA (SEMUA MENU DI SINI)
if st.session_state.page == 'Beranda':
    st.title("🌱 SIMPHONY")
    st.write("### Halo! Selamat datang di Ruang Amanmu.")
    st.write("Pilih layanan yang kamu butuhkan hari ini:")
    st.write("---")

    # Membuat Grid 2 Kolom untuk Menu
    col1, col2 = st.columns(2)

    with col1:
        if st.button("💬\nTeman Cerita"):
            kustom_navigasi('Forum')
        
        if st.button("🆘\nPusat Bantuan"):
            kustom_navigasi('Bantuan')

    with col2:
        if st.button("📚\nSudut Tenang"):
            kustom_navigasi('Edukasi')
            
        if st.button("🎮\nPohon Simphony"):
            kustom_navigasi('Game')

    st.write("---")
    st.info("💡 **Tips:** Identitasmu di aplikasi ini anonim. Jangan ragu untuk berekspresi!")

# 2. HALAMAN FORUM
elif st.session_state.page == 'Forum':
    if st.button("⬅️ Kembali"): kustom_navigasi('Beranda')
    st.header("💬 Teman Cerita (Anonim)")
    kategori = st.selectbox("Masalah apa yang ingin kamu ceritakan?", ["Keluarga", "Circle Pertemanan", "Bullying", "Faktor Internal"])
    isi_cerita = st.text_area("Tuliskan di sini...", placeholder="Jangan takut, tidak ada yang tahu siapa kamu.")
    if st.button("Kirim Cerita"):
        st.success("Terima kasih sudah berani bercerita. Kamu luar biasa!")

# 3. HALAMAN EDUKASI
elif st.session_state.page == 'Edukasi':
    if st.button("⬅️ Kembali"): kustom_navigasi('Beranda')
    st.header("📚 Sudut Tenang")
    st.write("Temukan solusi atas masalahmu melalui artikel berikut:")
    st.markdown("- [Membangun Kepercayaan Diri](https://www.klikdokter.com/psikologi/kesehatan-mental/tips-mudah-bangun-rasa-percaya-diri-anda?srsltid=AfmBOooG09i8JhHe1ev6uiihxNUxVV1ritAcT_9KSA0dZOWrQx1eCPGE)")
    st.markdown("- [Menghadapi Teman yang 'Exclusive'](https://kidshealth-org.translate.goog/en/teens/cliques.html?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc)")
    st.video("https://youtu.be/BI2_FVJOO1M?si=2OoD_oJGpSpdUOdT")

# 4. HALAMAN BANTUAN
elif st.session_state.page == 'Bantuan':
    if st.button("⬅️ Kembali"): kustom_navigasi('Beranda')
    st.header("🆘 Pusat Bantuan")
    st.write("Butuh teman bicara langsung? Hubungi konselor kami:")
    st.success("📞 Ibu Guru BK - SMAN 1 Sukatani (0812-xxxx)")

# 5. HALAMAN GAME (GAMIFIKASI)
elif st.session_state.page == 'Game':
    if st.button("⬅️ Kembali"): kustom_navigasi('Beranda')
    st.header("🎮 Pohon Simphony")
    st.write("Rawat pohonmu dengan terus berinteraksi positif!")
    st.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=150)
    st.progress(40, text="Progres Pohonmu: Level 2")
