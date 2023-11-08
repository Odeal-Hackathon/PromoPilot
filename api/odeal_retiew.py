from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from decouple import config

api_base = config('CS_API_BASE')
api_key = config('CS_API_KEY')


def retrieve_documentation(question: str):
    search_client = SearchClient(
        endpoint=api_base,
        index_name="odeal-index",
        credential=AzureKeyCredential(api_key)
    )

    results = search_client.search(
        search_text=question,
        top=2,
        search_fields=['content']
    )

    return [{"content": doc["content"]} for doc in results]