from fastapi import FastAPI, Request, HTTPException
from typing import List

app = FastAPI()

# This is the filename where we will store each calculation (like a basic database)
FILE_NAME = "history.txt"

@app.post("/calculate/")
async def calculate(request: Request):
    # Extract JSON data from the request body
    data = await request.json()

    # Extract input values: two numbers and the operation to perform
    num1 = request.num1
    num2 = request.num2
    operation = request.operation.lower()

    # Initialize result variable to store the outcome of the operation
    result = None
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero.")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation.")

    with open(FILE_NAME, "a") as file:
        file.write(f"{num1},{num2},{operation},{result}\n")

    """
    TODO: Implement the calculation logic
    - If the operation is "add", add num1 and num2
    - If "subtract", subtract num2 from num1
    - If "multiply", multiply them
    - If "divide", divide num1 by num2 (handle division by zero)
    """

    # TODO: Save the calculation to a text file
    # Each line should be in the format: num1,num2,operation,result
    # For example: 10,5,add,15

    return result  # Return the result of the calculation


@app.get("/history/")
def get_history():
    calculation_history = []
    try:
        with open(FILE_NAME, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    num1, num2, operation, result = parts
                    calculation_history.append({
                        "num1": float(num1),
                        "num2": float(num2),
                        "operation": operation,
                        "result": float(result)
                    })
    except FileNotFoundError:
        calculation_history = []


    # TODO: Read the "history.txt" file and return all records as a list
    # Each record should be converted into a dictionary with keys: num1, num2, operation, result

    """
    Example output:
    [
        {"num1": 10.0, "num2": 5.0, "operation": "add", "result": 15.0},
        {"num1": 20.0, "num2": 4.0, "operation": "divide", "result": 5.0}
    ]
    """

    return calculation_history  # List of all past calculations
