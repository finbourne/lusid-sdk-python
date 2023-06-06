# DataMapping

When importing data from an external source there are essentially three levels of interaction with LUSID.  (1) The data is a raw document that LUSID does not understand. You can store and retrieve it but it does not full interact with other documents inside LUSID  (2) The data has a map from fields and paths to 'properties' in LUSID. In essence, LUSID can then treat the data as weakly typed (decimal, string) data that can be returned through queries      and where various aggregation requests will then work.  (3) The data is fully translatable into LUSID and understood, in some sense, natively. This means that it can be used for context sensitive calculations such as pricing or risk calculations.  The data map object is designed to allow data to transition from step 1 to 2 and in some cases as an alternative for step 2 to 3.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_definitions** | [**List[DataDefinition]**](DataDefinition.md) | A map from LUSID item keys to data definitions that define the names, types and degree of uniqueness of data provided to LUSID in structured data stores. | [optional] 

## Example

```python
from lusid.models.data_mapping import DataMapping

# TODO update the JSON string below
json = "{}"
# create an instance of DataMapping from a JSON string
data_mapping_instance = DataMapping.from_json(json)
# print the JSON string representation of the object
print DataMapping.to_json()

# convert the object into a dict
data_mapping_dict = data_mapping_instance.to_dict()
# create an instance of DataMapping from a dict
data_mapping_form_dict = data_mapping.from_dict(data_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


