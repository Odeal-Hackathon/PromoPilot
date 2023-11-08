from azure.cosmos import CosmosClient
from decouple import config

endpoint = config('COSMOS_ENDPOINT')
key = config('COSMOS_KEY')
databaseId = config('COSMOS_DATABASE')
containerId = config('COSMOS_CONTAINER')


def customer_lookup(customerId: str = "") -> dict:
    if not customerId:
        return None
    client = CosmosClient(endpoint, credential=key)
    database = client.get_database_client(databaseId)
    container = database.get_container_client(containerId)

    try:
        response = container.read_item(item=customerId, partition_key=customerId)
        return response
    except Exception as e:
        return None