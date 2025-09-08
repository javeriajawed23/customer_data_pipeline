from typing import List, Dict
from .models import Customer
import random

class CustomerDataProcessor:
    """
    Processes raw customer data and transforms it into validated and enriched format.
    """

    def process_customers(self, raw_customers: List[Dict]) -> List[Dict]:
        processed = []

        for cust in raw_customers:
            # Ensure valid integer for customer_id
            customer_id = cust.get("id")
            if not isinstance(customer_id, int):
                customer_id = 0

            # Full name
            first_name = cust.get("first_name") or ""
            last_name = cust.get("last_name") or ""
            full_name = f"{first_name} {last_name}".strip()

            # Email and domain
            email = cust.get("email")
            email_domain = email.split("@")[-1] if email else "unknown"

            # Random attributes
            engagement_level = random.choice(["high", "medium", "low"])
            activity_status = random.choice(["active", "inactive"])
            acquisition_channel = random.choice(["website", "mobile_app", "email_campaign"])
            market_segment = random.choice(["US-West", "US-East", "EU-Central", "APAC"])
            customer_tier = random.choice(["basic", "premium", "enterprise"])

            # Data quality
            quality_score = 100
            if not email:
                quality_score -= 10
            if not full_name:
                quality_score -= 10

            # Create Customer model
            validated = Customer(
                customer_id=customer_id,
                full_name=full_name,
                email=email,
                engagement_level=engagement_level,
                activity_status=activity_status,
                acquisition_channel=acquisition_channel,
                market_segment=market_segment,
                customer_tier=customer_tier,
                data_quality_score=quality_score
            )

            processed.append(validated.model_dump())  # Pydantic v2

        return processed
