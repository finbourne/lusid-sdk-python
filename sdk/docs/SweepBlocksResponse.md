# SweepBlocksResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, ResourceId]**](ResourceId.md) | The identifiers of blocks which have been successfully swept, indexed by ephemeral request-lived id. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The identifiers of blocks that could not be swept, along with a reason for their failure. | [optional] 

## Example

```python
from lusid.models.sweep_blocks_response import SweepBlocksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SweepBlocksResponse from a JSON string
sweep_blocks_response_instance = SweepBlocksResponse.from_json(json)
# print the JSON string representation of the object
print SweepBlocksResponse.to_json()

# convert the object into a dict
sweep_blocks_response_dict = sweep_blocks_response_instance.to_dict()
# create an instance of SweepBlocksResponse from a dict
sweep_blocks_response_form_dict = sweep_blocks_response.from_dict(sweep_blocks_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


