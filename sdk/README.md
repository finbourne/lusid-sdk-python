# Running SDK Tests

Build and run the container using `docker-compose`

```
$ docker-compose up && docker-compose rm -f
```

Alernatively run using `docker` commands

Build the container which installs Python 3 and associated dependencies
```
$ docker build -t finbourne/lusid-sdk-python-test .
```

Run the tests
```
$ docker run -it --rm --name lusid-sdk-python-test -v `pwd`:/usr/src finbourne/lusid-sdk-python-test
```

## Test Configuration

Create a file named `secrets.json` in the `tests` folder with the structure below and populated with the appropriate values.

``` json
{
  "api" : {
    "tokenUrl": "",
    "username": "",
    "password": "",
    "clientId": "",
    "clientSecret": "",
    "apiUrl": ""
  }
}
```

| Key | Description |
| --- | --- |
| `tokenUrl` | Okta endpoint to generate the authentication token.  This will be of the form https://lusid.okta.com/oauth2/<key\>/v1/token |
| `username` | Okta username |
| `password` | Okta password |
| `clientId` | Okta client identifier |
| `clientSecret` | Okta client secret |
| `apiUrl` | API url |