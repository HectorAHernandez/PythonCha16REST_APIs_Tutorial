# REST APIs tutorial.
# Python and REST APIs: Interacting With Web Services"
"""
Table of Contents

- REST Architecture
- REST APIs and Web Services:
    . HTTP Methods
    . Status Codes
    . API Endpoints
- REST and Python: Consuming APIs
    . GET
    . POST
    . PUT
    . PATCH
    . DELETE
- REST and Python: Building APIs
    . Identify Resources
    . Define Your Endpoints
    . Pick Your Data Interchange Format
    . Design Success Responses
    . Design Error Responses
- REST and Python: Tools of the Trade
    . Flask
    . Django REST Framework
    . FastAPI
- Conclusion

There's an amazing amount of data available on the Web. Many web services, like
YouTube and GitHub, make their data accessible to third-party applications
through an application programming interface (API). One of the most popular ways
to build APIs is the REST architecture style. Python provides some great tools
not only to get data from REST APIs but also to build your own Python REST APIs.

In this tutorial, you'll learn:
    . What REST architecture is
    . How REST APIs provide access to web data
    . How to consume data from REST APIs using the requests library
    . What steps to take to build a REST API
    . What some popular Python tools are for building REST APIs
By using Python and REST APIs, you can retrieve, parse, update, and manipulate
the data provided by any web service you're interested in.

Free Bonus: Click here to download a copy of the "REST API Examples" Guide
(https://realpython.com/api-integration-in-python/) and
get a hands-on introduction to Python + REST API principles with actionable
examples. """


# REST Architecture:
"""REST stands for representational state transfer and is a software
architecture style that defines a pattern for client and server communications
over a network. REST provides a set of constraints for software architecture
to promote performance, scalability, simplicity, and reliability in the system.

REST defines the following architectural constraints:
- Stateless: The server won't maintain any state between requests from the
    client.
- Client-server: The client and server must be decoupled from each other,
    allowing each to develop independently.
- Cacheable: The data retrieved from the server should be cacheable either by
    the client or by the server.
- Uniform interface: The server will provide a uniform interface for accessing
    resources without defining their representation.
- Layered system: The client may access the resources on the server indirectly
    through other layers such as a proxy or load balancer.
- Code on demand (optional): The server may transfer code to the client that
    it can run, such as JavaScript for a single-page application.

Note, REST is not a specification but a set of guidelines on how to architect
    a network-connected software system."""


# REST APIs and Web Services:
"""A REST web service is any web service that adheres to REST architecture
constraints. These web services expose their data to the outside world through
an API. REST APIs provide access to web service data through public web URLs.

For example, here's one of the URLs for GitHub's REST API
(https://docs.github.com/en/free-pro-team@latest/rest):

https://api.github.com/users/<username>
This URL allows you to access information about a specific GitHub user. You
access data from a REST API by sending an HTTP request to a specific URL and
processing the response. """


# HTTP Methods:
"""REST APIs listen for or "wait for" HTTP methods like GET, POST, and DELETE
to know which operations to perform on the web service's resources. A resource
is any data available in the web service that can be accessed and manipulated
with HTTP requests to the REST API. The HTTP method tells the API which action
to perform on the resource.

While there are many HTTP methods, the five methods listed below are the most
commonly used with REST APIs:

HTTP method	Description
-----------     -----------------------------
GET	        Retrieve an existing resource.
POST	        Create a new resource.
PUT	        Update an existing resource.
PATCH	        Partially update an existing resource.
DELETE	        Delete a resource.
A REST API client application can use these five HTTP methods to manage the
state of resources in the web service."""


