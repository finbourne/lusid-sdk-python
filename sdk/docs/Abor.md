# Abor

An Abor entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Abor. | [optional] 
**description** | **str** | The description for the Abor. | [optional] 
**portfolio_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The list with the portfolio ids which are part of the Abor. | 
**abor_configuration_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Abor. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.abor import Abor

# TODO update the JSON string below
json = "{}"
# create an instance of Abor from a JSON string
abor_instance = Abor.from_json(json)
# print the JSON string representation of the object
print Abor.to_json()

# convert the object into a dict
abor_dict = abor_instance.to_dict()
# create an instance of Abor from a dict
abor_form_dict = abor.from_dict(abor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


