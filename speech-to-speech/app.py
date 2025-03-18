from fastapi import FastAPI , Request
import uvicorn
from scripts.services.services import run_start_sh_recursive

app = FastAPI()

@app.get('/')
def read_root() : return {'Message' : ''}

@app.post('/up-tts')
async def up_tts(request : Request) : 

    data = await request.json()

    path = data['path']
    break_ = data['break']

    run_start_sh_recursive(path , break_)

    return {'Message' : 'TTS started'}

if __name__ == '__main__' : uvicorn.run(
    app , 
    host = '0.0.0.0' , 
    port = 8000
)