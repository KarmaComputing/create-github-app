# Create a Github app minimal example

This code verifies GitHub app api access by

1. Creates a signed `jwt` using the Github app private key
2. Uses `curl` to send a request with the `jwt` token to verify the token

It is based on the [official GitHub Ruby example](https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#authenticating-as-a-github-app), converted into python.

## Setup
- Create Github app
- Verify api access with private key
- See: https://docs.github.com/en/developers/apps/building-github-apps/creating-a-github-app 

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Settings

Edit env:
```
cp .env.example .env
```

## Run
```
python3 authenticate.py
```

Response:
```
(venv) $ python authenticate.py                                                                                                    
HTTP/2 200                                                                                                                         
server: GitHub.com                                                                                                                 
content-type: application/json; charset=utf-8                                                                                      
... more
```

Then, you should see a response from GitHub which sends back your app information.
If OK, then authentication was a success (note that the `jwt` is signed for a maximum of
10 minutes).
