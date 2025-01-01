import streamlit as st

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.image("assets/cover_aetheria.png")

st.markdown("### 👾 Selamat Datang di Aetheria!")

st.markdown("""
Aetheria adalah asisten konsultasi karir yang bertujuan untuk membantu Anda meningkatkan peluang keberhasilan dalam dunia kerja. 
Aplikasi ini menawarkan berbagai layanan, seperti pembuatan CV yang sesuai dengan Applicant Tracking System (ATS), latihan wawancara, rekomendasi pekerjaan berdasarkan keterampilan dan pengalaman, serta strategi networking. 
""")

with st.expander("**✨ Fitur Menarik Aplikasi Aetheria**", expanded=True):
    features = [
        "🎨 UI yang menarik dan mudah digunakan, membuat Anda merasa nyaman saat menggunakan aplikasi",
        "📁 Bisa mengunggah file dan memberikan penjelasan yang mudah dimengerti",
        "💬 Bisa mengakses percakapan sebelumnya, jadi Anda tidak perlu khawatir kehilangan informasi",
        "✂️ Bisa mengatur panjang jawaban chatbot sesuai dengan kebutuhan, seperti lebih singkat atau lebih detail",
        "🎭 Bisa menyesuaikan tingkat kreativitas chatbot, jadi respon chatbot lebih bervariasi",
        "💡 Bisa memilih berbagai pilihan kepribadian chatbot untuk membuat percakapan lebih menarik",
        "📄 Bisa membuat resume dalam format PDF setelah Anda selesai mengisi data, siap dibagikan atau dicetak",
        "☁️ Aplikasi menggunakan teknologi AWS, jadi selalu siap digunakan tanpa gangguan, bahkan saat banyak orang menggunakan",
    ]
    for feature in features:
        st.markdown(f"- {feature}")

with st.expander("**👾 Cara Menggunakan Fitur Chatbot**", expanded=True):
    st.markdown("""
    1. **Upload File**: Bisa mengunggah file seperti dokumen PDF atau Word untuk dianalisis. Chatbot akan memberikan penjelasan yang mudah dipahami berdasarkan isi file tersebut.
    2. **Riwayat Percakapan**: Bisa mengakses percakapan sebelumnya yang telah disimpan. Jadi, Anda bisa melanjutkan diskusi tanpa kehilangan informasi penting.
    3. **Pilihan Kepribadian Chatbot**: Ada berbagai pilihan kepribadian yang bisa Anda pilih untuk meningkatkan interaksi dan membuat percakapan lebih menarik.
    4. **Pengaturan Jawaban**: Bisa mengatur panjang jawaban yang diberikan oleh chatbot, apakah ingin lebih singkat atau lebih detail, sesuai dengan kebutuhan Anda.
    5. **Kreativitas Jawaban**: Pengaturan tingkat kreativitas chatbot bisa disesuaikan. Anda bisa memilih apakah Anda ingin jawaban yang lebih formal atau lebih kreatif.
    """)

with st.expander("**📝 Cara Menggunakan Fitur Pembuatan CV**", expanded=True):
    st.markdown("""
    1. **Informasi Pribadi**: Masukkan data pribadi Anda seperti nama, informasi kontak, dan deskripsi singkat.
    2. **Pendidikan**: Tambahkan latar belakang pendidikan Anda. Anda bisa menambahkan beberapa inputan.
    3. **Pengalaman Kerja**: Tambahkan pengalaman kerja Anda. Gunakan bullet points untuk format yang lebih rapi.
    4. **Informasi Tambahan**: Masukkan skills, bahasa, dan sertifikasi yang Anda miliki.
    5. **Generate PDF**: Review informasi Anda dan buat resume dalam format PDF.

    **Tips**: Saat memasukkan pengalaman Anda, gunakan '- ' (strip diikuti spasi) di awal setiap poin baru untuk membuat bullet points di resume PDF Anda.

    Contoh:
    ```
    - Memimpin tim beranggotakan 5 developer dalam lingkungan Amazon Web Service
    - Mengembangkan fitur produk baru yang meningkatkan keterlibatan pengguna sebesar 70%
    - Mengimplementasikan pipeline CI/CD, mengurangi waktu deployment sebesar 75%
    ```
    """)


