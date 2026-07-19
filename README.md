# Backend for FOSSLingo

### Deploying (Vercel preferred)
1. Create a Vercel account and link your Github account to it (Create a Github account if you don't have one)
2. Fork `FOSSLingo/backend`
3. In Vercel, select "Import Project" and select "backend". This is the repo we forked.
4. Click "Deploy", and note down the URL it gives you! This URL will be used in your selfhosted frontend.

### Self hosting deploy
1. Clone this repo somewhere easy to access
2. Create a Python venv: `uv venv venv`
3. Activate the venv: `venv\Scripts\activate`
4. Install dependencies: `uv pip install -r requirements.txt`'
5. Start server: `fastapi run main.py --host 0.0.0.0 --port 8000`