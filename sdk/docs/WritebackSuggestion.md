# WritebackSuggestion

A writeback suggested against a target-side item of a rec result. Polymorphic by WritebackType; each  supported type has a corresponding inherited class carrying the upsertable request it proposes.
## Example

```python
from lusid.models.writeback_suggestion import WritebackSuggestion
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

# Example with WritebackSuggestion 

settle_expected_activity_writeback_suggestion_instance = lusid.models.settle_expected_activity_writeback_suggestion.SettleExpectedActivityWritebackSuggestion(
                        result_pattern = lusid.models.writeback_result_pattern.WritebackResultPattern(
                            units_difference = '', 
                            result_cardinality = '', 
                            use_target_units = True, ), 
                        portfolio_id = lusid.models.resource_id.ResourceId(
                            scope = '', 
                            code = '', ), 
                        settlement_instruction_request = lusid.models.settlement_instruction_request.SettlementInstructionRequest(
                            settlement_instruction_id = '', 
                            transaction_id = '', 
                            settlement_category = '', 
                            instruction_type = '', 
                            instrument_identifiers = {
                                'key' : ''
                                }, 
                            contractual_settlement_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            actual_settlement_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            units = 1.337, 
                            sub_holding_key_overrides = {
                                'key' : lusid.models.perpetual_property.PerpetualProperty(
                                    key = '', 
                                    value = lusid.models.property_value.PropertyValue(
                                        label_value = '', 
                                        metric_value = lusid.models.metric_value.MetricValue(
                                            unit = '', ), 
                                        label_value_set = lusid.models.label_value_set.LabelValueSet(
                                            values = [
                                                ''
                                                ], ), ), 
                                    reference_data = {
                                        'key' : lusid.models.property_reference_data_value.PropertyReferenceDataValue(
                                            string_value = '', 
                                            numeric_value = 1.337, )
                                        }, )
                                }, 
                            custodian_account_override = lusid.models.resource_id.ResourceId(
                                scope = '', 
                                code = '', ), 
                            instruction_to_portfolio_rate = 1.337, 
                            settlement_in_lieu = lusid.models.settlement_in_lieu.SettlementInLieu(
                                original_settlement_currency = '', 
                                amount = 1.337, ), 
                            properties = [
                                lusid.models.perpetual_property.PerpetualProperty(
                                    key = '', )
                                ], ), 
                        writeback_type = '', )

writeback_suggestion_instance = WritebackSuggestion(settle_expected_activity_writeback_suggestion_instance)

```
See all compatible oneOf types with WritebackSuggestion


[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

