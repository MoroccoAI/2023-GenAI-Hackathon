from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_answer", methods=["POST"])
def get_answer():
    pdf_text = request.form.get("pdf_text")
    question = request.form.get("question")

    # Use GPT-3 to generate an answer
    prompt = f"Question: {question}\nContext: {pdf_text}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=200
    )
    generated_answer = response.choices[0].text.strip()

    return jsonify({"answer": generated_answer})

if __name__ == "__main__":
    app.run(debug=True)
