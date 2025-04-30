# Investor

Inner dto of an Investor Record on the LUSID API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_type** | **str** | The type of the Investor | [optional] 
**investor_identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The identifiers of the Investor | [optional] 
**entity_unique_id** | **str** | The unique Investor entity identifier | [optional] 
**person** | [**Person**](Person.md) |  | [optional] 
**legal_entity** | [**LegalEntity**](LegalEntity.md) |  | [optional] 

## Example

```python
from lusid.models.investor import Investor

# TODO update the JSON string below
json = "{}"
# create an instance of Investor from a JSON string
investor_instance = Investor.from_json(json)
# print the JSON string representation of the object
print Investor.to_json()

# convert the object into a dict
investor_dict = investor_instance.to_dict()
# create an instance of Investor from a dict
investor_form_dict = investor.from_dict(investor_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


