# InvestorRecord

Representation of an Investor Record on the LUSID API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_investor_record_id** | **str** | The unique LUSID Investor Record Identifier of the Investor Record. | [optional] 
**display_name** | **str** | The display name of the Investor Record | [optional] 
**description** | **str** | The description of the Investor Record | [optional] 
**investor** | [**Investor**](Investor.md) |  | [optional] 
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Unique client-defined identifiers of the Investor Record. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Investor Record. | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the Investor Record. | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.investor_record import InvestorRecord

# TODO update the JSON string below
json = "{}"
# create an instance of InvestorRecord from a JSON string
investor_record_instance = InvestorRecord.from_json(json)
# print the JSON string representation of the object
print InvestorRecord.to_json()

# convert the object into a dict
investor_record_dict = investor_record_instance.to_dict()
# create an instance of InvestorRecord from a dict
investor_record_form_dict = investor_record.from_dict(investor_record_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