# Status Codes:
"""Once a REST API receives and processes an HTTP request, it will return an
HTTP response. Included in this response is an HTTP status code. This status
code provides information about the results of the request. An application
sending requests to the API can check the status code and perform actions based
on the result. These actions could include handling errors or displaying a
success message to a user.

Below is a list of the most common status codes returned by REST APIs:

Code	Meaning	          Description
----    --------------    ---------------------------------------------------- 
200	OK	          The requested action was successful.
201	Created	          A new resource was created.
202	Accepted	  The request was received, but no modification has been
                           made yet.
204	No Content	  The request was successful, but the response has no
                           content.

400	Bad Request	  The request was malformed.
401	Unauthorized	  The client is not authorized to perform the requested
                           action.
404	Not Found	  The requested resource was not found.
415	Unsupported Media Type	The request data format is not supported by the
                           server.
422	UnprocessableEntity  The request data was properly formatted but
                            contained invalid or missing data.
500	InternalServerError  The server threw an error when processing the
                             request.
These ten status codes represent only a small subset of the available HTTP
status codes (https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). Status
codes are numbered based on the category of the result:
Code
range	Category
-----   -------------------
2xx	Successful operation
3xx	Redirection
4xx	Client error
5xx	Server error
HTTP status codes come in handy when working with REST APIs as you'll often
need to perform different logic based on the results of the request."""


# API Endpoints:
"""A REST API exposes a set of public URLs that client applications use to access
the resources of a web service. These URLs, in the context of an API, are called
endpoints.

To help clarify this, take a look at the table below. In this table, you'll see
API endpoints for a hypothetical CRM system. These endpoints are for a customer
resource that represents potential customers in the system:

HTTP
method	API endpoint	          Description
------  -----------------------   ------------------------
GET	/customers	          Get a list of customers.
GET	/customers/<customer_id>  Get a single customer.
POST	/customers	          Create a new customer.
PUT	/customers/<customer_id>  Update a specific customer.
PATCH	/customers/<customer_id>  Partially update a specific customer.
DELETE	/customers/<customer_id>  Delete a specific customer.

Each of the endpoints above performs a different action based on the HTTP
method.

Note: The base URL for the endpoints has been omitted for brevity. In reality,
you'll need the full URL path to access an API endpoint:

https://api.example.com/customers

This is the full URL you'd use to access this endpoint. The base URL is
everything besides /customers. This is "https://api.example.com"

You'll note that some endpoints have <customer_id> at the end. This notation
means you need to append a numeric customer_id to the URL to tell the REST API
which customer you'd like to work with. This is:
             "https://api.example.com/customers/12/"
             "https://api.example.com/customers/4512/"

The endpoints listed above represent only one resource in the system, in this
case the 'customers' resource. Production-ready REST APIs often have tens or
even hundreds of different endpoints to manage the resources in the web service.
"""


# REST and Python: Consuming APIs:
"""To write code that interacts with REST APIs, most Python developers turn to
use the "requests" library to send HTTP requests. This library abstracts away
the complexities of making HTTP requests. It's one of the few projects worth
treating as if it's part of the standard library.

To start using the "requests" library, you need to install it first. You can
use pip to install it:

$ python -m pip install requests
or in my virtual environment:
(REST_API_Proj) PS C:\PythonBasicsBookExercises\cha16\REST_APIs_Tutorial> python
                                                      -m pip install requests

Now that you've got requests installed, you can start sending HTTP requests."""


