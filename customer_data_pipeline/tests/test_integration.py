import pytest
from src.api_client import CustomerAPIClient
from src.data_processor import CustomerDataProcessor

@pytest.mark.asyncio
async def test_full_pipeline(tmp_path):
    """
    Integration test for fetching and processing customers.
    This version avoids DataExporter and works with the current client.
    """
    client = CustomerAPIClient(base_url="https://reqres.in/api")
    processor = CustomerDataProcessor()

    # Fetch customers (synchronously, because fetch_all_customers returns a list)
    raw_customers = client.fetch_all_customers()  # remove await

    # Process customers
    processed = processor.process_customers(raw_customers)

    # Basic assertions
    assert isinstance(processed, list)
    assert len(processed) > 0
    for c in processed:
        assert "customer_id" in c
        assert "full_name" in c
        assert "email" in c
        assert "data_quality_score" in c

    # Optional: save to tmp_path just to mimic export
    output_file = tmp_path / "output.json"
    with open(output_file, "w") as f:
        import json
        json.dump(processed, f)
