# ConstituentsAdjustmentHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | There can be at most one holdings adjustment for a portfolio at a  specific effective time so this uniquely identifies the adjustment. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.constituents_adjustment_header import ConstituentsAdjustmentHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ConstituentsAdjustmentHeader from a JSON string
constituents_adjustment_header_instance = ConstituentsAdjustmentHeader.from_json(json)
# print the JSON string representation of the object
print ConstituentsAdjustmentHeader.to_json()

# convert the object into a dict
constituents_adjustment_header_dict = constituents_adjustment_header_instance.to_dict()
# create an instance of ConstituentsAdjustmentHeader from a dict
constituents_adjustment_header_form_dict = constituents_adjustment_header.from_dict(constituents_adjustment_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


