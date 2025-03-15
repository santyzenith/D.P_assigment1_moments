import yaml
import os
import base64
from openai import OpenAI

def load_config():
    config_path = os.path.abspath("config.yaml")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def check_file_exists(image_path):
    if os.path.exists(image_path):
        if os.path.isfile(image_path):
            print(f"El archivo '{image_path}' es un archivo válido.")
            return True
        else:
            print(f"'{image_path}' es un directorio.")
            return False
    else:
        print(f"El archivo '{image_path}' no existe")
        return False
        
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        #return base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:image/jpeg;base64,{base64.b64encode(image_file.read()).decode('utf-8')}"
        
def get_llm_description(image_path):
    config = load_config()
    img_path = os.path.abspath("uploads/"+image_path)
    check_file_exists(img_path)
    
    image_base64 = image_to_base64(img_path)
    
    client = OpenAI(
        base_url=config["openai"]["base_url"],
        api_key=config["openai"]["api_key"],
    )

    completion = client.chat.completions.create(
        model=config["openai"]["model"],
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Briefly describe the image, answer in Spanish."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_base64
                        }
                    }
                ]
            }
        ]
    )
    
    return completion.choices[0].message.content

    