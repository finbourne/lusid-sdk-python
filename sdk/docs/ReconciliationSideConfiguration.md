# ReconciliationSideConfiguration

Specification for one side of a valuations/positions scheduled reconciliation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**effective_at** | **datetime** |  | [optional] 
**as_at** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from lusid.models.reconciliation_side_configuration import ReconciliationSideConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationSideConfiguration from a JSON string
reconciliation_side_configuration_instance = ReconciliationSideConfiguration.from_json(json)
# print the JSON string representation of the object
print ReconciliationSideConfiguration.to_json()

# convert the object into a dict
reconciliation_side_configuration_dict = reconciliation_side_configuration_instance.to_dict()
# create an instance of ReconciliationSideConfiguration from a dict
reconciliation_side_configuration_form_dict = reconciliation_side_configuration.from_dict(reconciliation_side_configuration_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


