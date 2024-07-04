# UpsertInstrumentsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, Instrument]**](Instrument.md) | The instruments which have been successfully updated or created. | [optional] 
**staged** | [**Dict[str, Instrument]**](Instrument.md) | The instruments that have been staged for updation or creation. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The instruments that could not be updated or created or were left unchanged without error along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Meta data associated with the upsert event. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_instruments_response import UpsertInstrumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertInstrumentsResponse from a JSON string
upsert_instruments_response_instance = UpsertInstrumentsResponse.from_json(json)
# print the JSON string representation of the object
print UpsertInstrumentsResponse.to_json()

# convert the object into a dict
upsert_instruments_response_dict = upsert_instruments_response_instance.to_dict()
# create an instance of UpsertInstrumentsResponse from a dict
upsert_instruments_response_form_dict = upsert_instruments_response.from_dict(upsert_instruments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


