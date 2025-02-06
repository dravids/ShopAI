# ShopAI
One single app for all your shopping needs

# ShopAI Setup Guide

## Local Development Setup

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
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Start the development server
```bash
uvicorn src.main:app --reload --port 8000
```