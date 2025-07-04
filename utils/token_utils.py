import tiktoken

def count_tokens(text, model="mistralai/mistral-small-3.2-24b-instruct:free"):  # works with OpenRouter models too
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def trim_text_to_token_limit(text, max_tokens=80000, model="mistralai/mistral-small-3.2-24b-instruct:free"):
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return encoding.decode(tokens[:max_tokens])
