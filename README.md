# ShopAI
One single app for all your shopping needs

# Setup Guide

There are two ways to set up the ShopAI development environment:
1. Local Python setup with uvicorn
2. Docker/DevContainer setup

## 1. Local Python Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/shopai.git
cd shopai
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the development server:
```bash
uvicorn src.main:app --reload --port 8000
```

The API will be available at:
- API: http://localhost:8000
- Interactive API docs: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc

## 2. Docker/DevContainer Setup

### Option A: Using VS Code DevContainer

1. Prerequisites:
   - Install [Docker](https://docs.docker.com/get-docker/)
   - Install [VS Code](https://code.visualstudio.com/)
   - Install [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension

2. Open in DevContainer:
   - Open VS Code
   - Open the ShopAI folder
   - When prompted, click "Reopen in Container"
   - Or use Command Palette (F1): "Remote-Containers: Open Folder in Container"

The development server will start automatically on port 8001.

### Option B: Using Docker Compose

1. Prerequisites:
   - Install [Docker](https://docs.docker.com/get-docker/)
   - Install [Docker Compose](https://docs.docker.com/compose/install/)

2. Build and start the container:
```bash
docker-compose up --build
```

The API will be available at:
- API: http://localhost:8001
- Interactive API docs: http://localhost:8001/docs
- Alternative API docs: http://localhost:8001/redoc

## Verifying the Setup

Test the API is running by making a request to the ping endpoint:
```bash
curl http://localhost:8000/ping  # For local setup
# or
curl http://localhost:8001/ping  # For Docker setup
```

You should receive: `{"response":"pong"}`
