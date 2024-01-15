from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model for request
class MatrixInput(BaseModel):
    matrix: List[List[int]]

def largest_rectangle(matrix: List[List[int]]) -> tuple:
    if not matrix or not matrix[0]:
        raise ValueError("Invalid matrix input")

    rows, cols = len(matrix), len(matrix[0])
    max_area = 0
    result_number = None

    for r in range(rows):
        for c in range(cols):
            num = matrix[r][c]
            if num != -9:
                current_area = 0
                stack = []
                min_col = cols

                for i in range(r, rows):
                    for j in range(c, cols):
                        if matrix[i][j] == num:
                            matrix[i][j] = -9
                            current_area += 1

                            while stack and stack[-1][1] >= j:
                                _, popped_col = stack.pop()
                                min_col = min(min_col, popped_col)

                            stack.append((i, j))
                            min_col = min(min_col, j)

                            current_area = (i - r + 1) * (min_col - c + 1)

                            if current_area > max_area:
                                max_area = current_area
                                result_number = num

                        else:
                            break

    return result_number, max_area

# Log request and response
def log_request_response(request, response, elapsed_time):
    log_entry = {
        "timestamp": time.time(),
        "request": request.json(),
        "response": json.dumps(response),  # Use json.dumps() for dictionaries
        "elapsed_time": elapsed_time,
    }
    


# FastAPI endpoint
@app.post("/largest_rectangle", response_model=dict)
async def find_largest_rectangle(input_data: MatrixInput):
    start_time = time.time()

    try:
        result = largest_rectangle(input_data.matrix)
        elapsed_time = time.time() - start_time

        # Log request and response
        log_request_response(input_data, {"result": result}, elapsed_time)

        return {"result": result}

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

