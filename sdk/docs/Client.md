# Client


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 

## Example

```python
from lusid.models.client import Client

# TODO update the JSON string below
json = "{}"
# create an instance of Client from a JSON string
client_instance = Client.from_json(json)
# print the JSON string representation of the object
print Client.to_json()

# convert the object into a dict
client_dict = client_instance.to_dict()
# create an instance of Client from a dict
client_form_dict = client.from_dict(client_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


