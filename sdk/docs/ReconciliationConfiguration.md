# ReconciliationConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**ReconciliationSideConfiguration**](ReconciliationSideConfiguration.md) |  | [optional] 
**right** | [**ReconciliationSideConfiguration**](ReconciliationSideConfiguration.md) |  | [optional] 
**mapping_id** | [**ResourceId**](ResourceId.md) |  | [optional] 

## Example

```python
from lusid.models.reconciliation_configuration import ReconciliationConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationConfiguration from a JSON string
reconciliation_configuration_instance = ReconciliationConfiguration.from_json(json)
# print the JSON string representation of the object
print ReconciliationConfiguration.to_json()

# convert the object into a dict
reconciliation_configuration_dict = reconciliation_configuration_instance.to_dict()
# create an instance of ReconciliationConfiguration from a dict
reconciliation_configuration_form_dict = reconciliation_configuration.from_dict(reconciliation_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


