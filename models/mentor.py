from pydantic import BaseModel


class mentor(BaseModel):
    """
    Represents the data structure of a mentor.
    """

    name: str
    location: str
    price: str
    experience: str
    skills: float
    domain: int
    description: str
 