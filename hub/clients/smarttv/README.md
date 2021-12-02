# smarttv
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import smarttv
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import smarttv
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import smarttv
from pprint import pprint
from smarttv.api import default_api
from smarttv.model.inline_response200 import InlineResponse200
from smarttv.model.inline_response2001 import InlineResponse2001
from smarttv.model.inline_response2002 import InlineResponse2002
from smarttv.model.inline_response2003 import InlineResponse2003
from smarttv.model.inline_response2004 import InlineResponse2004
from smarttv.model.user import User
# Defining the host is optional and defaults to http://localhost:9081
# See configuration.py for a list of all supported configuration parameters.
configuration = smarttv.Configuration(
    host = "http://localhost:9081"
)



# Enter a context with an instance of the API client
with smarttv.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "ionel" # str | 
canal = "nasultv" # str | 

    try:
        api_instance.add_channel_username_canal_post(username, canal)
    except smarttv.ApiException as e:
        print("Exception when calling DefaultApi->add_channel_username_canal_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:9081*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**add_channel_username_canal_post**](docs/DefaultApi.md#add_channel_username_canal_post) | **POST** /addChannel/{username}/{canal} | 
*DefaultApi* | [**get_history_and_recommandations_nume_get**](docs/DefaultApi.md#get_history_and_recommandations_nume_get) | **GET** /getHistoryAndRecommandations/{nume} | 
*DefaultApi* | [**get_suggested_channels_gen_varsta_get**](docs/DefaultApi.md#get_suggested_channels_gen_varsta_get) | **GET** /getSuggestedChannels/{gen}/{varsta} | 
*DefaultApi* | [**get_users_get**](docs/DefaultApi.md#get_users_get) | **GET** /getUsers | 
*DefaultApi* | [**get_users_json_get**](docs/DefaultApi.md#get_users_json_get) | **GET** /getUsersJSON | Loads users into output_users.json file.
*DefaultApi* | [**insert_user_username_varsta_post**](docs/DefaultApi.md#insert_user_username_varsta_post) | **POST** /insertUser/{username}/{varsta} | 
*DefaultApi* | [**notification_distance_size_current_distance_get**](docs/DefaultApi.md#notification_distance_size_current_distance_get) | **GET** /notificationDistance/{size}/{current_distance} | 
*DefaultApi* | [**set_brightness_level_post**](docs/DefaultApi.md#set_brightness_level_post) | **POST** /setBrightness/{level} | 
*DefaultApi* | [**set_brightness_our_sensor_post**](docs/DefaultApi.md#set_brightness_our_sensor_post) | **POST** /setBrightnessOurSensor | Loads brightness from (another) file.
*DefaultApi* | [**set_brightness_sensor_post**](docs/DefaultApi.md#set_brightness_sensor_post) | **POST** /setBrightnessSensor | Loads brightness from file.
*DefaultApi* | [**timp_idle_time_post**](docs/DefaultApi.md#timp_idle_time_post) | **POST** /timp-idle/{time} | 
*DefaultApi* | [**timp_last_get**](docs/DefaultApi.md#timp_last_get) | **GET** /timp-last | 
*DefaultApi* | [**timp_start_get**](docs/DefaultApi.md#timp_start_get) | **GET** /timp-start | 


## Documentation For Models

 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [User](docs/User.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in smarttv.apis and smarttv.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from smarttv.api.default_api import DefaultApi`
- `from smarttv.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import smarttv
from smarttv.apis import *
from smarttv.models import *
```
