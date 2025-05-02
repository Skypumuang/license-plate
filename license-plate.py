import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.title("🚗 AI อ่านป้ายทะเบียนด้วย EasyOCR")

uploaded_file = st.file_uploader("📸 อัปโหลดภาพ", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="ภาพต้นฉบับ", use_container_width=True)

    img_np = np.array(image)
    reader = easyocr.Reader(['en', 'th'])
    result = reader.readtext(img_np)

    text_all = "\n".join([res[1] for res in result])
    st.subheader("📋 ข้อความที่ตรวจพบ:")
    st.code(text_all.strip() if text_all else "ไม่พบข้อความ")

    if text_all.strip():
        st.download_button("📥 ดาวน์โหลดข้อความ", text_all.strip(), file_name="plate_text.txt")

