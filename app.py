import streamlit as st

# --- PENGATURAN HALAMAN ---
st.set_page_config(page_title="SIMPHONY - SMAN 1 Sukatani", page_icon="🌱", layout="centered")

# --- CUSTOM CSS UNTUK BACKGROUND & TAMPILAN ---
# Gambar background menggunakan tema alam yang menenangkan
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
        background-attachment: fixed;
        background-size: cover;
    }
    
    /* Membuat kotak konten agak transparan agar tulisan tetap jelas terbaca */
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    .stButton>button {
        width: 100%;
        height: 100px;
        font-size: 20px;
        border-radius: 15px;
        border: none;
        background-color: #ffffff;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #e1f5fe;
        transform: translateY(-3px);
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI NAVIGASI ---
if 'page' not in st.session_state:
    st.session_state.page = 'Beranda'

def kustom_navigasi(halaman):
    st.session_state.page = halaman

# --- LOGIKA HALAMAN ---

# 1. HALAMAN BERANDA (DASHBOARD UTAMA)
if st.session_state.page == 'Beranda':
    st.title("🌱 SIMPHONY")
    st.write("### Halo! Selamat datang di Ruang Amanmu.")
    st.write("Pilih layanan yang kamu butuhkan hari ini:")
    st.write("---")

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
    st.info("💡 **Tips:** Identitasmu di aplikasi ini anonim. Jangan ragu untuk berekspresi! [cite: 114]")

# 2. HALAMAN FORUM (Sesuai Tujuan: Wadah Berbagi Pengalaman)
elif st.session_state.page == 'Forum':
    if st.button("⬅️ Kembali"): kustom_navigasi('Beranda')
    st.header("💬 Teman Cerita (Anonim)")
    st.write("Bagikan ceritamu secara rahasia untuk melepaskan beban pikiran.")
    
    kategori = st.selectbox("Apa yang ingin kamu bahas?", ["Keluarga", "Circle Pertemanan", "Bullying", "Faktor Internal"])
    isi_cerita = st.text_area("Tuliskan perasaanmu...", placeholder="Ceritakan di sini tanpa rasa takut[cite: 4]...")
    
    if st.button("Kirim Cerita"):
        st.success("Ceritamu telah terkirim. Terima kasih sudah berani membuka diri! ")

# 3. HALAMAN EDUKASI
elif st.session_state.page == 'Edukasi':
    if st.button("⬅️ Kembali"): kustom_navigasi('Beranda')
    st.header("📚 Sudut Tenang")
    st.write("Informasi dan edukasi untuk membantumu bersosialisasi dengan lebih baik[cite: 103].")
    st.markdown("- **Membangun Percaya Diri**")
    st.markdown("- **Tips Menghadapi Lingkungan Baru**")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# 4. HALAMAN BANTUAN
elif st.session_state.page == 'Bantuan':
    if st.button("⬅️ Kembali"): kustom_navigasi('Beranda')
    st.header("🆘 Pusat Bantuan")
    st.write("Kamu tidak sendirian. Para ahli siap membantumu[cite: 113].")
    st.success("📞 Hubungi Guru BK SMAN 1 Sukatani")
    st.write("Jadwalkan sesi konsultasi untuk mendapatkan bimbingan pribadi[cite: 103].")

# 5. HALAMAN GAME (Pohon Simphony)
elif st.session_state.page == 'Game':
    if st.button("⬅️ Kembali"): kustom_navigasi('Beranda')
    st.header("🎮 Pohon Simphony")
    st.write("Setiap langkah kecilmu untuk berinteraksi membantu pohon ini tumbuh.")
    st.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=150)
    st.progress(60, text="Level Pertumbuhan: 3")
