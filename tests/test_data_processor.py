import pytest
from src.data_processor import CustomerDataProcessor

def test_data_processor_transformation():
    raw_customers = [
        {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"},
        {"id": 2, "first_name": "Jane", "last_name": "", "email": None},
        {"id": 3, "first_name": "", "last_name": "", "email": "bademail@example.com"}
    ]
    processor = CustomerDataProcessor()
    processed = processor.process_customers(raw_customers)

    for c in processed:
        assert "customer_id" in c
        assert isinstance(c["customer_id"], int)
        assert "full_name" in c
        assert "email" in c
        assert "engagement_level" in c
        assert "data_quality_score" in c

def test_data_quality_scoring():
    processor = CustomerDataProcessor()
    raw_customers = [
        {"id": 1, "first_name": "Valid", "last_name": "User", "email": "valid@example.com"},
        {"id": 2, "first_name": "", "last_name": "", "email": None},
    ]
    processed = processor.process_customers(raw_customers)
    assert processed[0]["data_quality_score"] == 100
    assert processed[1]["data_quality_score"] == 80  # missing name & email

def test_edge_cases():
    processor = CustomerDataProcessor()
    malformed_customers = [
        {},  # empty
        {"id": None, "first_name": None, "last_name": None, "email": None},
        {"id": 4, "first_name": "Test", "last_name": "User", "email": "invalidemail@example.com"}
    ]
    processed = processor.process_customers(malformed_customers)
    for c in processed:
        assert isinstance(c["customer_id"], int)
        assert "full_name" in c
        assert "email" in c
        assert "data_quality_score" in c
