# Ai Voice Assistant

An interactive voice assistant powered by OpenAI agents and a Flask-based API.

## Project Structure

- `agent.py`: Core logic for the AI agent and conversational flow.
- `api.py`: Flask API endpoints for interacting with the assistant.
- `prompts.py`: System prompts and agent instructions.
- `sample.env`: Template for environment variables (OpenAI API Keys, etc.).
- `requirements.txt`: Python dependencies.

## Key Features
- **Conversational Intelligence**: Uses OpenAI models to respond to user queries.
- **Voice-Ready**: Structured to handle input and output for voice-based interactions.
- **API Access**: Can be integrated into larger systems via the provided API.

## Getting Started

1.  **Configure Environment**: Rename `sample.env` to `.env` and add your API credentials.
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the API**:
    ```bash
    python api.py
    ```

## Usage
Interact with the assistant through the API endpoints defined in `api.py`.