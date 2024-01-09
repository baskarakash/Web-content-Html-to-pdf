from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
import requests
import pdfkit

app = FastAPI()

# Specify the path to wkhtmltopdf executable
config = pdfkit.configuration(wkhtmltopdf=r'C:\Users\AkashBaskar\Desktop\html2pdf\wkhtmltox\bin\wkhtmltopdf.exe')

@app.get("/")
async def main():
    html_content = """
    <html>
        <body>
            <form method="post" action="/generate_pdf">
                <label for="url">Enter URL:</label>
                <input type="text" name="url" id="url" required>
                <button type="submit">Generate PDF</button>
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/generate_pdf")
async def generate_pdf(url: str = Form(...)):
    try:
        # Fetch HTML content from the URL
        response = requests.get(url)
        response.raise_for_status()

        # Convert HTML to PDF using specified wkhtmltopdf executable
        pdf_content = pdfkit.from_url(url, False, configuration=config)

        # Save the PDF to a file
        pdf_filename = "output.pdf"
        with open(pdf_filename, "wb") as pdf_file:
            pdf_file.write(pdf_content)

        return {"message": "PDF generated successfully", "pdf_filename": pdf_filename}

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch URL: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))