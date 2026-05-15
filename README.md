# AI Voice Assistant

A real-time AI voice assistant for an auto service call center, built on LiveKit with a fully free AI stack.

## Stack

| Component | Service |
|---|---|
| Voice Infrastructure | LiveKit Cloud |
| Speech to Text | Groq Whisper (whisper-large-v3-turbo) |
| LLM | Groq Llama 3.3 70b |
| Text to Speech | ElevenLabs (eleven_turbo_v2_5) |
| Database | SQLite (local) |

## How It Works

When a caller connects to the LiveKit room, the agent:
1. Greets them and asks for their vehicle VIN
2. Looks up their profile in the database
3. Creates a new profile if they don't have one
4. Answers questions or directs them to the right department

## Project Structure

- `agent.py` — Entry point, wires together STT, LLM, TTS and connects to LiveKit
- `api.py` — VIN lookup, create vehicle, and update contact function tools backed by SQLite
- `prompts.py` — System instructions and welcome message for the agent
- `sample.env` — Template for required environment variables
- `requirements.txt` — Python dependencies

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/Pallavi-Pandey/ai-voice-assistant
   cd ai-voice-assistant
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment** — copy `sample.env` to `.env` and fill in your credentials:
   ```
   LIVEKIT_URL=wss://your-project.livekit.cloud
   LIVEKIT_API_KEY=your-livekit-api-key
   LIVEKIT_API_SECRET=your-livekit-api-secret
   GROQ_API_KEY=your-groq-api-key
   ELEVENLABS_API_KEY=your-elevenlabs-api-key
   ```

   | Credential | Where to get it |
   |---|---|
   | LiveKit | cloud.livekit.io |
   | Groq | console.groq.com |
   | ElevenLabs | elevenlabs.io |

5. **Run the agent**
   ```bash
   python agent.py start
   ```

## Testing

Use the LiveKit Cloud Console at `cloud.livekit.io` → Agents → Console → Start a session.

The agent will greet you and walk through the VIN lookup flow. Test VIN: `1HGCM82633A123456`.
