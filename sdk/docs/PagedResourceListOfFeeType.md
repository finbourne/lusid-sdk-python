# PagedResourceListOfFeeType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[FeeType]**](FeeType.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_fee_type import PagedResourceListOfFeeType

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfFeeType from a JSON string
paged_resource_list_of_fee_type_instance = PagedResourceListOfFeeType.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfFeeType.to_json()

# convert the object into a dict
paged_resource_list_of_fee_type_dict = paged_resource_list_of_fee_type_instance.to_dict()
# create an instance of PagedResourceListOfFeeType from a dict
paged_resource_list_of_fee_type_form_dict = paged_resource_list_of_fee_type.from_dict(paged_resource_list_of_fee_type_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


