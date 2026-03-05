import streamlit as st
import random
from datetime import date

# Sayfa Konfigürasyonu
st.set_page_config(page_title="Şeyda'ya Özel ❤️", page_icon="🌹", layout="centered")

# CSS ile biraz özelleştirme (Arka plan ve yazı tipleri)
st.markdown("""
    <style>
    .main {
        background-color: #fff5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4b4b;
        color: white;
    }
    h1 {
        color: #d32f2f;
        text-align: center;
    }
    </style>
    """, unsafe_allow_status_html=True)

st.title("Günün Sürpriz Notu ✨")

# Not Listesi (Burayı dilediğin kadar doldurabilirsin)
notlar = [
    "Bugün harika görünüyorsun (görmeme gerek bile yok)! ❤️",
    "Seninle tanıştığımız o günü düşünmek bile beni gülümsetiyor.",
    "Dünyanın en şanslı insanıyım çünkü yanımda sen varsın. 🌟",
    "Bugün kendine bir kahve ısmarla, benden sana küçük bir mola olsun.",
    "Senin zekan ve kalbin benim için en büyük ilham kaynağı. 🥰",
    "Hangi dert olursa olsun, beraber olduğumuz sürece her şeyi çözeriz.",
    "Gülüşün, tüm günümü aydınlatmaya yetiyor. 🌹"
]

# Her gün sadece 1 farklı not çıkması için bugünün tarihini seed olarak kullanıyoruz
random.seed(date.today().toordinal())
gunun_notu = random.choice(notlar)

# Ekran Tasarımı
st.write("---")
st.subheader("Merhaba Şeyda! Bugün senin için bir mesajım var:")

st.info(gunun_notu)

# İnteraktif bir buton (Havai fişek/balon efekti)
if st.button("Bana bir sürpriz daha yap!"):
    st.balloons()
    st.success("Seni çok seviyorum! ❤️")

# Opsiyonel: Fotoğraf veya Şarkı Linki
st.write("---")
st.write("🎵 **Günün Modu:** [Seninle En Sevdiğimiz Şarkı](https://open.spotify.com/...)") # Linki değiştir

# İleride beraber çekildiğiniz bir fotoğrafı eklemek istersen:
# st.image("biz.jpg", caption="Unutulmaz bir anımız.")
