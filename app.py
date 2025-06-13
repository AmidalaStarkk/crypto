# -----------------------------------------------------------------------------
# LIENZO COMPLETO PARA PRESENTACIÓN DE PROYECTO CON STREAMLIT Y N8N
# -----------------------------------------------------------------------------
# Autor: Tu Colega Programador de Streamlit ;)
# Fecha: 12 de Junio de 2025
#
# Funcionalidad Avanzada: Ejecución de n8n en segundo plano (threading)
# mientras se muestra una presentación visual en primer plano.
# -----------------------------------------------------------------------------

import streamlit as st
import requests
import time
import threading
import os

# --- 1. CONFIGURACIÓN GENERAL DE LA PÁGINA ---
st.set_page_config(
    page_title="Crypto Analyst",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. BARRA LATERAL DE NAVEGACIÓN (SIDEBAR) ---
with st.sidebar:
    st.title("🤖 Bitcoin Trading")
    st.write("---")
    st.header("Navigation Menu")

    option = st.radio(
        "Select a section to explore:",
        (
            "Project Home",
            "Problem Statement: Problem and Solution",
            "Fine tunning",
            "Model workflow",
            "Data/Inputs",
            "Outputs",
            "Predictions",
            "NATE",
            "Demo: Report Generator",
            "Results and Conclusions",
            "Join Our Community!"

        ),
        label_visibility="collapsed"
    )
    st.write("---")

# --- 3. FUNCIONES AUXILIARES Y DE PÁGINA ---

def home_page():
    """Cover section and team presentation."""
    st.markdown("<h1 style='text-align: center;'>🤖 Crypto Analyst</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Automated system for predictions, live trading, and market reports.</h3>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<h2 style='text-align: center;'>The Team Behind the Project</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        st.image("https://ca.slack-edge.com/T02NE0241-U08N4UW610C-ead40ca89833-512", caption="Pablo Lalia", use_container_width=True)
        st.markdown("<p style='text-align: center;'><strong>Role:</strong> AI and Language Models Expert</p>", unsafe_allow_html=True)

    with col2:
        st.image("https://ca.slack-edge.com/T02NE0241-U08N7UQEPT3-67872564de55-192", caption="Damien Hurley", use_container_width=True)
        st.markdown("<p style='text-align: center;'><strong>Role:</strong> Prediction Model Developer</p>", unsafe_allow_html=True)

    with col3:
        st.image("https://ca.slack-edge.com/T02NE0241-U08MWK0FF6F-61ade144e6f4-512", caption="Lidia Comendador Martínez", use_container_width=True)
        st.markdown("<p style='text-align: center;'><strong>Role:</strong> n8n and Automation Specialist</p>", unsafe_allow_html=True)


def problem_statement_page():
    """Section describing the problem and proposed solution."""
    st.markdown("<h1 style='text-align: center;'>🎯 The Problem: Volatility and Information Overload</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: justify;'>
    The cryptocurrency market is extremely volatile and generates a massive volume of data every day. Manually analyzing this information to make informed decisions is inefficient, time-consuming, and prone to biases.
    </div>
    """, unsafe_allow_html=True)
    st.write("---")
    st.markdown("<h2 style='text-align: center;'>💡 Our Solution:</h2>", unsafe_allow_html=True)
    st.markdown("""
    1. A specialized LLM for cryptocurrency trading.
    2. An advanced Bitcoin prediction model capable of analyzing market trends and executing trading actions for you.
    3. An automated workflow to orchestrate data collection and report dissemination based on the model's predictions.
    """)
    st.image("static/esquema.jpg", caption="Our n8n workflow diagram: The data orchestrator for the model and reports.", use_container_width=True)

def llm_finetuning_page():
    """Section showing fine tuning summary with a centered image."""
    st.markdown("<h1 style='text-align: center;'>🧠 Fine Tuning Summary</h1>", unsafe_allow_html=True)
    st.image("static/foto_fine_tuning.png", use_container_width=True)

def workflow():
    st.markdown("<h1 style='text-align: center;'>🔁 Slide 1: Time Series Workflow</h1>", unsafe_allow_html=True)

    st.markdown("""
    This workflow illustrates the complete time series forecasting pipeline:
    1. **Collect Data** – OHLCV + indicators
    2. **Engineer Features** – Momentum, Cross-corelations, Volatility etc.
    3. **Build Sequences** – Create (X, y) for supervised LSTM
    4. **Train Model** – LSTM Seq2Seq with custom loss
    5. **Forecast** – Reconstruct prices
    6. **Analyze** – Generate signals, visualizations, uncertainty
    """)
    st.image("static/workflow.png",
             caption="Time Series Forecasting Workflow Diagram",
             use_container_width=True)

def data_inputs():
    st.markdown("<h1 style='text-align: center;'>📥 Slide 2: Data Inputs</h1>", unsafe_allow_html=True)

    st.markdown("""
    The following elements are used to make forecasts:
    - **Price Data**: OHLCV from Binance (1w, 1d, 4h)
    - **Technical Indicators**: RSI, MACD, Bollinger Bands, OBV, etc.
    - **Calendar Features**: Weekday, Month, Halving Cycle
    - **Lagged Signals**: Rolling windows of previous observations
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.image("static/workflow1.png",
             caption="Visualization of Bitcoin price",
             use_container_width=True)
    with col2:
        # Add some vertical spacing to align with the other image
        st.markdown("<br>", unsafe_allow_html=True)
        st.image("static/workflow2.png",
             caption="Bitcoin historical dataset",
             use_container_width=True)

def outputs():
    st.markdown("<h1 style='text-align: center;'>📤 Slide 3: Outputs</h1>", unsafe_allow_html=True)

    st.markdown("""
    Once trained, the model produces:
    - **Price Predictions for 4h, 1d, 1w**
    - **Buy/Sell Signals**
    - **Uncertainty Bands**
    """)
    st.image("static/outputs3.png",
                 caption="Forecast vs Actual Prices",
                 use_container_width=True)
    st.image("static/output2.png",
             caption="Buy/Sell Signal Chart with Prediction Overlay",
             width=400)

def predictions():
    st.markdown("<h1 style='text-align: center;'>📈 Predictions Visualized</h1>", unsafe_allow_html=True)
    st.markdown("""
    This page illustrates how the predictions relative to recent market behaviour.
    """)
    st.image("static/prediction2.png", caption="Plotted Predictions", use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>📊 Forecast vs Reality</h2>", unsafe_allow_html=True)
    st.image("static/prediction1.png", caption="Numerical Predictions", width=400)

def nate():

    # Load the image
    # Replace 'NATE.png' with the actual path to your image file
    # if it's not in the same directory as your Streamlit script.
    st.markdown("<h1 style='text-align: center;'>🤖 NATE Workflow Visualization</h1>", unsafe_allow_html=True)
    st.image("static/NATE.png", use_container_width=True)


def call_n8n_workflow(url, result_holder):
    """
    Function executed in a separate thread.
    Calls the n8n webhook and saves the result in a shared dictionary.
    """
    try:
        # We add a long timeout because the process can take time.
        response = requests.post(url, json={}, timeout=300)
        response.raise_for_status() # Raises an error if the response is not 2xx
        result_holder['result'] = response.json()
    except requests.exceptions.RequestException as e:
        result_holder['error'] = str(e)

def demo_n8n_page():
    """Interactive section to execute the n8n workflow."""
    st.markdown("<h1 style='text-align: center;'>🔧 Interactive Demo: Report Generator</h1>", unsafe_allow_html=True)
    st.write(
        "Test our analysis engine. Clicking the button will execute our n8n workflow in real-time."
    )
    # Using two spaces and \n for an explicit line break in Markdown
    st.info(
            "The workflow will collect data, access the prediction model, process everything with AI, and generate a report.  \nPlease be patient, the complete process can take between 1 and 2 minutes.",
            icon="🤖"
        )

    if st.button("✨ Generate Bitcoin Report Now!", type="primary"):

        # Dictionary to share the result between threads.
        result_holder = {'result': None, 'error': None}

        # --- WEBHOOK URL ---
        # CAUTION! This is a TEST URL. For the app to work independently,
        # you need to activate your workflow in n8n and use the PRODUCTION URL.
        N8N_WEBHOOK_URL = "https://n8n.srv861951.hstgr.cloud/webhook/3e1ceeb8-2107-44e1-a1d2-1af1abc466c2"

        # 1. Start the n8n call in a separate thread
        thread = threading.Thread(
            target=call_n8n_workflow,
            args=(N8N_WEBHOOK_URL, result_holder)
        )
        thread.start()

        # 2. While the thread runs, show the visual presentation
        placeholder = st.empty()
        stages = [
            {
                "text": "Step 1: Collecting news from the last 24h...",
                "icon": "📰",
                "pic": os.path.join(os.getcwd(), 'static', 'brave1.png'),
                "duration": 30
            },
            {
                "text": "Step 2: Collecting tweets from relevant Bitcoin trading figures from the last 24h...",
                "icon": "🐤",
                "pic": os.path.join(os.getcwd(), 'static', 'X1.png'),
                "duration": 30
            },
            {
                "text": "Step 3: Merging both branches and filtering for relevant information...",
                "icon": "🖇️",
                "pic": os.path.join(os.getcwd(), 'static', 'filter1.png'),
                "duration": 20
            },
            {
                "text": "Step 4: The main AI brain generates the final report...",
                "icon": "🧠",
                "pic": os.path.join(os.getcwd(), 'static', 'main_brain.png'),
                "duration": 40
            }
        ]

        for stage in stages:
            with placeholder.container():
                st.info(stage["text"], icon=stage["icon"])
                st.image(stage["pic"], use_container_width=True) # Placeholder URL
                time.sleep(stage["duration"])

        # 3. Wait for the n8n thread to finish (if it hasn't already)
        with placeholder.container():
            st.info("Process almost complete... Waiting for the final Google Drive URL...", icon="✅")
            st.image("https://i.imgur.com/uG9t8k7.gif", use_container_width=True) # Keep the last GIF

        thread.join() # The main script waits here until the secondary thread finishes.

        # 4. Process and display the final result
        placeholder.empty()
        if result_holder['error']:
            st.error(f"Connection Error with n8n: {result_holder['error']}", icon="🚨")
        elif result_holder['result']:
            result_json = result_holder['result']
            st.success("Workflow completed! The report has been generated in Google Drive.", icon="🎉")

            if isinstance(result_json, dict) and 'webViewLink' in result_json:
                doc_url = result_json['webViewLink'] # Direct access to the key
                st.markdown(f"""
                <a href="{doc_url}" target="_blank" style="display: inline-block; padding: 14px 22px; background-color: #FF4B4B; color: white; text-align: center; text-decoration: none; font-size: 18px; border-radius: 8px; font-weight: bold;">
                    View Generated Document ↗️
                </a>
                """, unsafe_allow_html=True)
            else:
                st.warning("The workflow executed, but the response was not in the expected format.")
                st.write("Response received from n8n:")
                st.json(result_json)
        else:
             st.error("An unexpected error occurred during the process.")

def results_page():
    """Section to display metrics, results, and conclusions."""
    st.markdown("<h1 style='text-align: center;'>🤑 A TRADE HAS BEEN EXECUTED!</h1>", unsafe_allow_html=True)
    st.image("static/trade.png")


def telegram_page():
        """Page displaying Telegram QR code with a fun message."""
        st.markdown("<h1 style='text-align: center;'>🎁 Join Our Community!</h1>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("<h3 style='text-align: center;'>Scan for a SouRprise! 🍋</h3>", unsafe_allow_html=True)
            st.image("static/t_me-BitBitBitSahurBot.jpg", caption="Scan me if you dare!", use_container_width=True)
            st.markdown("<p style='text-align: center; font-style: italic;'>Our AI-powered Telegram bot is waiting for you!</p>", unsafe_allow_html=True)

# --- 4. MAIN LOGIC ---
if option == "Project Home":
    home_page()
elif option == "Problem Statement: Problem and Solution":
    problem_statement_page()
elif option == "Fine tunning":
    llm_finetuning_page()
elif option == "Model workflow":
    workflow()
elif option == "Data/Inputs":
    data_inputs()
elif option == "Outputs":
    outputs()
elif option == "Predictions":
    predictions()
elif option == "NATE":
    nate()
elif option == "Demo: Report Generator":
    demo_n8n_page()
elif option == "Results and Conclusions":
    results_page()
elif option == "Join Our Community!":
    telegram_page()