# GET HTTP Method:
"""GET is one of the most common HTTP methods you'll use when working with
REST APIs. This method allows you to retrieve resources from a given API. GET
is a read-only operation, so you shouldn't use it to modify an existing
resource.

To test out GET and the other methods in this section, you'll use a API service
called JSONPlaceholder (located at https://jsonplaceholder.typicode.com/). This
free service provides fake API endpoints that send back responses that requests
can process. This JSONPlaceholder API Service contains below Resources and
Endpoints or Routes:
Resources
JSONPlaceholder comes with a set of 6 common resources:

/posts	   100 posts
/comments  500 comments
/albums	   100 albums
/photos	   5000 photos
/todos	   200 todos
/users	   10 users
Note: resources have relations. For example: posts have many comments, albums
have many photos, ... see guide for the full list.

Routes
All HTTP methods are supported. You can use http or https for your requests.
GET	/posts
GET	/posts/1
GET	/posts/1/comments
GET	/comments?postId=1
POST	/posts
PUT	/posts/1
PATCH	/posts/1
DELETE	/posts/1

To try this out, start up the Python REPL and run the following commands to
send a GET request to a JSONPlaceholder endpoint:"""
import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos/1"
# api_url = "https://jsonplaceholder.typicode.com/users/1"
# api_url = "https://jsonplaceholder.typicode.com/posts/1"
# api_url = "https://jsonplaceholder.typicode.com/comments/1"
# api_url = "https://jsonplaceholder.typicode.com/albums/1"
# api_url = "https://jsonplaceholder.typicode.com/photos/1"
response_get = requests.get(api_url)
# Output:
# >>> response_get.json()
# {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
# Note: When we ran this statements the Content-Type was not application/json
#       it was 'text/html; charset=utf-8' therefore response.json() generates
#       error.

""" This code calls requests.get() to send a GET request to /todos/1, which
responds with the todo item with the ID 1. Then you can call .json() on the
response object to view the data that came back from the API.

The response data is formatted as JSON, a key-value store similar to a
Python dictionary. It's a very popular data format and the de facto
interchange format for most REST APIs.

Beyond viewing the JSON data from the API, you can also view other things
about the response:"""

if response_get.status_code == 200 and response_get.reason == "OK":
    resp_py = json.loads(response_get.text)  # Deserialize to Python Dict DataType
    print(
        f"\n Successful GET /todos/1, status:  {response_get.status_code} \
reason: {response_get.reason}"
    )
    #  Successful GET /todos/1, status:  200 reason: OK

    resp_userId = resp_py["userId"]
    resp_title = resp_py["title"]
    resp_completed = resp_py["completed"]

    print(f"\nresp_userId: {resp_userId}")
    print(f"resp_title: {resp_title}")
    print(f"resp_completed: {resp_completed}")

    # Now playing with response in json format:
    from_json_userId = response_get.json()["userId"]
    from_json_title = "** -- " + response_get.json()["title"] + " -- **"
    from_json_completed = response_get.json()["completed"]
    print(
        f"\n *** Data directly from response_get.json(): \nuserId: \
{from_json_userId} \ntitle: {from_json_title} \
\ncompleted? {from_json_completed} \n"
    )

else:
    print(
        f"Unsuccessful GET /todos/1 status: {response_get.status_code}  \
reason: {response_get.reason}"
    )

# print(f"response_get.headers --> {response.headers}")
# output: response_get.headers --> {'Date': 'Fri, 14 Apr 2023 00:33:51 GMT',
#         'Content-Type': 'text/html; charset=utf-8',
#'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive',
# 'Status': '200 OK', 'X-Frame-Options': 'SAMEORIGIN',....

# print(response_get.headers["Content-Type"])
# output: text/html; charset=utf-8
"""Here, you access response.status_code to see the HTTP status code. You
can also view the response's HTTP headers with response.headers. This
dictionary contains metadata about the response, such as the Content-Type
of the response. """

# Converting the responded json object to Python Datatype using json.loads(),
# this is deserializing the json object:
import json

resp_py = json.loads(response_get.text)  # Deserialize  the json to Python Dict
print(type(resp_py))
# <class 'dict'>
print(f"\n\nresponse_py in Python DataType --> {resp_py}")
# response in Python DataType --> {'userId': 1, 'id': 1,
#                     'title': 'delectus aut autem', 'completed': False}
user_id = resp_py["userId"]
title = resp_py["title"]
completed = resp_py["completed"]
print(
    f"\n- Task '{title}' executed by user {user_id} is \
completed? {completed}"
)
# - Task 'delectus aut autem' executed by user 1 is completed? False


# POST HTML Method:
"""Now, take a look at how you use requests to POST data to a REST API to
create a new resource. You'll use JSONPlaceholder again, but this time
you'll include JSON data in the request. Here's the data that you'll
send:

{
    "userId": 1,
    "title": "Buy milk",
    "completed": false
}
This JSON contains information for a new todo item. Back in the Python REPL,
or in this code, run the following code to create the new todo: """
import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "By honey", "completed": False}

