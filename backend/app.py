# app.py
from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import spacy
from dataset import get_response
from flask_cors import CORS

print("Loading AI model... (Try'O Bot)")
nlp = spacy.load("en_core_web_sm")
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
print("Loaded successfully!")

app = Flask(__name__)
CORS(app)

chat_history_ids = None

def preprocess(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_punct and not token.is_space])

def get_ai_response(user_input, history_ids=None):
    inputs = tokenizer(user_input + tokenizer.eos_token, return_tensors="pt")
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    if history_ids is not None:
        input_ids = torch.cat([history_ids, input_ids], dim=-1)
        attention_mask = torch.cat([torch.ones_like(history_ids), attention_mask], dim=-1)

    output_ids = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_new_tokens=100,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95
    )

    response = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response, output_ids

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history_ids
    data = request.json
    user_input = data.get("message", "").strip()
    if not user_input:
        return jsonify({"response": "Please say something!"})

    rule_response = get_response(preprocess(user_input))
    if rule_response != "Sorry, I can't understand.":
        return jsonify({"response": rule_response})

    ai_response, chat_history_ids = get_ai_response(user_input, chat_history_ids)
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)
