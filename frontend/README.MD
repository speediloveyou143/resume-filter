# RAG model for Resume filtering
# Tech-stack
---------------
1. frontend(streamlit)
2. backend(python,Flask,REST Apis,NLP)
3. database(mongo db)
4. gen-ai(RAG,Prompt-techniques,LLM)

# Project-setup
- frontend
  - venv(development)
  - requirements.txt
  - app.py
  - Readme.md
  - .env(development)
- backend
  - venv(development)
  - requirements.txt
  - server.py
  
# Project Running commands
- frontend
  - cd frontend(mac,linux,windows)
  - python -m venv venv(mac,linux,windows)
  - source venv/bin/activate(mac/linux),venv\scripts\activate(windows)
  - pip install -r requirements.txt(mac,linux,windows)
  - streamlit run app.py(mac,linux,windows)
- backend
  - cd backend(mac,linux,windows)
  - python -m venv venv(mac,linux,windows)
  - source venv/bin/activate(mac/linux),venv\scripts\activate(windows)
  - pip install -r requirements.txt(mac,linux,windows)
  - python server.py(mac,linux,windows)
  
# Project features
- frontend
  1. streamlit file uploading button
  2. reading pdf documents
  3. Api calling
- backend
