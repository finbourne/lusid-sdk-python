# IndexConvention

A set of conventions that describe the conventions for calculation of payments made on rates interbank lending and similar.  Based on ISDA 2006 conventions and similar documentation. Please see the knowledge base for further documentation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixing_reference** | **str** | The reference rate name for fixings. | 
**publication_day_lag** | **int** | Number of days between spot and publication of the rate. | 
**payment_tenor** | **str** | The tenor of the payment. For an OIS index this is always 1 day. For other indices, e.g. LIBOR it will have a variable tenor typically between 1 day and 1 year.    For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097) | 
**day_count_convention** | **str** | when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them.  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365]. | 
**currency** | **str** | Currency of the index convention. | 
**index_name** | **str** | The name of the index for which this represents the conventions of.  For instance, \&quot;SOFR\&quot;, \&quot;LIBOR\&quot;, \&quot;EURIBOR\&quot;, etc.  Defaults to \&quot;INDEX\&quot; if not specified. | [optional] 
**scope** | **str** | The scope used when updating or inserting the convention. | [optional] 
**code** | **str** | The code of the convention. | [optional] 

## Example

```python
from lusid.models.index_convention import IndexConvention

# TODO update the JSON string below
json = "{}"
# create an instance of IndexConvention from a JSON string
index_convention_instance = IndexConvention.from_json(json)
# print the JSON string representation of the object
print IndexConvention.to_json()

# convert the object into a dict
index_convention_dict = index_convention_instance.to_dict()
# create an instance of IndexConvention from a dict
index_convention_form_dict = index_convention.from_dict(index_convention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


