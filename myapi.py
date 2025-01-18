from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define the expected input fields
class CodeSnippet(BaseModel):
    code: str
    language: str

@app.post("/api/test-code")
def analyze_code(payload: CodeSnippet):
    """
    Expects JSON with 'code' and 'language'.
    Example:
    {
      "code": "function hello(){ return 'Hello'; }",
      "language": "JavaScript"
    }
    """
    # If code is empty, raise a 400 Bad Request
    if not payload.code.strip():
        raise HTTPException(status_code=400, detail='The "code" field cannot be empty.')

    # Mock AI logic: just return some dummy test cases & suggestions
    mock_test_cases = [
        "Test 1: Verify function runs without errors",
        "Test 2: Check edge cases"
    ]
    mock_suggestions = "Add error handling for invalid input."

    # Build and return the response
    response = {
        "testCases": mock_test_cases,
        "suggestions": mock_suggestions
    }
    return response


