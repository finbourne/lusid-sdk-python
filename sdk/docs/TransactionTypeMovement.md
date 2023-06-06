# TransactionTypeMovement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movement_types** | **str** | Movement types determine the impact of the movement on the holdings | 
**side** | **str** | The Side determines which of the fields from our transaction are used to generate the Movement. Side1 means the &#39;security&#39; side of the transaction, ie the Instrument and Units; Side2 means the &#39;cash&#39; side, ie the Total Consideration | 
**direction** | **int** |  A multiplier to apply to Transaction amounts; the values are -1 to indicate to reverse the signs and 1 to indicate to use the signed values from the Transaction directly. For a typical Transaction with unsigned values, 1 means increase, -1 means decrease | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The properties associated with the underlying Movement | [optional] 
**mappings** | [**List[TransactionTypePropertyMapping]**](TransactionTypePropertyMapping.md) | This allows you to map a transaction property to a property on the underlying holding | [optional] 
**name** | **str** | The movement name (optional) | [optional] 
**movement_options** | **List[str]** | Allows extra specifications for the movement. The only option currently available is &#39;DirectAdjustment&#39;. A movement type of &#39;StockMovement&#39; with an option of &#39;DirectAdjusment&#39; will allow you to adjust the unitsof a holding without affecting its cost base. You will, therefore, be able to reflect the impact of a stock split by loading a Transaction. | [optional] 

## Example

```python
from lusid.models.transaction_type_movement import TransactionTypeMovement

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTypeMovement from a JSON string
transaction_type_movement_instance = TransactionTypeMovement.from_json(json)
# print the JSON string representation of the object
print TransactionTypeMovement.to_json()

# convert the object into a dict
transaction_type_movement_dict = transaction_type_movement_instance.to_dict()
# create an instance of TransactionTypeMovement from a dict
transaction_type_movement_form_dict = transaction_type_movement.from_dict(transaction_type_movement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


