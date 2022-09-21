# Profiles REST API

Profiles REST API course code.

API VIEW & VIEWSET -> classes for writing api

API VIEW

- describe logic to make API endpoint
- match functions standard http methods
- GET -> fetch item
- POST -> create item
- PUT -> update item
- PATCH -> partially update item
- DELETE -> delete item

When to use?

- full control over the logic
- processing files and rendering a synchronous reponse
- calling other APIs/services in same request
- accessing local files or data

Note:
Serializer

- feature from ret frasmewokr, convert data inputs into python objects

VIEWSET

- uses model operations for functions e.g. list to get list of objects, create to create objects ..
- perfect for standard database operations
- a quick / simple api
- little to no customization on logic
