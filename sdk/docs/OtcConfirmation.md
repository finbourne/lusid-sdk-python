# OtcConfirmation

For the storage of any information pertinent to the confirmation of an OTC trade. e.g the Counterparty Agreement Code

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_agreement_id** | [**ResourceId**](ResourceId.md) |  | [optional] 

## Example

```python
from lusid.models.otc_confirmation import OtcConfirmation

# TODO update the JSON string below
json = "{}"
# create an instance of OtcConfirmation from a JSON string
otc_confirmation_instance = OtcConfirmation.from_json(json)
# print the JSON string representation of the object
print OtcConfirmation.to_json()

# convert the object into a dict
otc_confirmation_dict = otc_confirmation_instance.to_dict()
# create an instance of OtcConfirmation from a dict
otc_confirmation_form_dict = otc_confirmation.from_dict(otc_confirmation_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


