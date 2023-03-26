from fastapi import FastAPI, UploadFile, File
import io
import PyPDF2

# initiate object
app = FastAPI()


@app.post("/uploadFile/")
async def uploadFile(file: UploadFile = File(...)):

    # check if uploaded file is pdf
    if file.content_type != 'application/pdf':
        return {"error": "Only PDF files allowed"}

    # Extract text from PDF file
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(await file.read()))
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()

    return {"filename": file.filename,
            "text": text}
