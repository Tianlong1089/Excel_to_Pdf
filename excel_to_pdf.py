import pandas as pd
from fpdf import FPDF

ABSOLUTE_PATH= '/media/tianlong55/BLOCK II/Data'

for i in ([1,2,3]):
    globals() ['file%s'%i] = pd.read_excel(ABSOLUTE_PATH+f'/1000{i}-2023.1.18.xlsx', sheet_name='Sheet 1')
    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()
    pdf.set_font(family="TImes",size=16, style="B")
    pdf.cell(w=50, h=8, txt= f"Invoice nr. 1000{i}")
    pdf.output(f'/home/tianlong55/Downloads/PyCharm_Projects/Excel_to_Pdf/PDF/file_1000{i}.pdf')







''' Extra:
from pathlib import Path
filename = Path(filepath).stem
invoice_nr = filename.split("_")[0]

'''