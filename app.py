import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Modern LangChain imports
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API Key not found! Please check your .env file and ensure it contains GOOGLE_API_KEY=your_key")
    st.stop()

# 1. Initialize API and Model
# Using gemini-2.5-flash as it is the current standard for 2026
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    google_api_key=api_key, 
    temperature=0.7
)

# 2. Define Prompt Template
nutritional_info_template = PromptTemplate(
    input_variables=["food_items"],
    template="""Analyze the following food items and provide a detailed nutritional breakdown: {food_items}. 
    Please include:
    - Calories per item
    - Macronutrients (Protein, Fats, Carbs)
    - Key Micronutrients
    - A summary of total calories for the entire list."""
)

# 3. Streamlit UI Logic
def main():
    st.set_page_config(page_title="NutriAI 2026", page_icon="🍎")
    st.title("🍎 NutriAI - Professional Nutritionist")
    st.write("Enter your meals below to get an instant AI-powered health report.")

    with st.form("nutrition_form"):
        food_items = st.text_area("What did you eat today?", placeholder="e.g., 2 boiled eggs, 100g oats, 1 medium apple")
        submitted = st.form_submit_button("Analyze My Meal")

        if submitted:
            if not food_items.strip():
                st.warning("Please enter some food items first!")
            else:
                with st.spinner("Calculating nutrients..."):
                    try:
                        # Generate Response
                        prompt = nutritional_info_template.format(food_items=food_items)
                        response = llm.invoke(prompt)
                        
                        st.divider()
                        st.subheader("Nutritional Report")
                        st.markdown(response.content)
                    except Exception as e:
                        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()