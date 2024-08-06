# FeeType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | The name of the fee type. | 
**description** | **str** | The description of the fee type. | 
**component_transactions** | [**List[ComponentTransaction]**](ComponentTransaction.md) | A set of component transactions that relate to the fee type. | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.fee_type import FeeType

# TODO update the JSON string below
json = "{}"
# create an instance of FeeType from a JSON string
fee_type_instance = FeeType.from_json(json)
# print the JSON string representation of the object
print FeeType.to_json()

# convert the object into a dict
fee_type_dict = fee_type_instance.to_dict()
# create an instance of FeeType from a dict
fee_type_form_dict = fee_type.from_dict(fee_type_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


