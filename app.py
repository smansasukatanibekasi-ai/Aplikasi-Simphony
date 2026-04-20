import streamlit as st

# --- PENGATURAN HALAMAN ---
st.set_page_config(page_title="SIMPHONY - SMAN 1 Sukatani", page_icon="🌱")

# --- JUDUL & NAVIGASI ---
st.title("🌱 SIMPHONY")
st.subheader("Solusi Interaksi Siswa & Mental Health")

menu = ["🏠 Beranda", "💬 Teman Cerita (Anonim)", "📚 Sudut Tenang", "🆘 Pusat Bantuan"]
choice = st.sidebar.selectbox("Pilih Menu", menu)

# --- HALAMAN BERANDA ---
if choice == "🏠 Beranda":
    st.write("### Selamat Datang di Ruang Amanmu!")
    st.image("https://images.unsplash.com/photo-1516062423079-7ca13cdc7f5a?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80")
    st.info("Aplikasi ini dirancang untuk membantumu berinteraksi tanpa rasa takut akan diskriminasi atau bullying.")

# --- HALAMAN FORUM ANONIM ---
elif choice == "💬 Teman Cerita (Anonim)":
    st.write("### 📢 Ceritakan Keluh Kesahmu")
    st.write("Identitasmu tetap rahasia. Jangan ragu untuk berbagi.")
    
    kategori = st.selectbox("Kategori Masalah", ["Keluarga", "Circle Pertemanan", "Bullying", "Lainnya"])
    pesan = st.text_area("Apa yang sedang kamu rasakan?")
    
    if st.button("Kirim Cerita"):
        if pesan:
            st.success("Cerita berhasil dikirim secara anonim. Tetap kuat ya!")
        else:
            st.warning("Tuliskan ceritamu terlebih dahulu.")

# --- HALAMAN EDUKASI ---
elif choice == "📚 Sudut Tenang":
    st.write("### 📖 Artikel Motivasi & Tips")
    st.write("- **Tips Menghadapi Circle Exclusive**")
    st.write("- **Cara Berkomunikasi dengan Orang Tua**")
    st.write("- **Membangun Percaya Diri Setelah Bullying**")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Contoh link video

# --- HALAMAN BANTUAN ---
elif choice == "🆘 Pusat Bantuan":
    st.write("### 📞 Kontak Konselor Profesional")
    st.write("Jika kamu butuh penanganan lebih lanjut, hubungi guru BK atau konselor kami:")
    st.table({
        "Nama": ["Ibu Guru A", "Bapak Guru B"],
        "Spesialisasi": ["Masalah Keluarga", "Bullying & Trauma"],
        "WA": ["0812xxxx", "0813xxxx"]
    })
