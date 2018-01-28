# pyrebrickable

Python Rebrickable http://www.rebrickable.com client using the openAPI json provided

generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 
- Package version: 0.1.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.3+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/rienafairefr/pyrebrickable.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/rienafairefr/pyrebrickable.git`)

Then import the package:
```python
import rebrickable
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rebrickable
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = rebrickable.LegoApi()
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)

try:
    # Get a list of all Colors.
    api_instance.lego_colors_list(page=page, page_size=page_size, ordering=ordering)
except ApiException as e:
    print("Exception when calling LegoApi->lego_colors_list: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://rebrickable.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*LegoApi* | [**lego_colors_list**](docs/LegoApi.md#lego_colors_list) | **GET** /api/v3/lego/colors/ | Get a list of all Colors.
*LegoApi* | [**lego_colors_read**](docs/LegoApi.md#lego_colors_read) | **GET** /api/v3/lego/colors/{id}/ | Get details about a specific Color.
*LegoApi* | [**lego_elements_read**](docs/LegoApi.md#lego_elements_read) | **GET** /api/v3/lego/elements/{element_id}/ | Get details about a specific Element ID.
*LegoApi* | [**lego_mocs_parts_list**](docs/LegoApi.md#lego_mocs_parts_list) | **GET** /api/v3/lego/mocs/{set_num}/parts/ | Get a list of all Inventory Parts in this MOC.
*LegoApi* | [**lego_mocs_read**](docs/LegoApi.md#lego_mocs_read) | **GET** /api/v3/lego/mocs/{set_num}/ | Get details for a specific MOC.
*LegoApi* | [**lego_part_categories_list**](docs/LegoApi.md#lego_part_categories_list) | **GET** /api/v3/lego/part_categories/ | Get a list of all Part Categories.
*LegoApi* | [**lego_part_categories_read**](docs/LegoApi.md#lego_part_categories_read) | **GET** /api/v3/lego/part_categories/{id}/ | Get details about a specific Part Category.
*LegoApi* | [**lego_parts_colors_list**](docs/LegoApi.md#lego_parts_colors_list) | **GET** /api/v3/lego/parts/{part_num}/colors/ | Get a list of all Colors a Part has appeared in.
*LegoApi* | [**lego_parts_colors_read**](docs/LegoApi.md#lego_parts_colors_read) | **GET** /api/v3/lego/parts/{part_num}/colors/{color_id}/ | Get details about a specific Part/Color combination.
*LegoApi* | [**lego_parts_colors_sets_list**](docs/LegoApi.md#lego_parts_colors_sets_list) | **GET** /api/v3/lego/parts/{part_num}/colors/{color_id}/sets/ | Get a list of all Sets the Part/Color combination has appeard in.
*LegoApi* | [**lego_parts_list**](docs/LegoApi.md#lego_parts_list) | **GET** /api/v3/lego/parts/ | Get a list of Parts.
*LegoApi* | [**lego_parts_read**](docs/LegoApi.md#lego_parts_read) | **GET** /api/v3/lego/parts/{part_num}/ | Get details about a specific Part.
*LegoApi* | [**lego_sets_alternates_list**](docs/LegoApi.md#lego_sets_alternates_list) | **GET** /api/v3/lego/sets/{set_num}/alternates/ | Get a list of MOCs which are Alternate Builds of a specific Set - i.e. all parts in the MOC can
*LegoApi* | [**lego_sets_list**](docs/LegoApi.md#lego_sets_list) | **GET** /api/v3/lego/sets/ | Get a list of Sets, optionally filtered by any of the below parameters.
*LegoApi* | [**lego_sets_parts_list**](docs/LegoApi.md#lego_sets_parts_list) | **GET** /api/v3/lego/sets/{set_num}/parts/ | Get a list of all Inventory Parts in this Set.
*LegoApi* | [**lego_sets_read**](docs/LegoApi.md#lego_sets_read) | **GET** /api/v3/lego/sets/{set_num}/ | Get details for a specific Set.
*LegoApi* | [**lego_sets_sets_list**](docs/LegoApi.md#lego_sets_sets_list) | **GET** /api/v3/lego/sets/{set_num}/sets/ | Get a list of all Inventory Sets in this Set.
*LegoApi* | [**lego_themes_list**](docs/LegoApi.md#lego_themes_list) | **GET** /api/v3/lego/themes/ | Return all Themes
*LegoApi* | [**lego_themes_read**](docs/LegoApi.md#lego_themes_read) | **GET** /api/v3/lego/themes/{id}/ | Return details for a specific Theme
*UsersApi* | [**users_allparts_list**](docs/UsersApi.md#users_allparts_list) | **GET** /api/v3/users/{user_token}/allparts/ | Get a list of all the Parts in all the user&#39;s Part Lists as well as the Parts inside Sets in the user&#39;s Set Lists.
*UsersApi* | [**users_badges_list**](docs/UsersApi.md#users_badges_list) | **GET** /api/v3/users/badges/ | Get a list of all the available Badges
*UsersApi* | [**users_badges_read**](docs/UsersApi.md#users_badges_read) | **GET** /api/v3/users/badges/{id}/ | Get details about a specific Badge
*UsersApi* | [**users_build_read**](docs/UsersApi.md#users_build_read) | **GET** /api/v3/users/{user_token}/build/{set_num}/ | Find out how many parts the user needs to build the specified Set.
*UsersApi* | [**users_lost_parts_create**](docs/UsersApi.md#users_lost_parts_create) | **POST** /api/v3/users/{user_token}/lost_parts/ | Add one or more Lost Parts to the user.
*UsersApi* | [**users_lost_parts_delete**](docs/UsersApi.md#users_lost_parts_delete) | **DELETE** /api/v3/users/{user_token}/lost_parts/{id}/ | Remove the Lost Part from the user.
*UsersApi* | [**users_lost_parts_list**](docs/UsersApi.md#users_lost_parts_list) | **GET** /api/v3/users/{user_token}/lost_parts/ | Get a list of all the Lost Parts from the user&#39;s LEGO collection.
*UsersApi* | [**users_partlists_create**](docs/UsersApi.md#users_partlists_create) | **POST** /api/v3/users/{user_token}/partlists/ | Add a new Part List.
*UsersApi* | [**users_partlists_delete**](docs/UsersApi.md#users_partlists_delete) | **DELETE** /api/v3/users/{user_token}/partlists/{list_id}/ | Delete a Part List and all it&#39;s Parts.
*UsersApi* | [**users_partlists_list**](docs/UsersApi.md#users_partlists_list) | **GET** /api/v3/users/{user_token}/partlists/ | Get a list of all the user&#39;s Part Lists.
*UsersApi* | [**users_partlists_partial_update**](docs/UsersApi.md#users_partlists_partial_update) | **PATCH** /api/v3/users/{user_token}/partlists/{list_id}/ | Update an existing Part List&#39;s details.
*UsersApi* | [**users_partlists_parts_create**](docs/UsersApi.md#users_partlists_parts_create) | **POST** /api/v3/users/{user_token}/partlists/{list_id}/parts/ | Add one or more Parts to the Part List.
*UsersApi* | [**users_partlists_parts_delete**](docs/UsersApi.md#users_partlists_parts_delete) | **DELETE** /api/v3/users/{user_token}/partlists/{list_id}/parts/{part_num}/{color_id}/ | Delete a Part from the Part List.
*UsersApi* | [**users_partlists_parts_list**](docs/UsersApi.md#users_partlists_parts_list) | **GET** /api/v3/users/{user_token}/partlists/{list_id}/parts/ | Get a list of all the Parts in a specific Part List.
*UsersApi* | [**users_partlists_parts_read**](docs/UsersApi.md#users_partlists_parts_read) | **GET** /api/v3/users/{user_token}/partlists/{list_id}/parts/{part_num}/{color_id}/ | Get details about a specific Part in the Part List.
*UsersApi* | [**users_partlists_parts_update**](docs/UsersApi.md#users_partlists_parts_update) | **PUT** /api/v3/users/{user_token}/partlists/{list_id}/parts/{part_num}/{color_id}/ | Replace an existing Part&#39;s details in the Part List.
*UsersApi* | [**users_partlists_read**](docs/UsersApi.md#users_partlists_read) | **GET** /api/v3/users/{user_token}/partlists/{list_id}/ | Get details about a specific Part List.
*UsersApi* | [**users_partlists_update**](docs/UsersApi.md#users_partlists_update) | **PUT** /api/v3/users/{user_token}/partlists/{list_id}/ | Replace an existing Part List&#39;s details.
*UsersApi* | [**users_parts_list**](docs/UsersApi.md#users_parts_list) | **GET** /api/v3/users/{user_token}/parts/ | Get a list of all the Parts in all the user&#39;s Part Lists.
*UsersApi* | [**users_profile_list**](docs/UsersApi.md#users_profile_list) | **GET** /api/v3/users/{user_token}/profile/ | Get details about a specific user.
*UsersApi* | [**users_setlists_create**](docs/UsersApi.md#users_setlists_create) | **POST** /api/v3/users/{user_token}/setlists/ | Add a new Set List.
*UsersApi* | [**users_setlists_delete**](docs/UsersApi.md#users_setlists_delete) | **DELETE** /api/v3/users/{user_token}/setlists/{list_id}/ | Delete a Set List and all it&#39;s Sets.
*UsersApi* | [**users_setlists_list**](docs/UsersApi.md#users_setlists_list) | **GET** /api/v3/users/{user_token}/setlists/ | Get a list of all the user&#39;s Set Lists.
*UsersApi* | [**users_setlists_partial_update**](docs/UsersApi.md#users_setlists_partial_update) | **PATCH** /api/v3/users/{user_token}/setlists/{list_id}/ | Update an existing Set List&#39;s details.
*UsersApi* | [**users_setlists_read**](docs/UsersApi.md#users_setlists_read) | **GET** /api/v3/users/{user_token}/setlists/{list_id}/ | Get details about a specific Set List.
*UsersApi* | [**users_setlists_sets_create**](docs/UsersApi.md#users_setlists_sets_create) | **POST** /api/v3/users/{user_token}/setlists/{list_id}/sets/ | Add one or more Sets to the Set List. Existing Sets are unaffected.
*UsersApi* | [**users_setlists_sets_delete**](docs/UsersApi.md#users_setlists_sets_delete) | **DELETE** /api/v3/users/{user_token}/setlists/{list_id}/sets/{set_num}/ | Delete a Set from the Set List.
*UsersApi* | [**users_setlists_sets_list**](docs/UsersApi.md#users_setlists_sets_list) | **GET** /api/v3/users/{user_token}/setlists/{list_id}/sets/ | Get a list of all the Sets in a specific Set List.
*UsersApi* | [**users_setlists_sets_partial_update**](docs/UsersApi.md#users_setlists_sets_partial_update) | **PATCH** /api/v3/users/{user_token}/setlists/{list_id}/sets/{set_num}/ | Update an existing Set&#39;s details in the Set List.
*UsersApi* | [**users_setlists_sets_read**](docs/UsersApi.md#users_setlists_sets_read) | **GET** /api/v3/users/{user_token}/setlists/{list_id}/sets/{set_num}/ | Get details about a specific Set in the Set List.
*UsersApi* | [**users_setlists_sets_update**](docs/UsersApi.md#users_setlists_sets_update) | **PUT** /api/v3/users/{user_token}/setlists/{list_id}/sets/{set_num}/ | Replace an existing Set&#39;s details in the Set List.
*UsersApi* | [**users_setlists_update**](docs/UsersApi.md#users_setlists_update) | **PUT** /api/v3/users/{user_token}/setlists/{list_id}/ | Replace an existing Set List&#39;s details.
*UsersApi* | [**users_sets_create**](docs/UsersApi.md#users_sets_create) | **POST** /api/v3/users/{user_token}/sets/ | Add one or more Sets to the user&#39;s LEGO collection. Existing Sets are unaffected.
*UsersApi* | [**users_sets_delete**](docs/UsersApi.md#users_sets_delete) | **DELETE** /api/v3/users/{user_token}/sets/{set_num}/ | Delete the Set from all the user&#39;s Set Lists.
*UsersApi* | [**users_sets_list**](docs/UsersApi.md#users_sets_list) | **GET** /api/v3/users/{user_token}/sets/ | Get a list of all the Sets in the user&#39;s LEGO collection.
*UsersApi* | [**users_sets_read**](docs/UsersApi.md#users_sets_read) | **GET** /api/v3/users/{user_token}/sets/{set_num}/ | Get details about a specific Set in the user&#39;s LEGO collection.
*UsersApi* | [**users_sets_sync_create**](docs/UsersApi.md#users_sets_sync_create) | **POST** /api/v3/users/{user_token}/sets/sync/ | Synchronise a user&#39;s Sets to the POSTed list.
*UsersApi* | [**users_sets_update**](docs/UsersApi.md#users_sets_update) | **PUT** /api/v3/users/{user_token}/sets/{set_num}/ | Update an existing Set&#39;s quantity in all Set Lists. This PUT call is different to others in that it will create
*UsersApi* | [**users_token_create**](docs/UsersApi.md#users_token_create) | **POST** /api/v3/users/_token/ | Generate a User Token to be used for authorising user account actions in subsequent calls. Username can be either


## Documentation For Models



## Documentation For Authorization

 All endpoints do not require authorization.


## Author

Matthieu Berthomé (rienafairefr)

