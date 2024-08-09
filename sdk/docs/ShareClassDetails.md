# ShareClassDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_instrument_id** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the share class&#39; instrument identifiers | [optional] 
**instrument_scope** | **str** | The scope in which the share class instrument lies. | [optional] 
**dom_currency** | **str** | The domestic currency of the share class instrument | [optional] 
**instrument_active** | **bool** | If the instrument of the share class is active. | [optional] 

## Example

```python
from lusid.models.share_class_details import ShareClassDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ShareClassDetails from a JSON string
share_class_details_instance = ShareClassDetails.from_json(json)
# print the JSON string representation of the object
print ShareClassDetails.to_json()

# convert the object into a dict
share_class_details_dict = share_class_details_instance.to_dict()
# create an instance of ShareClassDetails from a dict
share_class_details_form_dict = share_class_details.from_dict(share_class_details_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


