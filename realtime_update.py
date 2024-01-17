import requests, sys 


KEY = ""


def create_talk(stream_id, session_id, dialogue):

    url = f"https://api.d-id.com/talks/streams/{stream_id}"

    payload = {
        # "source_url": image_url,
        # "face": {"size":512},
        "script": {
            "input": dialogue,
            "type": "text",
            "subtitles": "false",
            "provider": {
                "type": "microsoft",
                "voice_id": "en-US-JennyNeural"
            },
            "ssml": "false"
        },
        "config": {
            "fluent": "false",
            "pad_audio": "0.0"
        }, 
        "session_id": session_id
    }
    headers = {
        "Content-Type": "application/json",
        # "Accept": "application/json",
        "Authorization": f"Basic {KEY}"
    }

    response = requests.post(url, headers=headers, json=payload)

    print(response.text)
    return response.json()



if __name__ == "__main__":
    # Capture command-line arguments
    args = sys.argv[1:]  # Exclude the script name
    stream_id = args[0]
    session_id = args[1]
    dialogue = args[2]

    # Call the create_talk method with the captured arguments
    create_talk(stream_id,session_id, dialogue)