req_userId = todo["userId"]
req_title = todo["title"]
req_completed = todo["completed"]

response_post = requests.post(api_url, json=todo)
# print(response_post.json())
# Output: {'userId': 1, 'title': 'By honey', 'completed': False, 'id': 201}

if response_post.status_code == 201 and response_post.reason == "Created":
    resp_py = json.loads(response_post.text)  # Deserialize to Python Dict DataType
    print(
        f"\n Successful POST /todos, status:  {response_post.status_code} \
reason: {response_post.reason}"
    )
    #  Successful POST /todos, status:  201 reason: Created

    resp_userId = resp_py["userId"]
    resp_title = resp_py["title"]
    resp_completed = resp_py["completed"]

    print(f"\nreq_userId == resp_userId? {req_userId == resp_userId}")
    print(f"req_title == resp_title? {req_title == resp_title}")
    print(f"req_completed == resp_completed? {req_completed == resp_completed}")
else:
    print(
        f"Unsuccessful POST /todos status: {response_post.status_code}  \
reason: {response_post.reason}"
    )

"""Here, you call requests.post() to create a new todo in the system.

First, you create a dictionary containing the data for your 'todo'. Then you
pass this dictionary to the 'json' keyword argument of requests.post(). When
you do this, requests.post() AUTOMATICALLY sets the request's HTTP header
'Content-Type' to 'application/json'. It also SERIALIZES the 'todo'
dictionary into a JSON string, which it appends to the body of the request.

If you don't use the 'json' keyword argument to supply the JSON data, then
you need to set 'Content-Type' accordingly and serialize the JSON MANUALLY.
Here's an equivalent version to the previous code: """
import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos"

todo = {"userId": 1, "title": "By beer", "completed": False}
headers = {"Content-Type": "application/json"}

response_post2 = requests.post(api_url, data=json.dumps(todo), headers=headers)
# print(f"\n *******")
# print(response_post2.json())
# Output: {'userId': 1, 'title': 'By beer', 'completed': False, 'id': 201}
print(response_post2.status_code)
# Output: 201 --> Created resource.

"""In this code, you add a headers dictionary that contains a single header
Content-Type set to application/json. This tells the REST API that you're
sending JSON data with the request.

You then call requests.post(), but instead of passing the 'todo' dictionary
to the json argument, you first call json.dumps(todo) to serialize it. After
it's serialized, you pass it to the 'data' keyword argument. The 'data'
argument tells requests what data to include in the request. You also pass
the headers dictionary to requests.post() to set the HTTP headers manually.

When you call requests.post() like this, it has the same effect as the
previous code but gives you more control over the request.

Note: json.dumps() comes from the json package in the standard library. This
package provides useful methods for working with JSON in Python.

Once the API responds, you call response.json() to view the JSON. The JSON
includes a generated id for the new todo. The 201 status code tells you
that a new resource was created. """


# PUT HTML Method:
"""Beyond GET and POST, requests provides support for all the other HTTP
methods you would use with a REST API. The following code sends a PUT
request to update an existing todo with new data. Any data sent with a PUT
request will completely replace the existing values of the 'todo' therefore
we ALWAYS NEED TO SEND ALL THE ATTRIBUTES in the object.

You'll use the same JSONPlaceholder endpoint you used with GET and POST,
but this time you'll append 10 to the end of the URL. This tells the REST
API which todo you'd like to update: """
import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos/10"

response = requests.get(api_url)  # GET to have a before picture.
# print(f"\n *******")
# print(response.json())
# Output: {'userId': 1, 'id': 10, 'title': 'illo est ratione doloremque
#          quia maiores aut', 'completed': True}

todo = {"userId": 1, "title": "Dance at Hector party", "completed": True}
req_userId = todo["userId"]
req_title = todo["title"]
req_completed = todo["completed"]

