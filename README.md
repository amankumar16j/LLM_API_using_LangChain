# LangChain Demo With Gemini and LLAMA2

This project demonstrates the use of **LangChain**, **Google Generative AI (Gemini)**, and **LLAMA2** in building a server-side application with **FastAPI** and a client-side interface with **Streamlit**. The application allows users to generate essays and poems dynamically by leveraging powerful language models.

---

## Purpose
The primary goal of this project is to:
- Explore and understand the application of **LangChain** in real-world scenarios.
- Showcase the integration of **Google Generative AI (Gemini)** and **LLAMA2** with LangChain.
- Demonstrate how to build interactive client-server applications using **FastAPI** and **Streamlit**.

---

## Features
- **Essay Generator**: Generates a 100-word essay on a given topic using Gemini.
- **Poem Generator**: Creates a child-friendly poem on a given topic using Gemini.
- **User-Friendly Interface**: A Streamlit-based interface for easy interaction.
- **API Architecture**: FastAPI for modular, scalable, and efficient backend.

---

## Project Structure
### Server-Side Code (FastAPI)
- **FastAPI Application**: 
  - Hosts routes to handle essay and poem generation requests.
  - Routes `/essay` and `/poem` leverage LangChain with **Google Generative AI**.
- **LangChain Integration**: Uses `ChatGoogleGenerativeAI` for model interaction.
- **Prompt Templates**:
  - Essay prompt: "Write me an essay about {topic} with 100 words."
  - Poem prompt: "Write me a poem about {topic} for a 5-year-old child."

### Client-Side Code (Streamlit)
- **Streamlit Application**:
  - Collects user inputs for essay or poem topics.
  - Sends requests to the FastAPI server to invoke the LangChain prompts.
  - Displays the generated essay or poem.

---

## How to Run

### Prerequisites
- Python 3.8 or later
- Environment variables:
  - `LANGCHAIN_API_KEY`: API key for LangChain.
  - `GOOGLE_API_KEY`: API key for Google Generative AI.
- Installed dependencies from `requirements.txt`.

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file and add the necessary keys:
     ```
     LANGCHAIN_API_KEY=your_langchain_api_key
     GOOGLE_API_KEY=your_google_api_key
     ```
4. Run the server:
   ```bash
   python server.py
   ```
   - The FastAPI server will run on `http://localhost:8000`.

5. Run the client:
   ```bash
   streamlit run client.py
   ```
   - The Streamlit app will open in the browser.

---

## API Endpoints
1. **Essay Generation**:
   - Endpoint: `/essay/invoke`
   - Method: `POST`
   - Input: 
     ```json
     {
       "input": {
         "topic": "Your topic here"
       }
     }
     ```
   - Output:
     ```json
     {
       "output": {
         "content": "Generated essay content"
       }
     }
     ```

2. **Poem Generation**:
   - Endpoint: `/poem/invoke`
   - Method: `POST`
   - Input:
     ```json
     {
       "input": {
         "topic": "Your topic here"
       }
     }
     ```
   - Output:
     ```json
     {
       "output": {
         "content": "Generated poem content"
       }
     }
     ```

---

## Tech Stack
- **Backend**: FastAPI, LangChain, Google Generative AI
- **Frontend**: Streamlit
- **Other Tools**: Python, Uvicorn, dotenv

---

## Future Enhancements
- Add support for additional models like LLAMA2.
- Improve the UI for better user experience.
- Enable multi-language support for essays and poems.
- Enhance error handling and logging mechanisms.

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

---

## License
This project is open-source and available under the MIT License.

---

## Acknowledgements
- [LangChain Documentation](https://docs.langchain.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Generative AI API](https://cloud.google.com/generative-ai)
