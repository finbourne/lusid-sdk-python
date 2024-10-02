# HoldingIdsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_ids** | **List[int]** | The array of unique holding identifiers | 

## Example

```python
from lusid.models.holding_ids_request import HoldingIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HoldingIdsRequest from a JSON string
holding_ids_request_instance = HoldingIdsRequest.from_json(json)
# print the JSON string representation of the object
print HoldingIdsRequest.to_json()

# convert the object into a dict
holding_ids_request_dict = holding_ids_request_instance.to_dict()
# create an instance of HoldingIdsRequest from a dict
holding_ids_request_form_dict = holding_ids_request.from_dict(holding_ids_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


