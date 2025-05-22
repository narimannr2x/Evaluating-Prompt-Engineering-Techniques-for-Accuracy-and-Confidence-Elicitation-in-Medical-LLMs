from pydantic import BaseModel, Field


class FinalAnswer(BaseModel):
    justification: str = Field(
        ...,
        description="every steps that stated in prompt which isnt final answer or confidence score"
    )
    final_answer: int = Field(
        ...,
        description="The numerical final answer value. it should be 1 or 2 or 3 or 4"
    )
    confidence_score: int = Field(
        ...,
        description="A score indicating the confidence level of the final answer. from 1 to 10  or 1 to 100 based on your given instruction"
    )

    