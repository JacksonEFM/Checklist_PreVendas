from fpdf import FPDF
from datetime import datetime
import streamlit as st
#def main(data, title, product_images, failure_images,validation_result, suggestions_data):
def main(data, title, product_images, failure_images, suggestions_data):
    class CustomPDF(FPDF):
        def header(self):
            self.image('img.png', x=10, y=8, w=30)  # Ajuste o caminho para sua imagem
            self.set_font("Arial", style="B", size=12)
            self.cell(0, 10, "Relatório de Validação", ln=True, align="C")
            self.ln(15)

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", size=8)
            self.cell(0, 10, f"Página {self.page_no()}", align="C")

    pdf = CustomPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Título
    pdf.set_font("Arial", style="B", size=16)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(0, 10, title, ln=True, align="C", fill=True)
    pdf.ln(10)

    # Data
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", ln=True, align="R")
    pdf.ln(10)

    # Adicionar fotos do produto no início
    if product_images:
        pdf.set_font("Arial", style="B", size=14)
        pdf.set_text_color(0, 0, 128)
        pdf.cell(0, 10, "Fotos do Produto:", ln=True)
        pdf.set_draw_color(0, 0, 128)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)

        for img in product_images:
            pdf.image(img, w=100)
            pdf.ln(10)

    # Adicionar dados coletados
    for section, items in data.items():
        pdf.set_font("Arial", style="B", size=14)
        pdf.set_text_color(0, 0, 128)
        pdf.multi_cell(0, 10, section)  # Título da seção
        pdf.set_draw_color(0, 0, 128)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)

        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0, 0, 0)

        for key, content in items.items():
            # Adicionar o status do item
            if content["status"]:
                status = "Sim"
                status_color = (0, 0, 0)  # Verde
            else:
                status = "Não"
                status_color = (255, 0, 0)  # Vermelho

            pdf.set_text_color(*status_color)
            pdf.multi_cell(0, 10, f"* {key}: {status}")

            # Comentários do item
            if content["comments"]:
                pdf.set_text_color(100, 100, 100)
                pdf.multi_cell(0, 10, f"  Observações: {content['comments']}")
                pdf.set_text_color(0, 0, 0)

            # Sugestões para itens não conformes
            if status == "Não Atendido":
                # Buscar sugestões associadas ao item não atendido
                item_suggestions = suggestions_data.get(key, [])
                #st.write(items)
                if item_suggestions:
                    pdf.set_font("Arial", style="I", size=12)
                    pdf.set_text_color(255, 140, 0)  # Laranja para sugestões
                    pdf.multi_cell(0, 10, "  Sugestões:")
                    for suggestion in item_suggestions:
                        pdf.multi_cell(0, 10, f"    - {suggestion}")
            pdf.ln(5)

    # Adicionar prints de falhas no final
    if failure_images:
        pdf.add_page()
        pdf.set_font("Arial", style="B", size=14)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, "Prints Comprovando Falhas:", ln=True)
        pdf.set_draw_color(255, 0, 0)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)

        for img in failure_images:
            pdf.image(img, w=100)
            pdf.ln(10)

    # Resultado de validação final
    pdf.set_font("Arial", style="B", size=14)
    pdf.set_text_color(0, 0, 128)
    #pdf.cell(0, 10, "Resultado de Validação:", ln=True)
    pdf.set_draw_color(0, 0, 128)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)
   # pdf.multi_cell(0, 10, validation_result)
    pdf.ln(5)

    # Salvar PDF
    filename = f"Relatorio PreVendas - Modelo: {title}.pdf"
    pdf.output(filename)
    return filename
