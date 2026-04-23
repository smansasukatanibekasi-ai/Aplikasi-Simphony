import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# --- KONEKSI DATABASE ---
conn = st.connection("gsheets", type=GSheetsConnection)

def simpan_ke_sheet(kategori, pesan):
    try:
        # Ambil data yang sudah ada
        existing_data = conn.read(ttl=0)
        
        # Buat data baru
        waktu = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        new_row = pd.DataFrame([{"Tanggal": waktu, "Kategori": kategori, "Curhatan": pesan}])
        
        # Gabungkan data lama dan baru
        updated_df = pd.concat([existing_data, new_row], ignore_index=True)
        
        # Update kembali ke Google Sheets
        conn.update(data=updated_df)
        return True
    except Exception as e:
        st.error(f"Gagal menyimpan: {e}")
        return False

# --- LOGIKA MENU TETAP SAMA ---
# (Gunakan menu Sidebar yang Anda inginkan sebelumnya)

# --- PENGATURAN HALAMAN & BACKGROUND ---
st.set_page_config(page_title="SIMPHONY - SMAN 1 Sukatani", page_icon="🌱")

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
        background-attachment: fixed;
        background-size: cover;
    }
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- KONEKSI DATABASE (VERSI BARU & GRATIS) ---
# Menghubungkan ke Google Sheets melalui fitur "Secrets" Streamlit
conn = st.connection("gsheets", type=GSheetsConnection)

def simpan_ke_sheet(kategori, pesan):
    try:
        # 1. Baca data yang sudah ada di Sheets
        # ttl=0 artinya kita selalu mengambil data terbaru
        existing_data = conn.read(ttl=0)
        
        # 2. Siapkan baris baru
        waktu = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        new_row = pd.DataFrame([{
            "Tanggal": waktu, 
            "Kategori": kategori, 
            "Curhatan": pesan
        }])
        
        # 3. Gabungkan data lama dengan data baru
        # Jika sheet kosong, kita pakai data baru saja
        if existing_data is not None and not existing_data.empty:
            updated_df = pd.concat([existing_data, new_row], ignore_index=True)
        else:
            updated_df = new_row
            
        # 4. Simpan kembali semuanya ke Google Sheets
        conn.update(data=updated_df)
        return True
    except Exception as e:
        st.error(f"Gagal menyimpan: {e}")
        return False

# --- NAVIGASI ---
menu = ["🏠 Beranda", "💬 Teman Cerita (Anonim)", "📚 Sudut Tenang", "🆘 Pusat Bantuan"]
choice = st.sidebar.selectbox("Pilih Menu", menu)

if choice == "🏠 Beranda":
    st.title("🌱 SIMPHONY")
    st.write("### Selamat Datang di Ruang Amanmu!")
    st.image("https://images.unsplash.com/photo-1516062423079-7ca13cdc7f5a?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80")
    st.info("Aplikasi ini membantu interaksi siswa SMAN 1 Sukatani agar lebih harmonis. Dibuat berdasarkan penelitian 'The Patterns of Interaction that Occur in the Learning Environment Case Study of SMA Negeri 1 Sukatani' oleh Anindya Kharisma Putri, Anggun Zulfa Qurrotul Aini, dan Denisa. This application is coded and developed by Irvan Daviana, S.Pd")

elif choice == "💬 Teman Cerita (Anonim)":
    st.write("### 📢 Ceritakan Keluh Kesahmu")
    st.write("Ceritamu akan tersimpan secara anonim untuk membantu kami memahamimu.")
    
    kategori = st.selectbox("Kategori Masalah", ["Keluarga", "Circle Pertemanan", "Bullying", "Faktor Internal"])
    pesan = st.text_area("Apa yang sedang kamu rasakan?")
    
    if st.button("Kirim Cerita"):
        if pesan:
            with st.spinner('Sedang mengirim secara anonim...'):
                berhasil = simpan_ke_sheet(kategori, pesan)
                if berhasil:
                    st.success("Cerita berhasil dikirim ke sistem SIMPHONY. Tetap kuat ya!")
        else:
            st.warning("Mohon tuliskan ceritamu terlebih dahulu.")

# 3. HALAMAN EDUKASI
elif choice == "📚 Sudut Tenang":
    st.write("### 📖 Artikel Motivasi & Tips")
    st.write("Edukasi untuk membantumu membangun hubungan sosial yang lebih baik.")
    st.write("- **Tips Menghadapi Circle Exclusive**")
    st.write("- **Cara Berkomunikasi dengan Orang Tua**")
    st.write("- **Membangun Percaya Diri Setelah Bullying**")
    st.video("https://youtu.be/BI2_FVJOO1M?si=8uHgSRxq2gnv2pDO")

# 4. HALAMAN BANTUAN
elif choice == "🆘 Pusat Bantuan":
    st.write("### 📞 Kontak Konselor Profesional")
    st.write("Jika kamu butuh penanganan lebih lanjut, hubungi guru BK atau konselor kami:")
    st.table({
        "Nama": ["Bapak Drs Ma'mun Nawawi,Bapak Faqih Maulidi, M.Pd., Ibu Riastuty Nuswo Utami, S.Pd., M.Pd", "Waka Kesiswaan, Staf Waka Kesiswaan, Konselor Pendamping"],
        "Spesialisasi": ["Masalah Keluarga & Bullying", "Pengembangan Diri"],
        "WA": ["0812xxxx",]
    })

# 5. HALAMAN GAMIFIKASI
elif choice == "🎮 Pohon Simphony":
    st.write("### 🎮 Pohon Simphony")
    st.write("Rawat pohonmu dengan terus berpikiran positif dan berani berinteraksi!")
    st.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=150)
    st.progress(60, text="Progres Pertumbuhan: Level 3")
