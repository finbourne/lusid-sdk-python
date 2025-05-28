# ResourceListOfInvestorRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[InvestorRecord]**](InvestorRecord.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_investor_record import ResourceListOfInvestorRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfInvestorRecord from a JSON string
resource_list_of_investor_record_instance = ResourceListOfInvestorRecord.from_json(json)
# print the JSON string representation of the object
print ResourceListOfInvestorRecord.to_json()

# convert the object into a dict
resource_list_of_investor_record_dict = resource_list_of_investor_record_instance.to_dict()
# create an instance of ResourceListOfInvestorRecord from a dict
resource_list_of_investor_record_form_dict = resource_list_of_investor_record.from_dict(resource_list_of_investor_record_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


