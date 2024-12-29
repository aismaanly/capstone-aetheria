import streamlit as st

# Create three columns
col1, col2, col3 = st.columns([1, 3, 1])

# Displaying images in the center column
with col2:
    st.image("assets/cover_aetheria.png")

st.markdown("### 👾 Selamat Datang di Aetheria!")

st.markdown("""
Aetheria adalah asisten konsultasi karir yang dirancang untuk membantu Anda dalam merencanakan karir dan mencapai tujuan profesional. 
Aplikasi ini menawarkan berbagai fitur untuk mempermudah pencarian kerja, termasuk pembuatan resume yang sesuai dengan standar ATS, 
latihan wawancara, rekomendasi pekerjaan, dan tips networking.
""")

with st.expander("**✨ Fitur Menarik Aplikasi Aetheria**", expanded=True):
    features = [
        "🎨 UI yang menarik dan mudah digunakan, membuat Anda merasa nyaman saat menggunakan aplikasi",
        "📁 Mampu mengunggah file dan memberikan penjelasan yang mudah dimengerti",
        "💬 Bisa mengakses percakapan sebelumnya, jadi Anda tidak perlu khawatir kehilangan informasi",
        "🤖 Bisa mengatur kepribadian chatbot dan melihat riwayat percakapan untuk pengalaman yang lebih personal",
        "✂️ Dapat mengatur panjang jawaban chatbot sesuai dengan kebutuhan, seperti lebih singkat atau lebih detail",
        "🎭 Tingkat kreativitas chatbot bisa disesuaikan, jadi jawabannya bisa lebih bervariasi",
        "🧑‍💻 Berbagai pilihan kepribadian chatbot yang bisa dipilih untuk membuat percakapan lebih menarik",
        "☁️ Aplikasi menggunakan teknologi AWS, jadi selalu siap digunakan tanpa gangguan, bahkan saat banyak orang menggunakan",
        "📄 Bisa membuat resume dalam format PDF setelah Anda selesai mengisi data, siap dibagikan atau dicetak",
    ]
    for feature in features:
        st.markdown(f"- {feature}")

with st.expander("**👾 Cara Menggunakan Fitur Chatbot**", expanded=True):
    st.markdown("""
    1. **Upload File**: Bisa mengunggah file seperti dokumen PDF atau Word untuk dianalisis. Chatbot akan memberikan penjelasan yang mudah dipahami berdasarkan isi file tersebut.
    2. **Riwayat Percakapan**: Bisa mengakses percakapan sebelumnya yang telah disimpan. Ini memungkinkan Anda untuk melanjutkan diskusi tanpa kehilangan informasi penting.
    3. **Pilihan Kepribadian Chatbot**: Ada berbagai pilihan kepribadian yang bisa Anda pilih untuk meningkatkan interaksi dan membuat percakapan lebih menarik.
    4. **Pengaturan Jawaban**: Anda bisa mengatur panjang jawaban yang diberikan oleh chatbot, apakah ingin lebih singkat atau lebih detail, sesuai dengan kebutuhan Anda.
    5. **Kreativitas Jawaban**: Pengaturan tingkat kreativitas chatbot bisa disesuaikan. Anda bisa memilih apakah Anda ingin jawaban yang lebih formal atau lebih kreatif.
    """)

with st.expander("**📝 Cara Menggunakan Fitur Pembuatan CV**", expanded=True):
    st.markdown("""
    1. **Informasi Pribadi**: Masukkan data pribadi Anda seperti nama, informasi kontak, dan deskripsi singkat.
    2. **Pendidikan**: Tambahkan latar belakang pendidikan Anda. Anda bisa menambahkan beberapa inputan.
    3. **Profesional**: Masukkan pengalaman kerja Anda. Gunakan bullet points untuk format yang lebih rapi.
    4. **Skills**: Daftar skills, bahasa, dan sertifikasi Anda.
    5. **Generate PDF**: Review informasi Anda dan buat resume dalam format PDF.

    **Tips**: Saat memasukkan pengalaman Anda, gunakan '- ' (strip diikuti spasi) di awal setiap poin baru untuk membuat bullet points di resume PDF Anda.

    Contoh:
    ```
    - Mengembangkan fitur produk baru yang meningkatkan keterlibatan pengguna sebesar 25%
    - Memimpin tim beranggotakan 5 pengembang dalam lingkungan Agile
    - Mengimplementasikan pipeline CI/CD, mengurangi waktu deployment sebesar 40%
    ```
    """)


