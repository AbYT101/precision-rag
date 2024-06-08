# Precision-RAG
Precision RAG: Prompt Tuning For Building Enterprise Grade RAG Systems

## Overview
The Prompt Generation System is an automated tool designed to assist users in generating multiple prompt options based on their input descriptions of tasks, objectives, and scenarios. The system employs sophisticated algorithms and evaluation metrics to ensure that the generated prompts align with the user's requirements.

### Features
- Input Processing: Accepts user input, including task descriptions, scenarios, and expected outputs.
- Prompt Generation Engine: Utilizes advanced NLP techniques and generative models to create diverse and contextually relevant prompt options.
- Evaluation Module: Evaluates generated prompts based on predefined metrics such as semantic similarity, coherence, and relevance.
- Integration of Prompt Knowledge Base: Incorporates a collection of prompts from the Fabric framework to enrich the prompt generation process.
- Semantic Routes: Fetches semantically similar prompts from the knowledge base to enhance the variety and relevance of generated prompts.

## Project Structure
```
precision-rag/
├── data/
│ ├── knowledge.txt
│ └── load_data.py
├── evaluation/
│ ├── automatic_evaluation.py
│ ├── evaluate.py
│ └── test_generator.py
├── rag/
│ ├── augmentation.py
│ ├── generate.py
│ ├── parse_prompts.py
│ ├── rag.py
│ ├── retrieve.py
│ └── ui.py
├── .gitignore
├── LICENSE
└── README.md
```

### Installation

1. **Clone the repository:**

    ```sh
    git clone git@github.com:AbYT101/precision-rag.git
    cd precision-rag
    ```

2. **Set up a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. **Install Requirements:**
    ```sh
    pip install -r requirements.txt
    ```
4. **Run Streamlit interface**
    ```sh
   streamlit run rag/ui.py 
   ```

## Usage
- Provide input description of the task, including scenarios and expected outputs.
- Run the prompt generation system.
- Evaluate generated prompt options based on relevance and coherence.
- Select desired prompt options for further use.

![10 Academy](https://github.com/AbYT101/precision-rag/tree/main/screenshot/prompts.png)

## License

This project is licensed under the Apache-2.0 License.


## Contributors

- [@abyt101](https://github.com/AbYT101) - Abraham Teka

<br>

## Challenge by

![10 Academy](https://static.wixstatic.com/media/081e5b_5553803fdeec4cbb817ed4e85e1899b2~mv2.png/v1/fill/w_246,h_106,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/10%20Academy%20FA-02%20-%20transparent%20background%20-%20cropped.png)