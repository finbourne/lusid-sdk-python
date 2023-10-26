# LusidUniqueId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type for the LUSID unique id, this will depend on the type of entity found, for instance &#39;Instrument&#39; would have a value of &#39;LusidInstrumentId&#39; | 
**value** | **str** | The value for the LUSID unique id | 

## Example

```python
from lusid.models.lusid_unique_id import LusidUniqueId

# TODO update the JSON string below
json = "{}"
# create an instance of LusidUniqueId from a JSON string
lusid_unique_id_instance = LusidUniqueId.from_json(json)
# print the JSON string representation of the object
print LusidUniqueId.to_json()

# convert the object into a dict
lusid_unique_id_dict = lusid_unique_id_instance.to_dict()
# create an instance of LusidUniqueId from a dict
lusid_unique_id_form_dict = lusid_unique_id.from_dict(lusid_unique_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


