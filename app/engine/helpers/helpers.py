import base64
from openai import OpenAI
from fastapi import UploadFile
from typing import Optional

async def check_image(file: Optional[UploadFile], user_message:str):
    await file.seek(0)
    file_bytes = await file.read()
    base64_image = base64.b64encode(file_bytes).decode('utf-8')
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe the image in as much detail as possible. Add the purpose of this picture."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=1500
    )

    response = {
        "original_query": user_message,
        "image_description": response.choices[0].message.content
    }
    
    return response
