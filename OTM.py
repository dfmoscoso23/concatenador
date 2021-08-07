from __future__ import print_function
import time
import meli
from meli.rest import ApiException
from pprint import pprint
# Defining the host, defaults to https://api.mercadolibre.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meli.Configuration(
    host = "https://api.mercadolibre.com"
)


# Enter a context with an instance of the API client
with meli.ApiClient() as api_client:
# Create an instance of the API class
    api_instance = meli.OAuth20Api(api_client)
    grant_type = 'authorization_code' # str
    client_id = '4726037063911819' # Your client_id
    client_secret = 'SKjt3ZUGtiXM90wvOn2xlvraWXEvQH2N' # Your client_secret
    redirect_uri = 'https://localhost:30000' # Your redirect_uri
    code = '8YuuVxJb1EX6FbX3PkvekQRAo1GpWEBr' # The parameter CODE
    refresh_token = 'APP_USR-4726037063911819-070315-04b3c088eb8697c12219d0109d14cc6d-553279780' # Your refresh_token

try:
    # Request Access Token
    api_response = api_instance.get_token(grant_type=grant_type, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, code=code, refresh_token=refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuth20Api->get_token: %s\n" % e)