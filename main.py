from fastapi import FastAPI, UploadFile
import subprocess
import tempfile
import os
from fastapi.responses import FileResponse

app = FastAPI()

@app.post("/convert")
async def convert_to_pdf(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_docx:
        contents = await file.read()
        temp_docx.write(contents)
        temp_docx.flush()
        temp_docx.close()

        output_dir = tempfile.mkdtemp()
        subprocess.run([
            "libreoffice", "--headless", "--convert-to", "pdf",
            temp_docx.name, "--outdir", output_dir
        ])

        pdf_path = os.path.join(output_dir, os.path.basename(temp_docx.name).replace(".docx", ".pdf"))
        return FileResponse(pdf_path, media_type="application/pdf", filename="converted.pdf")
