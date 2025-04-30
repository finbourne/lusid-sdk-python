# UpsertInvestorRecordsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, InvestorRecord]**](InvestorRecord.md) | The investor records which have been successfully updated or created. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The investor records that could not be updated or created or were left unchanged without error along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_investor_records_response import UpsertInvestorRecordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertInvestorRecordsResponse from a JSON string
upsert_investor_records_response_instance = UpsertInvestorRecordsResponse.from_json(json)
# print the JSON string representation of the object
print UpsertInvestorRecordsResponse.to_json()

# convert the object into a dict
upsert_investor_records_response_dict = upsert_investor_records_response_instance.to_dict()
# create an instance of UpsertInvestorRecordsResponse from a dict
upsert_investor_records_response_form_dict = upsert_investor_records_response.from_dict(upsert_investor_records_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


