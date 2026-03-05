import streamlit as st
import random
from datetime import date, datetime

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="Şeyda'ya Özel ❤️",
    page_icon="🌹",
    layout="centered"
)

# 2. Şık Tasarım İçin CSS (Hata düzeltildi)
st.markdown("""
    <style>
    .stApp {
        background-color: #fff5f5;
    }
    .main-title {
        color: #d32f2f;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0;
    }
    .sub-text {
        color: #5d4037;
        text-align: center;
        font-style: italic;
        margin-bottom: 2rem;
    }
    .note-box {
        background-color: white;
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #ff4b4b;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        font-size: 1.2rem;
        color: #333;
        text-align: center;
        margin: 2rem 0;
    }
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.6rem;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #d32f2f;
        color: white;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Başlık Alanı
st.markdown('<p class="main-title">Günün Sürprizi ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Sadece senin için, her gün yeni bir not...</p>', unsafe_allow_html=True)

# 4. Mesaj Listesi (Burayı istediğin kadar uzatabilirsin)
notlar = [
    "Bugün harika bir gün olacak, çünkü hayatımda sen varsın Şeyda! ❤️",
    "Gülüşün, tüm dertlerimi unutturan tek şey. 😊",
    "Seninle geçen her an, benim için en büyük hazine. 🌟",
    "Dünyanın en şanslı insanıyım çünkü seninle beraberim. 🥰",
    "Zekana, kalbine ve duruşuna her gün yeniden hayran kalıyorum. 🌹",
    "Bugün kendine çok iyi bak, çünkü benim için çok kıymetlisin. ✨",
    "İleride kuracağımız hayaller için bugün bir adım daha yakınız. 🏠",
    "Seninle kahve içmek bile dünyanın en huzurlu aktivitesi benim için. ☕",
    "Her sabah seninle uyandığım bir geleceğin hayaliyle gülümsüyorum."
]

# Her gün farklı ama sabit bir not çıkması için tarihi 'seed' olarak kullanıyoruz
random.seed(date.today().toordinal())
gunun_notu = random.choice(notlar)

# 5. Notu Göster
st.markdown(f'<div class="note-box">{gunun_notu}</div>', unsafe_allow_html=True)

# 6. İnteraktif Sürpriz Butonu
if st.button("Bana Bir Sürpriz Daha Yap!"):
    st.balloons()
    st.snow()
    st.success("Seni çok seviyorum Şeyda! ❤️")

# 7. Sayacı Ekle (Örn: Tanıştığınız Tarih)
# Buradaki tarihi kendi tanışma tarihinizle değiştirebilirsin
tanisma_tarihi = datetime(2024, 1, 1) # Yıl, Ay, Gün şeklinde yaz
bugun = datetime.now()
fark = bugun - tanisma_tarihi

st.write("---")
col1, col2, col3 = st.columns(3)
with col2:
    st.metric("Beraber Geçen Gün", f"{fark.days}")

st.caption("<center>Mehmet tarafından sevgiyle hazırlandı.</center>", unsafe_allow_html=True)
