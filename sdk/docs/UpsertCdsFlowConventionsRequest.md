# UpsertCdsFlowConventionsRequest

CDS Flow convention that is to be stored in the convention data store.  Only one of these must be present.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cds_flow_conventions** | [**CdsFlowConventions**](CdsFlowConventions.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_cds_flow_conventions_request import UpsertCdsFlowConventionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCdsFlowConventionsRequest from a JSON string
upsert_cds_flow_conventions_request_instance = UpsertCdsFlowConventionsRequest.from_json(json)
# print the JSON string representation of the object
print UpsertCdsFlowConventionsRequest.to_json()

# convert the object into a dict
upsert_cds_flow_conventions_request_dict = upsert_cds_flow_conventions_request_instance.to_dict()
# create an instance of UpsertCdsFlowConventionsRequest from a dict
upsert_cds_flow_conventions_request_form_dict = upsert_cds_flow_conventions_request.from_dict(upsert_cds_flow_conventions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


