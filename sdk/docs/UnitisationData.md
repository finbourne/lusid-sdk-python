# UnitisationData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares_in_issue** | **float** | The number of shares in issue at a valuation point. | 
**unit_price** | **float** | The price of one unit of the share class at a valuation point. | 
**net_dealing_units** | **float** | The net dealing in units for the share class at a valuation point. This could be the sum of negative redemptions (in units) and positive subscriptions (in units). | 

## Example

```python
from lusid.models.unitisation_data import UnitisationData

# TODO update the JSON string below
json = "{}"
# create an instance of UnitisationData from a JSON string
unitisation_data_instance = UnitisationData.from_json(json)
# print the JSON string representation of the object
print UnitisationData.to_json()

# convert the object into a dict
unitisation_data_dict = unitisation_data_instance.to_dict()
# create an instance of UnitisationData from a dict
unitisation_data_form_dict = unitisation_data.from_dict(unitisation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


