import jwt
import datetime
import subprocess
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

GITHUB_APP_PRIVATE_KEY_PEM_FILE_PATH = os.getenv(
    "GITHUB_APP_PRIVATE_KEY_PEM_FILE_PATH"
)  # noqa: E501

GITHUB_APP_ID = os.getenv("GITHUB_APP_ID")

with open(GITHUB_APP_PRIVATE_KEY_PEM_FILE_PATH) as fp:
    private_key = fp.read()
    jwt_payload = jwt.encode(
        {
            # issued at time, 60 seconds in the past to allow for clock drift
            "iat": datetime.datetime.utcnow() - datetime.timedelta(minutes=1),
            # JWT expiration time (10 minute maximum)
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
            # GitHub App's identifier
            "iss": GITHUB_APP_ID,
        },
        private_key,
        algorithm="RS256",
    )
    print(jwt_payload)
    # Verify
    subprocess.run(
        f'curl -i -H "Authorization: Bearer {jwt_payload}" -H "Accept: application/vnd.github+json" https://api.github.com/app',  # noqa: E501
        shell=True,
    )
