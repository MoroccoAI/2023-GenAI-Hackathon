# HyprSol AI-4-REC

HyprSol AI-4-REC model is used for the categorization task that the project requires to define the most important sections that need to be focused on by a given project. This model is a multilabel model using the bert architecture.

## Motivation

Knowing that the input of the user will be textual descriptions and informations, we felt that we need to make the model have a contextual understanding of those informations as such BERT came to mind, but just training the model to ouput what, the project need as final output the best fit technologies for the user's use case and we might want to directly train the model for doing just that, we thought it will be better to divide the work by having dedicated models. One for defining the categories that need to be focused for the specific use case in which case we would need a dataset that contains categorized projects. and the other ones will be a multiclass classifiers that are dedicated to choose te best fit technology in a particular category scope. This way we believe the whole process will be more accurate.

## Technologies

This project uses:
- **Python:** The main programming language.
- **NumPy:** For efficient data operations.
- **Pandas:** To clean and explore data.
- **PyTorch:** For building BERT models.
- **transformers:** A library with necessary tools.

## Folder Code Structure

```
ai/
├── data/
│   └── data.csv
├── trained_checkpoint/
│   ├── curr.ckpt
│   └── best_model.pt
├── model/
│   ├── creating_multilabel_model.py
│   └── model_notebook.ipynb
├── README.md
└── requirement.txt
```

## Run Locally

1. **Clone the project:**
```bash
git clone git@github.com:usmhic/hyprsolai.git
```

2. **Go to the project directory:**
```bash
cd hyprsolai/ai
```

3. **Create a Python virtual environment:**
```bash
python -m venv ./venv
```

4. **Activate the environment (Windows):**
```powershell
./venv/Scripts/Activate
```

   **Activate the environment (Linux):**
```bash
source ./venv/bin/activate
```

5. **Install requirements:**
```bash
pip install -r requirement.txt
```

6. **Create the multilabel classifier:**
```bash
python ai/model/creating_multilabel_model.py
```
```