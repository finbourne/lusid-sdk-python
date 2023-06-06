# BasketIdentifier

Descriptive information that describes a particular basket of instruments. Most commonly required with a CDS Index or similarly defined instrument.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** | Index set, e.g. iTraxx or CDX. | 
**name** | **str** | The index name within the set, e.g. \&quot;MAIN\&quot; or \&quot;Crossover\&quot;. | 
**region** | **str** | Applicable geographic country or region. Typically something like \&quot;Europe\&quot;, \&quot;Asia ex-Japan\&quot;, \&quot;Japan\&quot; or \&quot;Australia\&quot;. | 
**series_id** | **int** | The series identifier. | 

## Example

```python
from lusid.models.basket_identifier import BasketIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of BasketIdentifier from a JSON string
basket_identifier_instance = BasketIdentifier.from_json(json)
# print the JSON string representation of the object
print BasketIdentifier.to_json()

# convert the object into a dict
basket_identifier_dict = basket_identifier_instance.to_dict()
# create an instance of BasketIdentifier from a dict
basket_identifier_form_dict = basket_identifier.from_dict(basket_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


