import wave
import base64
from .....scripts.error.error import Error

def forward(model , speaker , text , ret_type , file_name = None , file_sampling_rate = None) : 

    try : 

        if not file_sampling_rate : file_sampling_rate = model.get_sampling_rate()

        audio = model.synthesize(text , speaker)

        if ret_type == 'file' : 

            with wave.open(file_name , 'w') as audio_file : 

                audio_file.setparams((1 , 2 , file_sampling_rate , len(audio) , 'NONE' , 'NONE'))
                audio_file.writeframes(audio)

            return file_name

        elif ret_type == 'base64' : return base64.b64encode(audio).decode('utf-8')
        elif ret_type == 'numpy' : return audio
        elif ret_type == 'bytes' : return audio.tobytes()

        else : return Error(
            f'''
            {ret_type} is not supported
            Please choose one of the following: (file , base64 , numpy , bytes)

            Or make a Issue/PR on the GitHub repository
            ''' , 
            dir = 'sts/tts/balacoon/scripts/services/services'
        )

    except Exception as e : return Error(e , dir = 'sts/tts/balacoon/scripts/services/services')

def forward_stream(model , speaker , text , ret_type , file_sampling_rate = None) : 

    if not file_sampling_rate : file_sampling_rate = model.get_sampling_rate()

    audio = model.synthesize(text , speaker)

    if ret_type == 'base64' : return base64.b64encode(audio).decode('utf-8')
    elif ret_type == 'numpy' : return audio
    elif ret_type == 'bytes' : return audio.tobytes()
