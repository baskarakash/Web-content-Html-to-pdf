from fastapi import FastAPI, HTTPException, Form,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pdfkit

app = FastAPI()

# Specify the path to wkhtmltopdf executable
config = pdfkit.configuration(wkhtmltopdf=r'C:\Users\AkashBaskar\Desktop\html2pdf\wkhtmltox\bin\wkhtmltopdf.exe')

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.post("/generate_pdf")
async def generate_pdf(html_content: str = Form(...)):
    try:
        # Convert HTML to PDF using specified wkhtmltopdf executable
        pdf_content = pdfkit.from_string(html_content, False, configuration=config)

        # Save the PDF to a file
        pdf_filename = "output.pdf"
        with open(pdf_filename, "wb") as pdf_file:
            pdf_file.write(pdf_content)

        return {"message": "PDF generated successfully", "pdf_filename": pdf_filename}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
