# ResourceListOfReconciliationBreak


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ReconciliationBreak]**](ReconciliationBreak.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_reconciliation_break import ResourceListOfReconciliationBreak

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfReconciliationBreak from a JSON string
resource_list_of_reconciliation_break_instance = ResourceListOfReconciliationBreak.from_json(json)
# print the JSON string representation of the object
print ResourceListOfReconciliationBreak.to_json()

# convert the object into a dict
resource_list_of_reconciliation_break_dict = resource_list_of_reconciliation_break_instance.to_dict()
# create an instance of ResourceListOfReconciliationBreak from a dict
resource_list_of_reconciliation_break_form_dict = resource_list_of_reconciliation_break.from_dict(resource_list_of_reconciliation_break_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


