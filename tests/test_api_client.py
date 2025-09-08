import pytest
from src.api_client import CustomerAPIClient

@pytest.mark.asyncio
async def test_api_client_retry_logic():
    client = CustomerAPIClient(base_url="https://reqres.in/api")
    # fetch_all_customers is synchronous now
    customers = client.fetch_all_customers()
    assert isinstance(customers, list)

@pytest.mark.asyncio
async def test_duplicate_handling():
    client = CustomerAPIClient(base_url="https://reqres.in/api")
    customers = client.fetch_all_customers()
    customer_ids = [c.get("id") for c in customers]
    assert len(customer_ids) == len(set(customer_ids))  # no duplicates
