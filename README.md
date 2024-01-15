To test the FastAPI service with the provided code, you can follow these steps:

Install FastAPI and Uvicorn if you haven't already:

bash

Copy code

pip install fastapi uvicorn

Save the provided code in a file, for example, main.py.

Run the FastAPI server using Uvicorn:

bash

Copy code

uvicorn main:app --reload

Replace main with the name of your file (without the extension if using a different name).

Once the server is running, you can test the API using a tool like curl, Postman, or a web browser.

Using curl from the command line:

bash

Copy code

curl -X POST -H "Content-Type: application/json" -d '{"matrix": [[1,1,1,0,1,-9],[1,1,1,1,2,-9],[1,1,1,1,2,-9],[1,0,0,0,5,-9],[5,0,0,0,5,-9]]}' http://127.0.0.1:8000/largest_rectangle

Using Postman or another API testing tool, send a POST request to http://127.0.0.1:8000/largest_rectangle with the JSON payload:

json

Copy code

{
  "matrix": [
    [1,1,1,0,1,-9],
    [1,1,1,1,2,-9],
    [1,1,1,1,2,-9],
    [1,0,0,0,5,-9],
    [5,0,0,0,5,-9]
  ]
}

Make sure to adapt the matrix values as needed.

Check the response from the API, and the server console will display logs indicating the request, response, and elapsed time.

Note: The provided example assumes that the FastAPI service is running locally on http://127.0.0.1:8000. If you deploy the service elsewhere, adjust the URL accordingly.

Sample Check:

![FastAPI-Swagger-UI](https://github.com/alen0577/largest_rectangle/assets/96831425/47816822-effa-4f53-84d7-7383155753ff)

