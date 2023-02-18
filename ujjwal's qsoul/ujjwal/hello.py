import openai
openai.api_key = "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"
prompt = input()
model = "text-davinci-003"
response = openai.Completion.create(
  engine=model,
  prompt=prompt,
  max_tokens=100
)
generated_text = response.choices[0].text
print(generated_text)
