from openai import OpenAI

client = OpenAI(
    api_key='API_KEY'
)


def get_car_ai_bio(model, brand, year):
    message = '''
    SEU PROMPT {model} {brand} {year}
    '''
    message = message.format(model=model, brand=brand, year=year)
    
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )

    return response.choices[0].message.content