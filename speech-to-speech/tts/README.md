
# Tree

||||
|---|---|---|
|TTS 
|----|Balacoon 
|----|----------|EN US CMUArtic JETS CPU|

# TTS 
```python
import requests

def send_tts_request(path , break_):

    url = 'http://localhost:8000/up-tts'

    headers = {'Content-Type' : 'application/json'}
    data = {
        'path': path,
        'break': break_duration
    }

    try : 

        response = requests.post(url , json = data , headers = headers)
        response.raise_for_status()

        return response

    except requests.exceptions.ConnectionError as e : print(f'Error: Could not connect to the server. {e}') ; return None
    except requests.exceptions.RequestException as e : print(f'Error: An error occurred during the request. {e}') ; return None
```


# TTS ---> Balacoon ---> EN US CMUArtic JETS CPU
```python

path = 'tts/balacoon/en_us-cmuartic_jets_cpu'
break_ = 'balacoon'

response = send_tts_request(path , break_)

if response.status_code == 200 : print('BALACOON EN US CMUARTIC JETS CPU UP!! ')
```

```bash
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{
        "path": "tts/balacoon/en_us-cmuartic_jets_cpu",
        "break": "balacoon"
    }' \
    http://localhost:8000/up-tts
```