response_put = requests.put(api_url, json=todo)
# print(response_put.json())
# output:
# {'userId': 1, 'title': 'Dance at Hector party', 'completed': True, 'id': 10}
# print(response.status_code)
# output: 200 --> Modified existing resource.
"""Here, you first call requests.get() to view the contents of the existing
todo. Next, you call requests.put() with new JSON data to replace the
existing to-do's values. You can see the new values when you call
response.json(). Successful PUT requests will always return 200 instead of
201 because you aren't creating a new resource but just updating an existing
one """

if response_put.status_code == 200 and response_put.reason == "OK":
    resp_py = json.loads(response_put.text)  # Deserialize to Python Dict DataType
    print(
        f"\n Successful PUT /todos, status:  {response.status_code} \
reason: {response.reason}"
    )
    #  Successful PUT /todos, status:  200 reason: OK

    resp_userId = resp_py["userId"]
    resp_title = resp_py["title"]
    resp_completed = resp_py["completed"]

    print(f"\nreq_userId == resp_userId? {req_userId == resp_userId}")
    print(f"req_title == resp_title? {req_title == resp_title}")
    print(f"req_completed == resp_completed? {req_completed == resp_completed}")
else:
    print(
        f"Unsuccessful PUT /todos status: {response_put.status_code}  \
reason: {response_put.reason}"
    )


# PATCH HTML Method:
"""Next up, you'll use requests.patch() to modify the value of a specific field
on an existing todo. PATCH differs from PUT in that it doesn't completely
replace the existing resource. It only modifies the values set in the JSON sent
with the request.

You'll use the same todo from the last example to try out requests.patch(). Here
are the current values:

{'userId': 1, 'title': 'Wash car', 'completed': True, 'id': 10}
Now you can update the title with a new value: """
import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos/10"

todo = {"title": "Happy Happy"}
req_title = todo["title"]

response_patch = requests.patch(api_url, json=todo)

if response_patch.status_code == 200 and response_patch.reason == "OK":
    resp_py = json.loads(response_patch.text)  # Deserialize to Python Dict DataType
    print(
        f"\n Successful PATCH /todos/10, status:  {response_patch.status_code} \
reason: {response_patch.reason}"
    )
    #  Successful PATCH /todos/10, status:  200 reason: OK

    resp_title = resp_py["title"]

    print(f"req_title == resp_title? {req_title == resp_title}")
else:
    print(
        f"Unsuccessful PATCH /todos/10 status: {response_patch.status_code}  \
reason: {response_patch.reason}"
    )

# print(response_patch.json())
# {'userId': 1, 'id': 10, 'title': 'Happy Happy', 'completed': True}
# print(response_patch.status_code)
# 200
# When you call response.json(), you can see that title was updated to
# Happy Happy.


# DELETE HTML Method:
"""Last but not least, if you want to completely remove a resource, then you
use DELETE. Here's the code to remove a todo:"""
import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos/10"

response_del = requests.delete(api_url)

if response_del.status_code == 200 and response_del.reason == "OK":
    print(
        f"\n Successful DELETE /todos/10, status:  {response.status_code} \
reason: {response.reason}"
    )
    #  Successful DELETE /todos/10, status:  200 reason: OK
else:
    print(
        f"Unsuccessful PATCH /todos/10 status: {response_del.status_code}  \
reason: {response_del.reason}"
    )

# print(response_del.json())
# {}
# print(response_del.status_code)
# 200
"""You call requests.delete() with an API URL that contains the ID for the todo
you would like to remove. This sends a DELETE request to the REST API, which
then removes the matching resource. After deleting the resource, the API sends
back an empty JSON object indicating that the resource has been deleted.

The requests library is an awesome tool for working with REST APIs and an
indispensable part of your Python tool belt. In the next section, you'll change
gears and consider what it takes to build a REST API. """


