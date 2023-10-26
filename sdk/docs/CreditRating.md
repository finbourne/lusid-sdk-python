# CreditRating

Object describing a credit rating,  which assesses the stability and credit worthiness of a legal entity  and hence its likelihood of defaulting on its outstanding obligations (typically debt).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating_source** | **str** | The provider of the credit rating, which will typically be an agency such as Moody&#39;s or Standard and Poor. | 
**rating** | **str** | The credit rating provided by the rating source. This would expected to be consistent with the rating scheme of that agency/source. | 

## Example

```python
from lusid.models.credit_rating import CreditRating

# TODO update the JSON string below
json = "{}"
# create an instance of CreditRating from a JSON string
credit_rating_instance = CreditRating.from_json(json)
# print the JSON string representation of the object
print CreditRating.to_json()

# convert the object into a dict
credit_rating_dict = credit_rating_instance.to_dict()
# create an instance of CreditRating from a dict
credit_rating_form_dict = credit_rating.from_dict(credit_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


