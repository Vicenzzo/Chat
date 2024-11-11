import openai

# Definir os parâmetros do Azure
openai.api_type = "azure"
openai.azure_endpoint = "https://vicen-m287c3uw-australiaeast.openai.azure.com/" 
openai.api_version = "2024-05-01-preview"
openai.api_key = "3fcf8054e63849d09678b1fafb032d6d"

deployment_name = "gpt-4-32k" 


chat_prompt = [
{
    "role": "system",
    "content": "Você é um assistente de IA que ajuda as pessoas a encontrar informações."
}
]  

# Incluir resultado de fala se a fala estiver habilitada  
speech_result = chat_prompt  

# Fazer a chamada à API
response = openai.chat.completions.create(
    model=deployment_name, 
    messages=speech_result,  
    max_tokens=10
)

print(response.to_json())  
    