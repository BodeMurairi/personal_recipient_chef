# 🍳 AI Personal Recipe Chef

An **Agentic AI cooking assistant** that generates recipes from **ingredients, text prompts, or food images**.
Built with **LangChain, LangGraph, Talvily, and Google Gemini**, the assistant can search the web for the best recipes and provide step-by-step cooking instructions.

This project demonstrates **modern agentic AI architecture**, including **tool use, memory, multimodal inputs, and LLM orchestration**.

---

# 🚀 Features

* 🤖 **AI Cooking Assistant** powered by Google Gemini
* 🔎 **Web Search Tool Integration** for up-to-date recipes
* 🧠 **Conversation Memory** using LangGraph
* 🖼 **Multimodal Input** (Text + Food Images)
* 📜 **Step-by-Step Recipe Instructions**
* 🧑‍🍳 Designed to behave like a **professional chef**
* 💻 **Command Line Interface**

---

# 🧠 How It Works

1. User provides:

   * Ingredients
   * Cooking question
   * Optional food image(s)

2. The agent:

   * Uses **Gemini LLM** to reason about the request
   * Calls the **web search tool** if needed
   * Uses **memory** to track conversation context
   * Analyzes **images and text together**

3. The assistant returns:

   * Recipe suggestions
   * Step-by-step cooking instructions
   * Helpful cooking tips

---

# 🏗 Project Architecture

```
personal_recipient_chef/
│
├── main.py
├── image_encoder.py
├── web_search.py
├── requirements.txt
├── .env
└── README.md
```

### File Descriptions

| File               | Purpose                                            |
| ------------------ | -------------------------------------------------- |
| `main.py`          | Main application entry point                       |
| `image_encoder.py` | Encodes images to Base64 for AI processing         |
| `web_search.py`    | Tool used by the AI agent to search recipes online |
| `requirements.txt` | Python dependencies                                |
| `.env`             | API keys and environment variables                 |

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/ai-personal-recipe-chef.git
cd ai-personal-recipe-chef
```

---

## 2️⃣ Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Set environment variables

Create a `.env` file:

```
GOOGLE_API_KEY=your_google_api_key_here
TAVILY_API_KEY=your_talvily_api_key_here
```

You can get a key from **Google AI Studio**.
You can get a tavily api key from **https://app.tavily.com/** create your account for free
---

# ▶️ Running the Application

Start the assistant:

```bash
python main.py
```

Example interaction:

```
Welcome to Sam Cooking Chef!

Enter your message: best recipe with chicken and rice
Enter image file paths: chicken.jpg
```

The AI will return:

* Suggested recipes
* Cooking steps
* Preparation instructions

---

# 🖼 Example Use Cases

### 1️⃣ Ingredient Based Cooking

```
User:
I have eggs, tomatoes and onions. What can I cook?
```

Output:

```
AI:
You can prepare a delicious tomato omelette...
```

---

### 2️⃣ Image Based Cooking

```
User:
What recipe can I cook with this ingredient?
Image: vegetables.jpg
```

Output:

```
AI analyzes image → suggests recipes.
```

---

### 3️⃣ Cooking Guidance

```
User:
How do I cook perfect fried rice?
```

Output:

```
Step-by-step instructions
```

---

# 🛠 Technologies Used

* **Python**
* **LangChain**
* **LangGraph**
* **Google Gemini (Gemini 2.5 Flash)**
* **Pillow (Image Processing)**
* **dotenv**
* **Agent Tooling**
* **Web search with Talvily**

---

# 🤖 Agent Capabilities

The AI agent can:

* Use tools (web search)
* Maintain conversation memory
* Analyze images
* Provide contextual responses
* Reason about cooking tasks

This demonstrates **modern AI agent design patterns** used in production AI systems.

---

# 📦 Dependencies

Example `requirements.txt`:

```
langchain
langchain-google-genai
langgraph
python-dotenv
pillow
requests
```

---

# 🧪 Future Improvements

Possible upgrades for this project:

* 🌐 Web interface (FastAPI or Streamlit)
* 🧾 Recipe saving system
* 🧠 Long-term memory database
* 🥗 Ingredient detection from images
* 📱 Mobile friendly UI
* 🎙 Voice cooking assistant

---

# 📸 Example Output

```
AI Recipe Suggestion:

Dish: Chicken Fried Rice

Ingredients:
- Chicken breast
- Cooked rice
- Soy sauce
- Garlic
- Eggs

Steps:
1. Heat oil in a pan
2. Cook garlic and chicken
3. Add eggs and scramble
4. Mix rice and soy sauce
5. Stir fry for 3 minutes
```

---

# 🎯 Learning Goals

This project demonstrates how to build:

* Agentic AI applications
* Multimodal AI workflows
* Tool-using LLM agents
* Memory enabled AI assistants

It is ideal for **AI engineering portfolios**.

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**Your Name**

Bode Murairi: Python developer| Backend Web developer|Machine Learning and AI Enthusiaste

GitHub: https://github.com/BodeMurairi
LinkedIn: https://www.linkedin.com/in/bode-murairi-2490501aa/ 

---

# ⭐ If You Like This Project

Please consider giving the repository a **star ⭐ on GitHub**.