# REST and Python: Building APIs
"""REST API design is a huge topic with many layers. As with most things in
technology, there's a wide range of opinions on the best approach to building
APIs. In this section, you'll look at some recommended steps to follow as you
build an API."""

# Step 1: Identify Resources
"""The first step you'll take as you build a REST API is to identify the
resources the API will manage. It's common to describe these resources as plural
nouns, like customers, events, or transactions. As you identify different
resources in your web service, you'll build out a list of nouns that describe
the different data users can manage in the API.

As you do this, make sure to consider any nested resources. For example,
customers may have sales, or events may contain guests. Establishing these
resource hierarchies will help when you define API endpoints."""


# Step 2: Define Your Endpoints
"""Once you've identified the resources in your web service, you'll want to use
these to define the API endpoints. Here are some example endpoints for a
"transactions" resource you might find in an API for a payment processing
service:

HTTP
method	API endpoint	                 Description
------  -----------------------------    -----------
GET	/transactions	                 Get a list of transactions.
GET	/transactions/<transaction_id>	 Get a single transaction.
POST	/transactions	                 Create a new transaction.
PUT	/transactions/<transaction_id>	 Update a transaction.
PATCH	/transactions/<transaction_id>	 Partially update a transaction.
DELETE	/transactions/<transaction_id>	 Delete a transaction.

These six endpoints cover all the operations that you'll need to create, read,
update, and delete "transactions" in the web service. Each resource (events,
customers, transactions, sales, ... ) in your web service would have a similar
list of endpoints based on what actions a user can perform with the API.

Note: An endpoint shouldn't contain verbs. Instead, you should select the
appropriate HTTP methods to convey the endpoint's action. For example, the
endpoint below contains an unneeded verb:

GET /getTransactions
Here, get is included in the endpoint when it isn't needed. The HTTP method
GET already provides the semantic meaning for the endpoint by indicating the
action. You can remove get from the endpoint:

GET /transactions
This endpoint contains only a plural noun, and the HTTP method GET communicates
the action.

Now take a look at an example of endpoints for a NESTED RESOURCE. Here, you'll
see endpoints for guests that are nested under events resources:

HTTP
method	API endpoint	                      Description
------  -----------------------------------   --------------
GET	/events/<event_id>/guests	      Get a list of guests.
GET	/events/<event_id>/guests/<guest_id>  Get a single guest.
POST	/events/<event_id>/guests	      Create a new guest.
PUT	/events/<event_id>/guests/<guest_id>  Update a guest.
PATCH	/events/<event_id>/guests/<guest_id>  Partially update a guest.
DELETE	/events/<event_id>/guests/<guest_id>  Delete a guest.

With these endpoints, you can manage guests for a specific event in the system.

This isn't the only way to define an endpoint for nested resources. Some people
prefer to use query strings to access a nested resource. A query string allows
you to send additional parameters with your HTTP request. In the following
endpoint, you append a query string to get guests for a specific event_id:

GET /guests?event_id=23
This endpoint will filter out any guests that don't reference the given
event_id. As with many things in API design, you need to decide which method
fits your web service best."""

# Step 3: API Versioning:
"""Note: It's very unlikely that your REST API will stay the same throughout
the life of your web service. Resources will change, and you'll need to update
your endpoints to reflect these changes. This is where API versioning comes in.
API versioning allows you to modify your API without fear of breaking existing
integrations.

There's a wide range of versioning strategies. Selecting the right option
depends on the requirements of your API. Below are some of the most popular
options for API versioning:

- URI versioning -->
(https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design#uri-versioning)

- HTTP header versioning -->
(https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design#header-versioning)

- Query string versioning -->
 (https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design#query-string-versioning)

- Media type versioning -->
 (https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design#media-type-versioning)

No matter what strategy you select, versioning your API is an important step to
ensuring it can adapt to changing requirements while supporting existing users.

Now that you've covered endpoints, in the next section you'll look at some
options for formatting data in your REST API. """


