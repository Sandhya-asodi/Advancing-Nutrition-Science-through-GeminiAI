🍎 NutriAI – Advancing Nutrition Science through GeminiAI


NutriAI is an AI-powered web application that provides detailed nutritional analysis of food items using Google Generative AI (Gemini). It helps users understand their diet by delivering insights on calories, macronutrients, micronutrients, and overall health impact.

Built with Streamlit + LangChain + Gemini AI, this tool enables smarter and more informed dietary decisions.

🚀 Features


🥗 Instant Nutritional Analysis

Calories per food item

Macronutrients (Protein, Fats, Carbohydrates)

Micronutrients (Vitamins & Minerals)


📊 Total Meal Summary


Overall calorie count

Combined nutrition insights


🤖 AI-Powered Insights


Uses Gemini 2.5 Flash model for accurate and fast responses

💡 User-Friendly Interface

Simple input via Streamlit UI

Real-time analysis

🧠 Use Case Scenarios

1. Tailored Meal Planning

Users can plan meals based on:

Dietary restrictions

Health goals

Preferences

The AI generates balanced meal suggestions and guidance.

2. Dynamic Nutritional Insights

Input meals or snacks

Get instant breakdown of nutrients

Helps track daily intake and improve food choices

3. Virtual Nutrition Coaching

Acts as a personal nutrition assistant

Provides:

Health suggestions

Diet improvements

Lifestyle guidance

🛠️ Tech Stack

Frontend: Streamlit

Backend: Python

AI Framework: LangChain

LLM: Google Gemini (via Generative AI API)

Environment Management: python-dotenv

📦 Installation




Install dependencies:

pip install -r requirements.txt

Create a .env file and add your API key:

GOOGLE_API_KEY=your_api_key_here

▶️ Running the App

streamlit run app.py
🧪 Example Input
2 boiled eggs, 100g oats, 1 apple
Output:

Calories per item

Protein, fats, carbs

Key vitamins & minerals

Total calorie summary

⚠️ Error Handling

Displays error if API key is missing

Handles invalid input gracefully

Shows runtime errors in UI

🔮 Future Enhancements

📷 Food image recognition

📊 Nutrition tracking dashboard

🛒 Grocery list generation

🧾 Weekly diet planner

📱 Mobile-friendly UI

🔗 Integration with fitness apps
