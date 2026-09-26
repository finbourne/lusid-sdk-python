# WritebackConfiguration

Base class for the configuration of a writeback a matching ruleset generates suggestions for against its  results. Polymorphic by WritebackType; each supported type has a corresponding inherited class.
## Example

```python
from lusid.models.writeback_configuration import WritebackConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

# Example with WritebackConfiguration 

settle_expected_activity_writeback_configuration_instance = lusid.models.settle_expected_activity_writeback_configuration.SettleExpectedActivityWritebackConfiguration(
                        mandatory_rule_names = lusid.models.settle_expected_activity_rule_names.SettleExpectedActivityRuleNames(
                            activity_type = '', 
                            activity_date = '', 
                            units = '', ), 
                        result_patterns = [
                            lusid.models.writeback_result_pattern.WritebackResultPattern(
                                units_difference = '', 
                                result_cardinality = '', 
                                use_target_units = True, )
                            ], 
                        writeback_type = '', 
                        target_side = '', )

writeback_configuration_instance = WritebackConfiguration(settle_expected_activity_writeback_configuration_instance)

```
See all compatible oneOf types with WritebackConfiguration


[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

