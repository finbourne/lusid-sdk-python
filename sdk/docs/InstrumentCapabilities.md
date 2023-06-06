# InstrumentCapabilities

Instrument capabilities containing useful information about the instrument and the model. This includes  - features corresponding to the instrument i.e. Optionality:American, Other:InflationLinked  - supported addresses (if model provided) i.e. Valuation/Pv, Valuation/DirtyPriceKey, Valuation/Accrued  - economic dependencies (if model provided) i.e. Cash:USD, Fx:GBP.USD, Rates:GBP.GBPOIS

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** | The Lusid instrument id for the instrument e.g. &#39;LUID_00003D4X&#39;. | [optional] 
**model** | **str** | The pricing model e.g. &#39;Discounting&#39;. | [optional] 
**features** | **Dict[str, str]** | Features of the instrument describing its optionality, payoff type and more e.g. &#39;Instrument/Features/Exercise: American&#39;, &#39;Instrument/Features/Product: Option&#39; | [optional] 
**supported_addresses** | [**List[DescribedAddressKey]**](DescribedAddressKey.md) | Queryable addresses supported by the model, e.g. &#39;Valuation/Pv&#39;, &#39;Valuation/Accrued&#39;. | [optional] 
**economic_dependencies** | [**List[EconomicDependency]**](EconomicDependency.md) | Economic dependencies for the model, e.g. &#39;Fx:GBP.USD&#39;, &#39;Cash:GBP&#39;, &#39;Rates:GBP.GBPOIS&#39;. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.instrument_capabilities import InstrumentCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentCapabilities from a JSON string
instrument_capabilities_instance = InstrumentCapabilities.from_json(json)
# print the JSON string representation of the object
print InstrumentCapabilities.to_json()

# convert the object into a dict
instrument_capabilities_dict = instrument_capabilities_instance.to_dict()
# create an instance of InstrumentCapabilities from a dict
instrument_capabilities_form_dict = instrument_capabilities.from_dict(instrument_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


