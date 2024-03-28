# SetShareClassInstrumentsRequest

The request used to create a Fund.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_class_instrument_scopes** | **List[str]** | The scopes in which the instruments lie, currently limited to one. | 
**share_class_instruments** | [**List[InstrumentResolutionDetail]**](InstrumentResolutionDetail.md) | Details the user-provided instrument identifiers and the instrument resolved from them. | 

## Example

```python
from lusid.models.set_share_class_instruments_request import SetShareClassInstrumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetShareClassInstrumentsRequest from a JSON string
set_share_class_instruments_request_instance = SetShareClassInstrumentsRequest.from_json(json)
# print the JSON string representation of the object
print SetShareClassInstrumentsRequest.to_json()

# convert the object into a dict
set_share_class_instruments_request_dict = set_share_class_instruments_request_instance.to_dict()
# create an instance of SetShareClassInstrumentsRequest from a dict
set_share_class_instruments_request_form_dict = set_share_class_instruments_request.from_dict(set_share_class_instruments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