# Step 4: Pick Your Data Interchange Format
"""Two popular options for formatting web service data are XML and JSON.
Traditionally, XML was very popular with SOAP APIs, but JSON is more popular
with REST APIs. To compare the two, take a look at an example book resource
formatted as XML and JSON.

Here's the book formatted as XML:

<?xml version="1.0" encoding="UTF-8" ?>
<book>
    <title>Python Basics</title>
    <page_count>635</page_count>
    <pub_date>2021-03-16</pub_date>
    <authors>
        <author>
            <name>David Amos</name>
        </author>
        <author>
            <name>Joanna Jablonski</name>
        </author>
        <author>
            <name>Dan Bader</name>
        </author>
        <author>
            <name>Fletcher Heisler</name>
        </author>
    </authors>
    <isbn13>978-1775093329</isbn13>
    <genre>Education</genre>
</book>

XML uses a series of elements to encode data. Each element has an opening and
closing tag, with the data in between. Elements can be nested inside other
elements. You can see this above, where several <author> tags are nested
inside of <authors>.

Now, take a look at the same book in JSON:

{
    "title": "Python Basics",
    "page_count": 635,
    "pub_date": "2021-03-16",
    "authors": [
        {"name": "David Amos"},
        {"name": "Joanna Jablonski"},
        {"name": "Dan Bader"},
        {"name": "Fletcher Heisler"}
    ],
    "isbn13": "978-1775093329",
    "genre": "Education"
}

JSON stores data in key-value pairs similar to a Python dictionary. Like XML,
JSON supports nesting data to any level, so you can model complex data.

Neither JSON nor XML is inherently better than the other, but there's a
preference for JSON among REST API developers. This is especially true when
you pair a REST API with a front-end framework like React or Vue."""


# Design Success Responses
"""Once you've picked a data format, the next step is to decide how you'll
respond to HTTP requests. All responses from your REST API should have a similar
format and include the proper HTTP status code.

In this section, you'll look at some example HTTP responses for a hypothetical
API that manages an inventory of cars. These examples will give you a sense of
how you should format your API responses. To make things clear, you'll look at
raw HTTP requests and responses instead of using an HTTP library like requests.

To start things off, take a look at a GET request to /cars, which returns a
list of cars:
"""

# GET HTPP Method Successful Response Format:
"""
Raw HTTP
GET /cars HTTP/1.1
Host: api.example.com

This HTTP request is made up of four parts:
1- GET is the HTTP method type.
2- /cars is the API endpoint.
3- HTTP/1.1 is the HTTP version.
4- Host: api.example.com is the API host.

These four parts are all you need to send a GET request to /cars. Now take a
look at the response. This API uses JSON as the data interchange format:

Raw HTTP:
HTTP/1.1 200 OK
Content-Type: application/json
...

[
    {
        "id": 1,
        "make": "GMC",
        "model": "1500 Club Coupe",
        "year": 1998,
        "vin": "1D7RV1GTXAS806941",
        "color": "Red"
    },
    {
        "id": 2,
        "make": "Lamborghini",
        "model":"Gallardo",
        "year":2006,
        "vin":"JN1BY1PR0FM736887",
        "color":"Mauve"
    },
    {
        "id": 3,
        "make": "Chevrolet",
        "model":"Monte Carlo",
        "year":1996,
        "vin":"1G4HP54K714224234",
        "color":"Violet"
    }
]

The API returns a response that contains a Python list of cars. You know that
the response was successful because of the 200 OK status code. The response also
has a Content-Type header set to application/json. This tells the user to parse
the response as JSON.

Note: When you're working with a real API, you're going to see more HTTP headers
than this. These headers differ between APIs, so they've been excluded in these
examples.

It's important to always set the correct Content-Type header on your response.
If you send JSON, then set Content-Type to application/json. If XML, then set it
to application/xml. This header tells the user how they should parse the data.

You also want to include an appropriate status code in your response. For any
successful GET request, you should return 200 OK. This tells the user that
their request was processed as expected.


Take a look at another GET request, this time for a single car:

Raw HTTP:
GET /cars/1 HTTP/1.1
Host: api.example.com
This HTTP request queries the API for car 1. Here's the response:

Raw HTTP:
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 1,
    "make": "GMC",
    "model": "1500 Club Coupe",
    "year": 1998,
    "vin": "1D7RV1GTXAS806941",
    "color": "Red"
},

This response contains a SINGLE JSON object with the car's data. Since it's a
SINGLE object, it doesn't need to be wrapped in a list. Like the last
response, this also has a 200 OK status code.

Note: A GET request should never modify an existing resource. If the request
contains data, then this data should be ignored and the API should return the
resource unchanged, like executing the GET without data.

"""

