from datasets import load_dataset
from transformers import AutoTokenizer, T5ForConditionalGeneration

CKPT = '/path/tp/transformer_model'

tokenizer = AutoTokenizer.from_pretrained(CKPT)
model = T5ForConditionalGeneration.from_pretrained(CKPT)

test_data = load_dataset('wikisql', split='test')

def translate_to_sql(text):
    inputs = tokenizer(text, padding='longest', max_length=64, return_tensors='pt')
    input_ids = inputs.input_ids
    attention_mask = inputs.attention_mask
    output = model.generate(input_ids, attention_mask=attention_mask, max_length=64)

    return tokenizer.decode(output[0], skip_special_tokens=True)

def text2SQL(natural_language_query):
    text =  "translate to SQL: " + natural_language_query
    sql_query = translate_to_sql(text)
    return sql_query