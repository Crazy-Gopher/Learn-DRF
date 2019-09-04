## PUT /api/<int:user_id>/user/  XML data
import requests

url = "http://localhost:8000/polls/api/users/11/"

payload = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<root>\n    <username>kapil_jain1</username>\n    <first_name>Kapil1</first_name>\n    <last_name>Jain1</last_name>\n    <email>kapiljain.jain93@gmail.com</email>\n    <date_joined>2019-07-18T14:16:59.342329Z</date_joined>\n    <password>Test@123</password>\n</root>"
headers = {
    'Authorization': "1234",
    'Accept': "application/xml",
    'Content-Type': "application/xml",
    'cache-control': "no-cache",
    'Postman-Token': "2fd28908-61c2-4f91-8730-8c068d6665f7"
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)

"""
<?xml version="1.0" encoding="utf-8"?>
<root>
    <id>11</id>
    <username>kapil_jain1</username>
    <last_name>Jain1</last_name>
    <first_name>Kapil1</first_name>
    <email>kapiljain.jain93@gmail.com</email>
    <date_joined>2019-07-18T14:16:59.342329Z</date_joined>
    <is_superuser>False</is_superuser>
    <is_staff>False</is_staff>
    <last_login></last_login>
    <is_active>True</is_active>
    <password>Test@123</password>
</root>
"""


## POST /api/user/ JSON Data
import requests

url = "http://localhost:8000/polls/api/users/"

payload = "{\n    \"username\": \"kapil_jain\",\n    \"last_name\": \"Jain\",\n    \"first_name\": \"Kapil\",\n    \"email\": \"kapiljain.jain93@gmail.com\",\n    \"password\": \"Test@123\"\n}"
headers = {
    'Authorization': "1234",
    'Accept': "application/json",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "d29059a9-4714-44e4-9999-4851dda5ee3b"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

"""
{
    "success": true,
    "user": {
        "id": 12,
        "username": "kapil_jain",
        "last_name": "Jain",
        "first_name": "Kapil",
        "email": "kapiljain.jain93@gmail.com",
        "date_joined": "2019-07-19T06:12:39.126928Z",
        "is_superuser": false,
        "is_staff": false,
        "last_login": null,
        "is_active": true,
        "password": "pbkdf2_sha256$150000$jN4d5if3OxRJ$pR7l5lpfr0vRMfODKG7ozWSs3LVnmygDYrzuQo8+vTU="
    }
}
"""