# POST HTPP Method Successful Response Format:
"""
Next up, check out a POST request to add a new car:
Raw HTTP:
POST /cars HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "make": "Nissan",
    "model": "240SX",
    "year": 1994,
    "vin": "1N6AD0CU5AC961553",
    "color": "Violet"
}
This POST request includes JSON for the new car in the request. It sets the
Content-Type header to application/json so the API knows the content type of
the request. The API will create a new car from the JSON.

Here's the response:
Raw HTTP:
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 4,
    "make": "Nissan",
    "model": "240SX",
    "year": 1994,
    "vin": "1N6AD0CU5AC961553",
    "color": "Violet"
}

This response has a 201 "Created" status code AND Message to tell the user that
a new resource was created. Make sure to use 201 Created (status and Message)
instead of 200 OK (status and Message) for all successful POST requests.

This response also includes a copy of the new car with an id generated by the
API. It's important to send back an id in the response so that the user can
modify the resource again.

Note: It's important to always send back a copy of a resource when a user
creates it with POST or modifies it with PUT or PATCH. This way, the user can
see the changes that they've made.

"""

# PUT HTPP Method Successful Response Format:
"""
Now take a look at a PUT request (Put replace all data with the data in the
Request data section, which should include all the attributes):
Raw HTTP:
PUT /cars/4 HTTP/1.1     --> Modify resource with id= 4
Host: api.example.com
Content-Type: application/json

{
    "make": "Buick",
    "model": "Lucerne",
    "year": 2006,
    "vin": "4T1BF3EK8AU335094",
    "color":"Maroon"
}
This request uses the id from the previous request to update the car with all
new data. As a reminder, PUT updates all fields on the resource with new data.

Here's the response:
Raw HTTP:
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 4,
    "make": "Buick",
    "model": "Lucerne",
    "year": 2006,
    "vin": "4T1BF3EK8AU335094",
    "color":"Maroon"
}

The response includes a copy of the car with the new data. Again, you always
want to send back the full resource for a PUT request. The same applies to
a PATCH request:
"""

# PATCH HTPP Method Successful Response Format:
"""
Raw HTTP:
PATCH /cars/4 HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "vin": "VNKKTUD32FA050307",
    "color": "Green"
}
PATCH requests only update a part of a resource. In the request above, the vin
and color fields will be updated with new values. Here's the response:

Raw HTTP:
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 4,
    "make": "Buick",
    "model": "Lucerne",
    "year": 2006,
    "vin": "VNKKTUD32FA050307",
    "color": "Green"
}


The response contains a full copy of the car. As you can see, only the vin and
color fields have been updated.

Finally, take a look at how your REST API should respond when it receives
a DELETE request. Here's a DELETE request to remove a car:
"""

# DELETE HTPP Method Successful Response Format:
"""Raw HTTP:
DELETE /cars/4 HTTP/1.1
This DELETE request tells the API to remove the car with the ID 4. Here's the
response:

Raw HTTP:
HTTP/1.1 204 No Content
This response only includes the status code 204 No Content. This status code
tells a user that the operation was successful, but no content was returned in
the response. This makes sense since the car has been deleted. There's no
reason to send a copy of it back in the response.

The responses above work well when everything goes as planned, but what happens
if there's a problem with the request? In the next section, you'll look at how
your REST API should respond when errors occur.
"""
