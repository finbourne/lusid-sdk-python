# FundDetails

The details of a Fund.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency of the fund which is the same as the base currency of all the portfolios of the fund&#39;s Abor. | [optional] 

## Example

```python
from lusid.models.fund_details import FundDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FundDetails from a JSON string
fund_details_instance = FundDetails.from_json(json)
# print the JSON string representation of the object
print FundDetails.to_json()

# convert the object into a dict
fund_details_dict = fund_details_instance.to_dict()
# create an instance of FundDetails from a dict
fund_details_form_dict = fund_details.from_dict(fund_details_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


