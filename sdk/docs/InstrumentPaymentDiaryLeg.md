# InstrumentPaymentDiaryLeg

A leg containing a set of cashflows.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leg_id** | **str** | Identifier for the leg of a payment diary. | [optional] 
**rows** | [**List[InstrumentPaymentDiaryRow]**](InstrumentPaymentDiaryRow.md) | List of individual cashflows within the payment diary. | [optional] 

## Example

```python
from lusid.models.instrument_payment_diary_leg import InstrumentPaymentDiaryLeg

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentPaymentDiaryLeg from a JSON string
instrument_payment_diary_leg_instance = InstrumentPaymentDiaryLeg.from_json(json)
# print the JSON string representation of the object
print InstrumentPaymentDiaryLeg.to_json()

# convert the object into a dict
instrument_payment_diary_leg_dict = instrument_payment_diary_leg_instance.to_dict()
# create an instance of InstrumentPaymentDiaryLeg from a dict
instrument_payment_diary_leg_form_dict = instrument_payment_diary_leg.from_dict(instrument_payment_diary_leg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


