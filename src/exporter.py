from typing import List, Dict
import json
from datetime import datetime
import logging

# Configure logging format and level
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataExporter:
    """
    Handles exporting customer data to JSON files and generating summary reports.
    
    Features:
    - Export customer data with metadata
    - Generate data quality summary
    - Generate overall summary report with average quality score
    """
    
    def export_customers(self, customers: List[Dict], output_file: str):
        """
        Export customer data to a JSON file including metadata.
        
        Args:
            customers (List[Dict]): List of processed customer dictionaries.
            output_file (str): Path to the output JSON file.
        """
        # Prepare metadata for the export
        metadata = {
            "total_customers": len(customers),
            "export_timestamp": datetime.utcnow().isoformat() + "Z",
            "data_quality_summary": self._quality_summary(customers)
        }

        # Combine metadata with sorted customer data
        data = {
            "metadata": metadata,
            "customers": sorted(customers, key=lambda x: x["full_name"])  # Sort by full name
        }

        # Write data to JSON file
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)
        
        logging.info(f"Exported {len(customers)} customers to {output_file}")

    def _quality_summary(self, customers: List[Dict]) -> Dict:
        """
        Generate a summary of customer data quality levels.
        
        Args:
            customers (List[Dict]): List of customer dictionaries.
        
        Returns:
            Dict: Summary counts of high, medium, and low quality customers.
        """
        high = sum(1 for c in customers if c["data_quality_score"] >= 90)
        medium = sum(1 for c in customers if 70 <= c["data_quality_score"] < 90)
        low = sum(1 for c in customers if c["data_quality_score"] < 70)
        
        return {
            "high_quality": high,
            "medium_quality": medium,
            "low_quality": low
        }

    def generate_summary_report(self, customers: List[Dict]) -> Dict:
        """
        Generate an overall summary report of customers including average quality score.
        
        Args:
            customers (List[Dict]): List of customer dictionaries.
        
        Returns:
            Dict: Summary report with total customers and average data quality score.
        """
        if not customers:
            return {"total_customers": 0, "average_quality_score": 0}
        
        # Calculate average data quality score
        avg_score = sum(c["data_quality_score"] for c in customers) / len(customers)
        
        summary = {
            "total_customers": len(customers),
            "average_quality_score": avg_score
        }
        
        logging.info(f"Summary report: {summary}")
        return summary
