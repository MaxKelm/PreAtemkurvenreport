from fpdf import FPDF

def export_pdf(data, path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="PDF Report Placeholder", ln=True, align='L')
    pdf.output(path)
    print(f"[pdf_report] Exported PDF to {path}")
