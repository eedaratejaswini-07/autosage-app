# ============================================
# AutoSage - Image Based Vehicle Analysis
# (Structured As Per Standard Guide Procedure)
# ============================================

# ============================================
# 1️⃣ Initialization of Google API Key
# ============================================

from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Load environment variables
try:
    # Try Streamlit Cloud Secrets
    api_key = st.secrets["GOOGLE_API_KEY"]
except Exception:
    # Fallback to local .env
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)

# ============================================
# 2️⃣ Interfacing With Pre-Trained Model
# ============================================

def load_model():
    return genai.GenerativeModel("models/gemini-2.5-flash")


# ============================================
# 3️⃣ Write Prompt For Gemini Model (Image Based)
# ============================================

image_prompt = """
You are an automobile expert tasked with providing a detailed overview of any vehicles.

FORMATTING RULES:
- Follow the structure exactly as written below.
- Each section must be on a new line.
- Do NOT combine multiple fields in one sentence.
- Use bullet points properly (one point per line).
- If unsure, mention (Estimated).
- Keep the output crisp, practical, and structured.

The information should be presented in a structured format as follows:

Brand: Name of the vehicle brand.

Model: Specific model of the vehicle.

Launch Year: Since when the Vehicle is available in market.

Vehicle Type: (Scooter / Motorcycle / Sedan / SUV / Hatchback / Electric / Hybrid)

Fuel Type: (Petrol / Diesel / Electric / Hybrid)

Key Features:
- Engine Capacity:
- Transmission Type:
- Top 3 Special Features:

Mileage: Provide the average mileage in km/l (or km/charge for EVs).

Performance:
- Power Output (if known):
- Torque (if known):

Average Price in INR: Mention the price range of the vehicle model.

Maintenance Level: (Low / Moderate / High)

Safety Features:
- ABS / Airbags / Stability Control / etc. (if applicable)

Other Details:
- Maintenance cost (approx):
- Unique selling points:
- Target audience:

Approximate Resale Value: Estimate the resale value of the vehicle after 10 years in Indian Rupees.

End with a short 2-line summary of the vehicle's overall positioning in the Indian market.
"""


# ============================================
# 4️⃣ Implement Function To Read Image
# ============================================

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return {
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }
    else:
        raise FileNotFoundError("No file uploaded")


# ============================================
# 5️⃣ Implement Function To Get Gemini Response
# ============================================

def get_image_response(image_data):
    model = load_model()
    response = model.generate_content([image_prompt, image_data])
    return response.text


# ============================================
# 6️⃣ Model Deployment - Streamlit Integration
# ============================================

st.set_page_config(layout="wide", page_title="AutoSage", page_icon="🚗")

# Session State
if "mode" not in st.session_state:
    st.session_state.mode = "image"

if "messages" not in st.session_state:
    st.session_state.messages = []


# Header
col1, col2 = st.columns([9,1])

with col1:
    st.markdown("# 🚗 AutoSage")
    st.markdown("AI-Powered Vehicle Intelligence")

with col2:
    if st.button("🤖", help="Open AutoSage Assistant"):
        st.session_state.mode = "chat"
        st.rerun()


# ============================================
# PRIMARY FEATURE - IMAGE ANALYSIS
# ============================================

if st.session_state.mode == "image":

    st.markdown("## 📸 Upload Vehicle Image")

    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, width="stretch")

        if st.button("Analyze Vehicle", type="primary"):
            with st.spinner("Analyzing Vehicle..."):
                image_data = input_image_setup(uploaded_file)
                result = get_image_response(image_data)

            st.markdown("### 🚘 Vehicle Analysis")
            st.markdown(result)


# ============================================
# 7️⃣ ADDITIONAL FEATURE - TEXT BASED CHAT ASSISTANT
# ============================================

elif st.session_state.mode == "chat":

    st.markdown("## 🤖 AutoSage Assistant")

    if st.button("⬅ Back to Image Analysis"):
        st.session_state.mode = "image"
        st.rerun()

    st.markdown("---")

    st.info("""
**What AutoSage Assistant Can Do:**

• Recommend vehicles based on your budget  
• Compare two or more vehicles  
• Provide seasonal maintenance tips  
• Suggest eco-friendly (EV/Hybrid) options  
• Explain specifications in simple terms  

**Try asking queries like:**
- Best bikes under 2 lakhs  
- Compare Nexon and Brezza  
- Winter car maintenance tips  
- Best electric cars under 20 lakhs  
""")

    st.markdown("---")

    # Prompt for chat assistant (UNCHANGED)
    def build_prompt(user_query):
        return f"""
You are AutoSage, an expert AI automotive advisor focused on the Indian automobile market.

Your role:
Provide clear, structured, and practical vehicle insights to help users make informed decisions.

FORMATTING RULES:
- Keep responses crisp and easy to scan.
- Use bullet points where helpful.
- Do NOT write long paragraphs.
- Provide realistic price and mileage ranges.
- If uncertain, provide approximate values.
- Focus on decision-making insights.

User Query:
{user_query}

----------------------------------------
RESPONSE STRUCTURE (Use as applicable)
----------------------------------------

If the query is about Buying / Recommendation:

Recommended Models (2-4 options):
- Model Name - Price Range (INR)

For each model include:
- Mileage:
- Key Features (Top 3):
- Best For:

Short Verdict: Which option is better and why.

----------------------------------------

If the query is about Comparison:

Comparison Overview:
- Price Difference:
- Mileage Difference:
- Feature Highlights:
- Pros & Cons (each model)

Recommendation: Which one to choose and for what type of buyer.

----------------------------------------

If the query is about Maintenance:

Maintenance Advice:
- Key Checks:
- Seasonal Tips (if relevant):
- Estimated Service Cost Level:

----------------------------------------

If the query is about Eco-Friendly Vehicles:

Recommended EV/Hybrid Options:
- Model - Price - Range (km/charge)

Include:
- Charging Time:
- Running Cost Benefit:
- Government Incentives (India context if applicable)

End every response with a short 2-3 line practical summary.
"""

    def get_text_response(prompt):
        model = load_model()
        response = model.generate_content(prompt)
        return response.text

    # Display chat history
    for role, msg in st.session_state.messages:
        if role == "user":
            st.markdown(f"**🧑 You:** {msg}")
        else:
            st.markdown(f"**🚗 AutoSage:** {msg}")

    user_input = st.text_input("Type your message...")

    if st.button("Send"):
        if user_input:
            st.session_state.messages.append(("user", user_input))

            with st.spinner("Thinking..."):
                response = get_text_response(build_prompt(user_input))

            st.session_state.messages.append(("bot", response))
            st.rerun()


# ============================================
# Footer
# ============================================

st.markdown("---")
st.caption("AutoSage • Multimodal AI Vehicle Expert • Powered by Gemini 2.5 Flash")
