# UpsertFlowConventionsRequest

Flow conventions that is to be stored in the convention data store.  Only one of these must be present.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_flow_conventions_request import UpsertFlowConventionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertFlowConventionsRequest from a JSON string
upsert_flow_conventions_request_instance = UpsertFlowConventionsRequest.from_json(json)
# print the JSON string representation of the object
print UpsertFlowConventionsRequest.to_json()

# convert the object into a dict
upsert_flow_conventions_request_dict = upsert_flow_conventions_request_instance.to_dict()
# create an instance of UpsertFlowConventionsRequest from a dict
upsert_flow_conventions_request_form_dict = upsert_flow_conventions_request.from_dict(upsert_flow_conventions_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


