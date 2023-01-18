from fastapi import APIRouter, UploadFile, File, Form
from api_stable_diffusion.stable_diffusion_working import StableDiffusionWorking
from api_backend.api_key import apikey
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from convert_pdf.converter import PDF2MAIL

app_router = APIRouter()


@app_router.post('/upload')
async def upload(email: str = Form(...), file: UploadFile = File(...)):
    print(type(file))
    print(file)
    print(email)
    image = await file.read()
    sdw = StableDiffusionWorking(image=image, apikey=apikey)
    response = sdw.run_stable_diffusion()
    pdf2sendmail = PDF2MAIL(response=response, email=email)
    pdf2sendmail.pdf2mail()
    return JSONResponse(content=jsonable_encoder(response), media_type='application/json')


@app_router.get('/image')
async def image_base():
    return {"image": "yes"}
