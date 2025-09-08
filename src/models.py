from pydantic import BaseModel, EmailStr
from typing import Optional

class Customer(BaseModel):
    """
    Pydantic model representing a Customer.
    
    Attributes:
        customer_id (int): Unique identifier for the customer.
        full_name (str): Full name of the customer.
        email (Optional[EmailStr]): Customer's email address (optional).
        engagement_level (str): Level of engagement (e.g., high, medium, low).
        activity_status (str): Status of activity (e.g., active, inactive).
        acquisition_channel (str): How the customer was acquired 
                                   (e.g., website, mobile_app, email_campaign).
        market_segment (str): Market segment the customer belongs to 
                              (e.g., US-West, US-East, EU-Central, APAC).
        customer_tier (str): Customer tier (e.g., basic, premium, enterprise).
        data_quality_score (int): Quality score of the customer data (0-100).
    """
    
    customer_id: int
    full_name: str
    email: Optional[EmailStr]
    engagement_level: str
    activity_status: str
    acquisition_channel: str
    market_segment: str
    customer_tier: str
    data_quality_score: int
