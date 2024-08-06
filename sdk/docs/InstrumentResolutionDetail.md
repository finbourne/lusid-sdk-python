# InstrumentResolutionDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, str]** | Unique instrument identifiers | 
**lusid_instrument_id** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers | [optional] [readonly] 
**instrument_scope** | **str** | The scope in which the instrument lies. | [optional] [readonly] 

## Example

```python
from lusid.models.instrument_resolution_detail import InstrumentResolutionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentResolutionDetail from a JSON string
instrument_resolution_detail_instance = InstrumentResolutionDetail.from_json(json)
# print the JSON string representation of the object
print InstrumentResolutionDetail.to_json()

# convert the object into a dict
instrument_resolution_detail_dict = instrument_resolution_detail_instance.to_dict()
# create an instance of InstrumentResolutionDetail from a dict
instrument_resolution_detail_form_dict = instrument_resolution_detail.from_dict(instrument_resolution_detail_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


