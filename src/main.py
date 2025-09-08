from .api_client import CustomerAPIClient
from .data_processor import CustomerDataProcessor
from .exporter import DataExporter
import os

def main():
    """
    Main function to run the customer data pipeline:
    1. Fetch customers from the API
    2. Process and enrich customer data
    3. Export processed data to a JSON file
    4. Generate and log a summary report
    """
    # Base URL of the customer API
    base_url = "https://reqres.in/api"
    
    # Initialize API client and fetch raw customer data
    client = CustomerAPIClient(base_url)
    raw_customers = client.fetch_all_customers()

    # Process raw customer data to validated and enriched format
    processor = CustomerDataProcessor()
    processed_customers = processor.process_customers(raw_customers)

    # Export processed data to JSON file
    exporter = DataExporter()
    # Save output JSON outside the 'src' folder
    output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sample_output.json")
    exporter.export_customers(processed_customers, output_file)
    
    # Generate and log a summary report
    exporter.generate_summary_report(processed_customers)

# Execute main function when script is run directly
if __name__ == "__main__":
    main()
