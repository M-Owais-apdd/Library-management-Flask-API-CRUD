# Library-management-Flask-API-CRUD
a Flask API for a "Library Management System" that allows CRUD operations for books and members.
Instruction

Open your terminal or command prompt and navigate to the directory where your main.py file is located
Execute the following command to run the Flask application: python main.py
You should see output indicating that the Flask server is running, typically something like:  Running on http://127.0.0.1:5000/

Using Postman
Download and Install Postman: If you haven't already, download and install Postman from Postman's official website.

Open Postman: Launch the Postman application.

Create a New Request:

Click on the "New" button or the "+" tab to create a new request.
Select "HTTP Request".
Set the Request Type:

Change the request type from GET to POST using the dropdown menu.
Enter the URL:

In the URL field, enter the endpoint for adding a book or member. For example, to add a book, use:

Verify

Open In Editor
Run
Copy code
http://127.0.0.1:5000/books
Set the Headers:

Click on the "Headers" tab.
Add a new header:
Key: Authorization
Value: secret_token (or whatever token you are using for authentication)
Set the Body:

Click on the "Body" tab.
Select "raw" and then choose "JSON" from the dropdown.
Enter the JSON data you want to send. For example, to add a book:
json

Verify

Open In Editor
Run
Copy code
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald"
}
Send the Request:

Click the "Send" button.
You should see a response in the lower section of Postman indicating whether the book was added successfully. 
