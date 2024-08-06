# InstrumentPaymentDiary

A payment diary containing all the cashflows on a single instrument.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id_type** | **str** | The identifier type of the instrument. | [optional] 
**instrument_id** | **str** | The identifier for the instrument. | [optional] 
**instrument_scope** | **str** | The scope of the instrument. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**legs** | [**List[InstrumentPaymentDiaryLeg]**](InstrumentPaymentDiaryLeg.md) | Aggregated sets of Cashflows. | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.instrument_payment_diary import InstrumentPaymentDiary

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentPaymentDiary from a JSON string
instrument_payment_diary_instance = InstrumentPaymentDiary.from_json(json)
# print the JSON string representation of the object
print InstrumentPaymentDiary.to_json()

# convert the object into a dict
instrument_payment_diary_dict = instrument_payment_diary_instance.to_dict()
# create an instance of InstrumentPaymentDiary from a dict
instrument_payment_diary_form_dict = instrument_payment_diary.from_dict(instrument_payment_diary_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


