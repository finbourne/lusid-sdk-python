# AdjustHolding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Contains warnings related to unresolved instruments | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.adjust_holding import AdjustHolding

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustHolding from a JSON string
adjust_holding_instance = AdjustHolding.from_json(json)
# print the JSON string representation of the object
print AdjustHolding.to_json()

# convert the object into a dict
adjust_holding_dict = adjust_holding_instance.to_dict()
# create an instance of AdjustHolding from a dict
adjust_holding_form_dict = adjust_holding.from_dict(adjust_holding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


