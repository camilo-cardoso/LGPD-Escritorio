import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import fitz  
import io


st.markdown("""
<style>
    .card {
        background: #1e65d3;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        padding: 5px;
        height: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("Ferramentas de Escritório")

col1, col2, col3 = st.columns(3)


with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📚 Unificar PDFs")
    arquivos = st.file_uploader("Envie os PDFs", type=["pdf"], accept_multiple_files=True, key="unificar")

    if arquivos and st.button("Unificar PDF"):
        pdf_writer = PdfWriter()

        for arquivo in arquivos:
            reader = PdfReader(arquivo)
            for pagina in reader.pages:
                pdf_writer.add_page(pagina)

        buffer = io.BytesIO()
        pdf_writer.write(buffer)
        buffer.seek(0)

        st.download_button("📥 Baixar PDF Unificado", buffer, "unificado.pdf")
    st.markdown('</div>', unsafe_allow_html=True)



with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📝 Extrair Texto")
    arquivo_pdf = st.file_uploader("Envie o PDF", type=["pdf"], key="extrair")

    if arquivo_pdf and st.button("Extrair Texto"):
        reader = PdfReader(arquivo_pdf)
        texto = ""

        for pagina in reader.pages:
            texto += pagina.extract_text() + "\n"

        st.text_area("Texto Extraído:", texto, height=300)
    st.markdown('</div>', unsafe_allow_html=True)


with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📉 Diminuir PDF")
    pdf_compress = st.file_uploader("Envie o PDF", type=["pdf"], key="compress")

    if pdf_compress and st.button("Comprimir"):
        doc = fitz.open(stream=pdf_compress.read(), filetype="pdf")

        for pagina in doc:
            pagina.clean_contents()

        buffer = io.BytesIO()
        doc.save(buffer, garbage=4, deflate=True, ascii=False)
        buffer.seek(0)

        st.download_button("📥 Baixar PDF Comprimido", buffer, "comprimido.pdf")
    st.markdown('</div>', unsafe_allow_html=True)
