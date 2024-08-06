# LegalEntity

Representation of Legal Entity on LUSID API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the Legal Entity | [optional] 
**description** | **str** | The description of the Legal Entity | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**lusid_legal_entity_id** | **str** | The unique LUSID Legal Entity Identifier of the Legal Entity. | [optional] 
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Unique client-defined identifiers of the Legal Entity. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Legal Entity. | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the Legal Entity. | [optional] 
**counterparty_risk_information** | [**CounterpartyRiskInformation**](CounterpartyRiskInformation.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.legal_entity import LegalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LegalEntity from a JSON string
legal_entity_instance = LegalEntity.from_json(json)
# print the JSON string representation of the object
print LegalEntity.to_json()

# convert the object into a dict
legal_entity_dict = legal_entity_instance.to_dict()
# create an instance of LegalEntity from a dict
legal_entity_form_dict = legal_entity.from_dict(legal_entity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


