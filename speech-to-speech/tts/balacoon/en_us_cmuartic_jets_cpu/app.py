from fastapi import FastAPI , Request
from fastapi.responses import FileResponse , StreamingResponse
import uvicorn 
import wave
from scripts.services.services import forward , forward_stream
from balacoon_tts import TTS

app = FastAPI()

tts = TTS('assets/models/en_us_cmuartic_jets_cpu.addon')

@app.get('/')
def read_root() : return {'Message' : ''}

@app.get('/synthesize')
def sysnthesize(request : Request) : 

    text = request.query_params.get('text')
    ret_type = request.query_params.get('ret_type')
    speaker = request.query_params.get('speaker')
    file_name = request.query_params.get('file_name' , None)

    if not text : return {'Message' : 'text is required'}
    if not ret_type : return {'Message' : 'ret_type is required'}
    if not speaker : return {'Message' : 'speaker is required'}

    yield {
        'Message' : f'''
        Synthesizing the text: {text}
        Speaker: {speaker}
        Return Type: {ret_type}
        File Name: {file_name}
        Type : synthesize
        '''
    }

    audio = forward(tts , speaker , text , ret_type , file_name)

    if ret_type == 'file' : return FileResponse(
        path = audio , 
        media_type = 'audio/wav'
    )
    elif ret_type == 'base64' : return {'Audio Base 64' : audio}
    elif ret_type == 'numpy' : return {'Audio Numpy' : audio}
    elif ret_type == 'bytes' : return {'Audio Bytes' : audio}

@app.get('/synthesize_stream')
def synthesize_stream(request : Request) : 

    text = request.query_params.get('text')
    ret_type = request.query_params.get('ret_type')
    speaker = request.query_params.get('speaker')

    if not text : return {'Message' : 'text is required'}
    if not ret_type : return {'Message' : 'ret_type is required'}
    if not speaker : return {'Message' : 'speaker is required'}

    yield {
        'Message' : f'''
        Synthesizing the text: {text}
        Speaker: {speaker}
        Return Type: {ret_type}
        Type : synthesize_stream
        '''
    }

    audio = forward_stream(tts , speaker , text , ret_type)

    return StreamingResponse(audio)

if __name__ == '__main__' : 

    uvicorn.run(
    app , 
    host = '0.0.0.0' , 
    port = 8001
)