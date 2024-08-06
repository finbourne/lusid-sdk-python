# UpdateInstrumentIdentifierRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The allowable instrument identifier to update, insert or remove e.g. &#39;Figi&#39;. | 
**value** | **str** | The new value of the allowable instrument identifier. If unspecified the identifier will be removed from the instrument. | [optional] 
**effective_at** | **str** | The effective datetime from which the identifier should be updated, inserted or removed. Defaults to the current LUSID system datetime if not specified. | [optional] 

## Example

```python
from lusid.models.update_instrument_identifier_request import UpdateInstrumentIdentifierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInstrumentIdentifierRequest from a JSON string
update_instrument_identifier_request_instance = UpdateInstrumentIdentifierRequest.from_json(json)
# print the JSON string representation of the object
print UpdateInstrumentIdentifierRequest.to_json()

# convert the object into a dict
update_instrument_identifier_request_dict = update_instrument_identifier_request_instance.to_dict()
# create an instance of UpdateInstrumentIdentifierRequest from a dict
update_instrument_identifier_request_form_dict = update_instrument_identifier_request.from_dict(update_instrument_identifier_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


