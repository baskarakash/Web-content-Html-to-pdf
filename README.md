# **FastAPI PDF Generator**

## **Project Overview**

The FastAPI PDF Generator is a web application that allows users to convert HTML content into a PDF file. Built with FastAPI and Jinja2, this application provides a user-friendly interface to input HTML content and generate a downloadable PDF file. It uses the `pdfkit` library to perform the conversion, leveraging the `wkhtmltopdf` executable for accurate rendering.

## **Features**

- **HTML to PDF Conversion**: Convert user-provided HTML content into a PDF file.
- **User Interface**: Simple and intuitive web form for inputting HTML content.
- **File Saving**: Generate and save the PDF file on the server.

## **Technologies Used**

- **FastAPI**: For creating the web application and API endpoints.
- **Jinja2**: For rendering HTML templates.
- **pdfkit**: For converting HTML to PDF.
- **wkhtmltopdf**: Executable used by `pdfkit` for HTML to PDF conversion.

## **File Structure**

- `main.py`: The main FastAPI application script.
- `templates/main.html`: HTML template for the user interface.

## **Dependencies**

Ensure you have the following dependencies installed:

- `fastapi`
- `uvicorn`
- `pdfkit`
- `wkhtmltopdf` (downloadable executable)

You can install the Python dependencies using:

```bash
pip install fastapi uvicorn pdfkit
