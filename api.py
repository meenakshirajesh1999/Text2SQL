import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

CKPT = 't5-small-finetuned-spider'

model = T5ForConditionalGeneration.from_pretrained(CKPT)
tokenizer = T5Tokenizer.from_pretrained(CKPT)

# Load the model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
model.eval()

def tokenize(text):
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt").to(device)
    with torch.no_grad():
        output = model.generate(**inputs, max_length=512)

    return tokenizer.decode(output[0], skip_special_tokens=True)

def text2SQL(schema, natural_language_query):
    natural_language_query =  "tables:\n " + schema.strip() + "\nquery for: " + natural_language_query.strip()
    sql_query = tokenize(natural_language_query)
    return sql_query