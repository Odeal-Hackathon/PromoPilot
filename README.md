# PromoPilot - GEN AI CHATBOT

This application was developed as part of the Ödeal GPT Hackathon. It's a generative AI-based chatbot designed to offer customers special campaigns and promotions.
You send your message by choosing the member business ID or general category. A customized response is then returned.

## Technologies Used

The main technologies utilized:

- [Python Flask](https://flask.palletsprojects.com/en/3.0.x/) - Python version: 3.11 
- [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/) - Bootstrap version: 5.1
- [Javascript](https://blog.jquery.com/2021/03/02/jquery-3-6-0-released/) - Javascript version: Jquery 3.6

---

## Requirements

### Environment

Ensure that your Python version is set to `3.11`:

```bash
python --version
```

- Setting up Virtualenv:

```bash
pip install virtualenv
```
- Creating a Virtual Environment:
```bash
virtualenv venv
```
- Activating the Virtual Environment:
```bash
source venv/bin/activate
```
- Installing the necessary libraries:
```bash
pip install -r requirements.txt
```

### Configuration

Set up your .env file:

```bash
cd <project-directory>
```

Add environment variables to the touch .env file.

- Then, add the following environment variables into the .env file:

```bash
API_KEY=<apikey>
REST_ENDPOINT=<endpoint>
SECRET_KEY=<asıri-gizli-bisi>

DATABASE_URL=postgresql://postgres:postgres@localhost/postgres

# Azure Cosmos DB
COSMOS_DATABASE=db
COSMOS_CONTAINER=container
COSMOS_ENDPOINT=endpoint
COSMOS_KEY=key

# Azure Cognitive Search
CS_API_BASE=cognitive-search.search.windows.net
CS_API_KEY=key

OPENAI_API_KEY=key
AZURE_API_BASE=azure

```

### Server Settings

- Building the Docker Image:
```bash
docker build -t promopilot:latest .
```

- Launching the Docker Container:
```bash
docker run -p 5001:5001 promopilot:latest
```
