# SweepBlocksRequest

A request to sweep specified blocks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_ids** | [**Dict[str, ResourceId]**](ResourceId.md) | A dictionary mapping ephemeral identifiers, which live as long as the request, to specific blocks to sweep. | 
**latest_allowable_modification_time** | **str** | Timestamp or cut label which the  block or related entities must not have been updated after. | 

## Example

```python
from lusid.models.sweep_blocks_request import SweepBlocksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SweepBlocksRequest from a JSON string
sweep_blocks_request_instance = SweepBlocksRequest.from_json(json)
# print the JSON string representation of the object
print SweepBlocksRequest.to_json()

# convert the object into a dict
sweep_blocks_request_dict = sweep_blocks_request_instance.to_dict()
# create an instance of SweepBlocksRequest from a dict
sweep_blocks_request_form_dict = sweep_blocks_request.from_dict(sweep_blocks_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


