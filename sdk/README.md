<a id="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://fbn-prd.lusid.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AborApi* | [**add_diary_entry**](docs/AborApi.md#add_diary_entry) | **POST** /api/abor/{scope}/{code}/accountingdiary | [EXPERIMENTAL] AddDiaryEntry: Add a diary entry to the specified Abor. This would be type 'Other'.
*AborApi* | [**close_period**](docs/AborApi.md#close_period) | **POST** /api/abor/{scope}/{code}/accountingdiary/$closeperiod | [EXPERIMENTAL] ClosePeriod: Closes or locks the current period for the given Abor.
*AborApi* | [**create_abor**](docs/AborApi.md#create_abor) | **POST** /api/abor/{scope} | [EXPERIMENTAL] CreateAbor: Create an Abor.
*AborApi* | [**delete_abor**](docs/AborApi.md#delete_abor) | **DELETE** /api/abor/{scope}/{code} | [EXPERIMENTAL] DeleteAbor: Delete an Abor.
*AborApi* | [**delete_diary_entry**](docs/AborApi.md#delete_diary_entry) | **DELETE** /api/abor/{scope}/{code}/accountingdiary/{diaryEntryCode} | [EXPERIMENTAL] DeleteDiaryEntry: Delete a diary entry type 'Other' from the specified Abor.
*AborApi* | [**get_abor**](docs/AborApi.md#get_abor) | **GET** /api/abor/{scope}/{code} | [EXPERIMENTAL] GetAbor: Get Abor.
*AborApi* | [**get_abor_properties**](docs/AborApi.md#get_abor_properties) | **GET** /api/abor/{scope}/{code}/properties | [EXPERIMENTAL] GetAborProperties: Get Abor properties
*AborApi* | [**get_journal_entry_lines**](docs/AborApi.md#get_journal_entry_lines) | **POST** /api/abor/{scope}/{code}/journalentrylines/$query | [EXPERIMENTAL] GetJournalEntryLines: Get the Journal Entry lines for the given Abor.
*AborApi* | [**get_trial_balance**](docs/AborApi.md#get_trial_balance) | **POST** /api/abor/{scope}/{code}/trialbalance/$query | [EXPERIMENTAL] GetTrialBalance: Get the Trial Balance for the given Abor.
*AborApi* | [**list_abors**](docs/AborApi.md#list_abors) | **GET** /api/abor | [EXPERIMENTAL] ListAbors: List Abors.
*AborApi* | [**list_diary_entries**](docs/AborApi.md#list_diary_entries) | **GET** /api/abor/{scope}/{code}/accountingdiary | [EXPERIMENTAL] ListDiaryEntries: List diary entries.
*AborApi* | [**lock_period**](docs/AborApi.md#lock_period) | **POST** /api/abor/{scope}/{code}/accountingdiary/$lockperiod | [EXPERIMENTAL] LockPeriod: Locks the last Closed or given Closed Period.
*AborApi* | [**patch_abor**](docs/AborApi.md#patch_abor) | **PATCH** /api/abor/{scope}/{code} | [EXPERIMENTAL] PatchAbor: Patch Abor.
*AborApi* | [**re_open_periods**](docs/AborApi.md#re_open_periods) | **POST** /api/abor/{scope}/{code}/accountingdiary/$reopenperiods | [EXPERIMENTAL] ReOpenPeriods: Reopen periods from a seed Diary Entry Code or when not specified, the last Closed Period for the given Abor.
*AborApi* | [**upsert_abor_properties**](docs/AborApi.md#upsert_abor_properties) | **POST** /api/abor/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertAborProperties: Upsert Abor properties
*AborConfigurationApi* | [**create_abor_configuration**](docs/AborConfigurationApi.md#create_abor_configuration) | **POST** /api/aborconfiguration/{scope} | [EXPERIMENTAL] CreateAborConfiguration: Create an AborConfiguration.
*AborConfigurationApi* | [**delete_abor_configuration**](docs/AborConfigurationApi.md#delete_abor_configuration) | **DELETE** /api/aborconfiguration/{scope}/{code} | [EXPERIMENTAL] DeleteAborConfiguration: Delete an AborConfiguration.
*AborConfigurationApi* | [**get_abor_configuration**](docs/AborConfigurationApi.md#get_abor_configuration) | **GET** /api/aborconfiguration/{scope}/{code} | [EXPERIMENTAL] GetAborConfiguration: Get AborConfiguration.
*AborConfigurationApi* | [**get_abor_configuration_properties**](docs/AborConfigurationApi.md#get_abor_configuration_properties) | **GET** /api/aborconfiguration/{scope}/{code}/properties | [EXPERIMENTAL] GetAborConfigurationProperties: Get Abor Configuration properties
*AborConfigurationApi* | [**list_abor_configurations**](docs/AborConfigurationApi.md#list_abor_configurations) | **GET** /api/aborconfiguration | [EXPERIMENTAL] ListAborConfigurations: List AborConfiguration.
*AborConfigurationApi* | [**patch_abor_configuration**](docs/AborConfigurationApi.md#patch_abor_configuration) | **PATCH** /api/aborconfiguration/{scope}/{code} | [EXPERIMENTAL] PatchAborConfiguration: Patch Abor Configuration.
*AborConfigurationApi* | [**upsert_abor_configuration_properties**](docs/AborConfigurationApi.md#upsert_abor_configuration_properties) | **POST** /api/aborconfiguration/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertAborConfigurationProperties: Upsert AborConfiguration properties
*AddressKeyDefinitionApi* | [**create_address_key_definition**](docs/AddressKeyDefinitionApi.md#create_address_key_definition) | **POST** /api/addresskeydefinitions | [EARLY ACCESS] CreateAddressKeyDefinition: Create an AddressKeyDefinition.
*AddressKeyDefinitionApi* | [**get_address_key_definition**](docs/AddressKeyDefinitionApi.md#get_address_key_definition) | **GET** /api/addresskeydefinitions/{key} | [EARLY ACCESS] GetAddressKeyDefinition: Get an AddressKeyDefinition.
*AddressKeyDefinitionApi* | [**list_address_key_definitions**](docs/AddressKeyDefinitionApi.md#list_address_key_definitions) | **GET** /api/addresskeydefinitions | [EARLY ACCESS] ListAddressKeyDefinitions: List AddressKeyDefinitions.
*AggregatedReturnsApi* | [**delete_returns_entity**](docs/AggregatedReturnsApi.md#delete_returns_entity) | **DELETE** /api/returns/{scope}/{code} | [EXPERIMENTAL] DeleteReturnsEntity: Delete returns entity.
*AggregatedReturnsApi* | [**get_returns_entity**](docs/AggregatedReturnsApi.md#get_returns_entity) | **GET** /api/returns/{scope}/{code} | [EXPERIMENTAL] GetReturnsEntity: Get returns entity.
*AggregatedReturnsApi* | [**list_returns_entities**](docs/AggregatedReturnsApi.md#list_returns_entities) | **GET** /api/returns | [EXPERIMENTAL] ListReturnsEntities: List returns entities.
*AggregatedReturnsApi* | [**upsert_returns_entity**](docs/AggregatedReturnsApi.md#upsert_returns_entity) | **POST** /api/returns | [EXPERIMENTAL] UpsertReturnsEntity: Upsert returns entity.
*AggregationApi* | [**generate_configuration_recipe**](docs/AggregationApi.md#generate_configuration_recipe) | **POST** /api/aggregation/{scope}/{code}/$generateconfigurationrecipe | [EXPERIMENTAL] GenerateConfigurationRecipe: Generates a recipe sufficient to perform valuations for the given portfolio.
*AggregationApi* | [**get_queryable_keys**](docs/AggregationApi.md#get_queryable_keys) | **GET** /api/results/queryable/keys | GetQueryableKeys: Query the set of supported \"addresses\" that can be queried from the aggregation endpoint.
*AggregationApi* | [**get_valuation**](docs/AggregationApi.md#get_valuation) | **POST** /api/aggregation/$valuation | GetValuation: Perform valuation for a list of portfolios and/or portfolio groups
*AggregationApi* | [**get_valuation_of_weighted_instruments**](docs/AggregationApi.md#get_valuation_of_weighted_instruments) | **POST** /api/aggregation/$valuationinlined | GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio
*AllocationsApi* | [**delete_allocation**](docs/AllocationsApi.md#delete_allocation) | **DELETE** /api/allocations/{scope}/{code} | [EARLY ACCESS] DeleteAllocation: Delete allocation
*AllocationsApi* | [**get_allocation**](docs/AllocationsApi.md#get_allocation) | **GET** /api/allocations/{scope}/{code} | [EARLY ACCESS] GetAllocation: Get Allocation
*AllocationsApi* | [**list_allocations**](docs/AllocationsApi.md#list_allocations) | **GET** /api/allocations | ListAllocations: List Allocations
*AllocationsApi* | [**upsert_allocations**](docs/AllocationsApi.md#upsert_allocations) | **POST** /api/allocations | UpsertAllocations: Upsert Allocations
*AmortisationRuleSetsApi* | [**create_amortisation_rule_set**](docs/AmortisationRuleSetsApi.md#create_amortisation_rule_set) | **POST** /api/amortisation/rulesets/{scope} | [EXPERIMENTAL] CreateAmortisationRuleSet: Create an amortisation rule set.
*AmortisationRuleSetsApi* | [**delete_amortisation_ruleset**](docs/AmortisationRuleSetsApi.md#delete_amortisation_ruleset) | **DELETE** /api/amortisation/rulesets/{scope}/{code} | [EXPERIMENTAL] DeleteAmortisationRuleset: Delete an amortisation rule set.
*AmortisationRuleSetsApi* | [**get_amortisation_rule_set**](docs/AmortisationRuleSetsApi.md#get_amortisation_rule_set) | **GET** /api/amortisation/rulesets/{scope}/{code} | [EXPERIMENTAL] GetAmortisationRuleSet: Retrieve the definition of a single amortisation rule set
*AmortisationRuleSetsApi* | [**list_amortisation_rule_sets**](docs/AmortisationRuleSetsApi.md#list_amortisation_rule_sets) | **GET** /api/amortisation/rulesets | [EXPERIMENTAL] ListAmortisationRuleSets: List amortisation rule sets.
*AmortisationRuleSetsApi* | [**set_amortisation_rules**](docs/AmortisationRuleSetsApi.md#set_amortisation_rules) | **PUT** /api/amortisation/rulesets/{scope}/{code}/rules | [EXPERIMENTAL] SetAmortisationRules: Set Amortisation Rules on an existing Amortisation Rule Set.
*AmortisationRuleSetsApi* | [**update_amortisation_rule_set_details**](docs/AmortisationRuleSetsApi.md#update_amortisation_rule_set_details) | **PUT** /api/amortisation/rulesets/{scope}/{code}/details | [EXPERIMENTAL] UpdateAmortisationRuleSetDetails: Update an amortisation rule set.
*ApplicationMetadataApi* | [**get_excel_addin**](docs/ApplicationMetadataApi.md#get_excel_addin) | **GET** /api/metadata/downloads/exceladdin | GetExcelAddin: Download Excel Addin
*ApplicationMetadataApi* | [**get_lusid_versions**](docs/ApplicationMetadataApi.md#get_lusid_versions) | **GET** /api/metadata/versions | GetLusidVersions: Get LUSID versions
*ApplicationMetadataApi* | [**list_access_controlled_resources**](docs/ApplicationMetadataApi.md#list_access_controlled_resources) | **GET** /api/metadata/access/resources | ListAccessControlledResources: Get resources available for access control
*BlocksApi* | [**delete_block**](docs/BlocksApi.md#delete_block) | **DELETE** /api/blocks/{scope}/{code} | [EARLY ACCESS] DeleteBlock: Delete block
*BlocksApi* | [**get_block**](docs/BlocksApi.md#get_block) | **GET** /api/blocks/{scope}/{code} | [EARLY ACCESS] GetBlock: Get Block
*BlocksApi* | [**list_blocks**](docs/BlocksApi.md#list_blocks) | **GET** /api/blocks | [EARLY ACCESS] ListBlocks: List Blocks
*BlocksApi* | [**upsert_blocks**](docs/BlocksApi.md#upsert_blocks) | **POST** /api/blocks | [EARLY ACCESS] UpsertBlocks: Upsert Block
*CalendarsApi* | [**add_business_days_to_date**](docs/CalendarsApi.md#add_business_days_to_date) | **POST** /api/calendars/businessday/{scope}/add | [EARLY ACCESS] AddBusinessDaysToDate: Adds the requested number of Business Days to the provided date.
*CalendarsApi* | [**add_date_to_calendar**](docs/CalendarsApi.md#add_date_to_calendar) | **PUT** /api/calendars/generic/{scope}/{code}/dates | AddDateToCalendar: Add a date to a calendar
*CalendarsApi* | [**batch_upsert_dates_for_calendar**](docs/CalendarsApi.md#batch_upsert_dates_for_calendar) | **POST** /api/calendars/generic/{scope}/{code}/dates/$batchUpsert | BatchUpsertDatesForCalendar: Batch upsert dates to a calendar
*CalendarsApi* | [**create_calendar**](docs/CalendarsApi.md#create_calendar) | **POST** /api/calendars/generic | [EARLY ACCESS] CreateCalendar: Create a calendar in its generic form
*CalendarsApi* | [**delete_calendar**](docs/CalendarsApi.md#delete_calendar) | **DELETE** /api/calendars/generic/{scope}/{code} | [EARLY ACCESS] DeleteCalendar: Delete a calendar
*CalendarsApi* | [**delete_date_from_calendar**](docs/CalendarsApi.md#delete_date_from_calendar) | **DELETE** /api/calendars/generic/{scope}/{code}/dates/{dateId} | DeleteDateFromCalendar: Remove a date from a calendar
*CalendarsApi* | [**delete_dates_from_calendar**](docs/CalendarsApi.md#delete_dates_from_calendar) | **POST** /api/calendars/generic/{scope}/{code}/dates/$delete | DeleteDatesFromCalendar: Delete dates from a calendar
*CalendarsApi* | [**generate_schedule**](docs/CalendarsApi.md#generate_schedule) | **POST** /api/calendars/schedule/{scope} | [EARLY ACCESS] GenerateSchedule: Generate an ordered schedule of dates.
*CalendarsApi* | [**get_calendar**](docs/CalendarsApi.md#get_calendar) | **GET** /api/calendars/generic/{scope}/{code} | GetCalendar: Get a calendar in its generic form
*CalendarsApi* | [**get_dates**](docs/CalendarsApi.md#get_dates) | **GET** /api/calendars/generic/{scope}/{code}/dates | [EARLY ACCESS] GetDates: Get dates for a specific calendar
*CalendarsApi* | [**is_business_date_time**](docs/CalendarsApi.md#is_business_date_time) | **GET** /api/calendars/businessday/{scope}/{code} | [EARLY ACCESS] IsBusinessDateTime: Check whether a DateTime is a \"Business DateTime\"
*CalendarsApi* | [**list_calendars**](docs/CalendarsApi.md#list_calendars) | **GET** /api/calendars/generic | [EARLY ACCESS] ListCalendars: List Calendars
*CalendarsApi* | [**list_calendars_in_scope**](docs/CalendarsApi.md#list_calendars_in_scope) | **GET** /api/calendars/generic/{scope} | ListCalendarsInScope: List all calenders in a specified scope
*CalendarsApi* | [**update_calendar**](docs/CalendarsApi.md#update_calendar) | **POST** /api/calendars/generic/{scope}/{code} | [EARLY ACCESS] UpdateCalendar: Update a calendar
*ChartOfAccountsApi* | [**create_chart_of_accounts**](docs/ChartOfAccountsApi.md#create_chart_of_accounts) | **POST** /api/chartofaccounts/{scope} | [EXPERIMENTAL] CreateChartOfAccounts: Create a Chart of Accounts
*ChartOfAccountsApi* | [**create_cleardown_module**](docs/ChartOfAccountsApi.md#create_cleardown_module) | **POST** /api/chartofaccounts/{scope}/{code}/cleardownmodules | [EXPERIMENTAL] CreateCleardownModule: Create a Cleardown Module
*ChartOfAccountsApi* | [**create_general_ledger_profile**](docs/ChartOfAccountsApi.md#create_general_ledger_profile) | **POST** /api/chartofaccounts/{scope}/{code}/generalledgerprofile | [EXPERIMENTAL] CreateGeneralLedgerProfile: Create a General Ledger Profile.
*ChartOfAccountsApi* | [**create_posting_module**](docs/ChartOfAccountsApi.md#create_posting_module) | **POST** /api/chartofaccounts/{scope}/{code}/postingmodules | [EXPERIMENTAL] CreatePostingModule: Create a Posting Module
*ChartOfAccountsApi* | [**delete_accounts**](docs/ChartOfAccountsApi.md#delete_accounts) | **POST** /api/chartofaccounts/{scope}/{code}/accounts/$delete | [EXPERIMENTAL] DeleteAccounts: Soft or hard delete multiple accounts
*ChartOfAccountsApi* | [**delete_chart_of_accounts**](docs/ChartOfAccountsApi.md#delete_chart_of_accounts) | **DELETE** /api/chartofaccounts/{scope}/{code} | [EXPERIMENTAL] DeleteChartOfAccounts: Delete a Chart of Accounts
*ChartOfAccountsApi* | [**delete_cleardown_module**](docs/ChartOfAccountsApi.md#delete_cleardown_module) | **DELETE** /api/chartofaccounts/{scope}/{code}/cleardownmodules/{cleardownModuleCode} | [EXPERIMENTAL] DeleteCleardownModule: Delete a Cleardown Module.
*ChartOfAccountsApi* | [**delete_general_ledger_profile**](docs/ChartOfAccountsApi.md#delete_general_ledger_profile) | **DELETE** /api/chartofaccounts/{scope}/{code}/generalledgerprofile/{generalLedgerProfileCode} | [EXPERIMENTAL] DeleteGeneralLedgerProfile: Delete a General Ledger Profile.
*ChartOfAccountsApi* | [**delete_posting_module**](docs/ChartOfAccountsApi.md#delete_posting_module) | **DELETE** /api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode} | [EXPERIMENTAL] DeletePostingModule: Delete a Posting Module.
*ChartOfAccountsApi* | [**get_account**](docs/ChartOfAccountsApi.md#get_account) | **GET** /api/chartofaccounts/{scope}/{code}/accounts/{accountCode} | [EXPERIMENTAL] GetAccount: Get Account
*ChartOfAccountsApi* | [**get_account_properties**](docs/ChartOfAccountsApi.md#get_account_properties) | **GET** /api/chartofaccounts/{scope}/{code}/accounts/{accountCode}/properties | [EXPERIMENTAL] GetAccountProperties: Get Account properties
*ChartOfAccountsApi* | [**get_chart_of_accounts**](docs/ChartOfAccountsApi.md#get_chart_of_accounts) | **GET** /api/chartofaccounts/{scope}/{code} | [EXPERIMENTAL] GetChartOfAccounts: Get ChartOfAccounts
*ChartOfAccountsApi* | [**get_chart_of_accounts_properties**](docs/ChartOfAccountsApi.md#get_chart_of_accounts_properties) | **GET** /api/chartofaccounts/{scope}/{code}/properties | [EXPERIMENTAL] GetChartOfAccountsProperties: Get chart of accounts properties
*ChartOfAccountsApi* | [**get_cleardown_module**](docs/ChartOfAccountsApi.md#get_cleardown_module) | **GET** /api/chartofaccounts/{scope}/{code}/cleardownmodules/{cleardownModuleCode} | [EXPERIMENTAL] GetCleardownModule: Get a Cleardown Module
*ChartOfAccountsApi* | [**get_general_ledger_profile**](docs/ChartOfAccountsApi.md#get_general_ledger_profile) | **GET** /api/chartofaccounts/{scope}/{code}/generalledgerprofile/{generalLedgerProfileCode} | [EXPERIMENTAL] GetGeneralLedgerProfile: Get a General Ledger Profile.
*ChartOfAccountsApi* | [**get_posting_module**](docs/ChartOfAccountsApi.md#get_posting_module) | **GET** /api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode} | [EXPERIMENTAL] GetPostingModule: Get a Posting Module
*ChartOfAccountsApi* | [**list_accounts**](docs/ChartOfAccountsApi.md#list_accounts) | **GET** /api/chartofaccounts/{scope}/{code}/accounts | [EXPERIMENTAL] ListAccounts: List Accounts
*ChartOfAccountsApi* | [**list_charts_of_accounts**](docs/ChartOfAccountsApi.md#list_charts_of_accounts) | **GET** /api/chartofaccounts | [EXPERIMENTAL] ListChartsOfAccounts: List Charts of Accounts
*ChartOfAccountsApi* | [**list_cleardown_module_rules**](docs/ChartOfAccountsApi.md#list_cleardown_module_rules) | **GET** /api/chartofaccounts/{scope}/{code}/cleardownmodules/{cleardownModuleCode}/cleardownrules | [EXPERIMENTAL] ListCleardownModuleRules: List Cleardown Module Rules
*ChartOfAccountsApi* | [**list_cleardown_modules**](docs/ChartOfAccountsApi.md#list_cleardown_modules) | **GET** /api/chartofaccounts/{scope}/{code}/cleardownmodules | [EXPERIMENTAL] ListCleardownModules: List Cleardown Modules
*ChartOfAccountsApi* | [**list_general_ledger_profiles**](docs/ChartOfAccountsApi.md#list_general_ledger_profiles) | **GET** /api/chartofaccounts/{scope}/{code}/generalledgerprofile | [EXPERIMENTAL] ListGeneralLedgerProfiles: List General Ledger Profiles.
*ChartOfAccountsApi* | [**list_posting_module_rules**](docs/ChartOfAccountsApi.md#list_posting_module_rules) | **GET** /api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode}/postingrules | [EXPERIMENTAL] ListPostingModuleRules: List Posting Module Rules
*ChartOfAccountsApi* | [**list_posting_modules**](docs/ChartOfAccountsApi.md#list_posting_modules) | **GET** /api/chartofaccounts/{scope}/{code}/postingmodules | [EXPERIMENTAL] ListPostingModules: List Posting Modules
*ChartOfAccountsApi* | [**patch_chart_of_accounts**](docs/ChartOfAccountsApi.md#patch_chart_of_accounts) | **PATCH** /api/chartofaccounts/{scope}/{code} | [EXPERIMENTAL] PatchChartOfAccounts: Patch a Chart of Accounts.
*ChartOfAccountsApi* | [**patch_cleardown_module**](docs/ChartOfAccountsApi.md#patch_cleardown_module) | **PATCH** /api/chartofaccounts/{scope}/{code}/cleardownmodules/{cleardownModuleCode} | [EXPERIMENTAL] PatchCleardownModule: Patch a Cleardown Module
*ChartOfAccountsApi* | [**patch_posting_module**](docs/ChartOfAccountsApi.md#patch_posting_module) | **PATCH** /api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode} | [EXPERIMENTAL] PatchPostingModule: Patch a Posting Module
*ChartOfAccountsApi* | [**set_cleardown_module_details**](docs/ChartOfAccountsApi.md#set_cleardown_module_details) | **PUT** /api/chartofaccounts/{scope}/{code}/cleardownmodules/{cleardownModuleCode} | [EXPERIMENTAL] SetCleardownModuleDetails: Set the details of a Cleardown Module
*ChartOfAccountsApi* | [**set_cleardown_module_rules**](docs/ChartOfAccountsApi.md#set_cleardown_module_rules) | **PUT** /api/chartofaccounts/{scope}/{code}/cleardownmodules/{cleardownModuleCode}/cleardownrules | [EXPERIMENTAL] SetCleardownModuleRules: Set the rules of a Cleardown Module
*ChartOfAccountsApi* | [**set_general_ledger_profile_mappings**](docs/ChartOfAccountsApi.md#set_general_ledger_profile_mappings) | **PUT** /api/chartofaccounts/{scope}/{code}/generalledgerprofile/{generalLedgerProfileCode}/mappings | [EXPERIMENTAL] SetGeneralLedgerProfileMappings: Sets the General Ledger Profile Mappings.
*ChartOfAccountsApi* | [**set_posting_module_details**](docs/ChartOfAccountsApi.md#set_posting_module_details) | **PUT** /api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode} | [EXPERIMENTAL] SetPostingModuleDetails: Set the details of a Posting Module
*ChartOfAccountsApi* | [**set_posting_module_rules**](docs/ChartOfAccountsApi.md#set_posting_module_rules) | **PUT** /api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode}/postingrules | [EXPERIMENTAL] SetPostingModuleRules: Set the rules of a Posting Module
*ChartOfAccountsApi* | [**upsert_account_properties**](docs/ChartOfAccountsApi.md#upsert_account_properties) | **POST** /api/chartofaccounts/{scope}/{code}/accounts/{accountCode}/properties/$upsert | [EXPERIMENTAL] UpsertAccountProperties: Upsert account properties
*ChartOfAccountsApi* | [**upsert_accounts**](docs/ChartOfAccountsApi.md#upsert_accounts) | **POST** /api/chartofaccounts/{scope}/{code}/accounts | [EXPERIMENTAL] UpsertAccounts: Upsert Accounts
*ChartOfAccountsApi* | [**upsert_chart_of_accounts_properties**](docs/ChartOfAccountsApi.md#upsert_chart_of_accounts_properties) | **POST** /api/chartofaccounts/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertChartOfAccountsProperties: Upsert Chart of Accounts properties
*CheckDefinitionsApi* | [**create_check_definition**](docs/CheckDefinitionsApi.md#create_check_definition) | **POST** /api/dataquality/checkdefinitions | [EXPERIMENTAL] CreateCheckDefinition: Create a Check Definition
*CheckDefinitionsApi* | [**delete_check_definition**](docs/CheckDefinitionsApi.md#delete_check_definition) | **DELETE** /api/dataquality/checkdefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteCheckDefinition: Deletes a particular Check Definition
*CheckDefinitionsApi* | [**delete_rules**](docs/CheckDefinitionsApi.md#delete_rules) | **POST** /api/dataquality/checkdefinitions/{scope}/{code}/$deleteRules | [EXPERIMENTAL] DeleteRules: Delete rules on a particular Check Definition
*CheckDefinitionsApi* | [**get_check_definition**](docs/CheckDefinitionsApi.md#get_check_definition) | **GET** /api/dataquality/checkdefinitions/{scope}/{code} | [EXPERIMENTAL] GetCheckDefinition: Get a single Check Definition by scope and code.
*CheckDefinitionsApi* | [**list_check_definitions**](docs/CheckDefinitionsApi.md#list_check_definitions) | **GET** /api/dataquality/checkdefinitions | [EXPERIMENTAL] ListCheckDefinitions: List Check Definitions
*CheckDefinitionsApi* | [**run_check_definition**](docs/CheckDefinitionsApi.md#run_check_definition) | **POST** /api/dataquality/checkdefinitions/{scope}/{code}/$run | [EXPERIMENTAL] RunCheckDefinition: Runs a Check Definition against given dataset.
*CheckDefinitionsApi* | [**update_check_definition**](docs/CheckDefinitionsApi.md#update_check_definition) | **PUT** /api/dataquality/checkdefinitions/{scope}/{code} | [EXPERIMENTAL] UpdateCheckDefinition: Update Check Definition defined by scope and code
*CheckDefinitionsApi* | [**upsert_rules**](docs/CheckDefinitionsApi.md#upsert_rules) | **POST** /api/dataquality/checkdefinitions/{scope}/{code}/$upsertRules | [EXPERIMENTAL] UpsertRules: Upsert rules to a particular Check Definition
*ComplexMarketDataApi* | [**delete_complex_market_data**](docs/ComplexMarketDataApi.md#delete_complex_market_data) | **POST** /api/complexmarketdata/{scope}/$delete | DeleteComplexMarketData: Delete one or more items of complex market data, assuming they are present.
*ComplexMarketDataApi* | [**get_complex_market_data**](docs/ComplexMarketDataApi.md#get_complex_market_data) | **POST** /api/complexmarketdata/{scope}/$get | GetComplexMarketData: Get complex market data
*ComplexMarketDataApi* | [**list_complex_market_data**](docs/ComplexMarketDataApi.md#list_complex_market_data) | **GET** /api/complexmarketdata | ListComplexMarketData: List the set of ComplexMarketData
*ComplexMarketDataApi* | [**upsert_append_complex_market_data**](docs/ComplexMarketDataApi.md#upsert_append_complex_market_data) | **POST** /api/complexmarketdata/{scope}/$append | [EARLY ACCESS] UpsertAppendComplexMarketData: Appends a new point to the end of a ComplexMarketData definition.
*ComplexMarketDataApi* | [**upsert_complex_market_data**](docs/ComplexMarketDataApi.md#upsert_complex_market_data) | **POST** /api/complexmarketdata/{scope} | UpsertComplexMarketData: Upsert a set of complex market data items. This creates or updates the data in Lusid.
*ComplianceApi* | [**create_compliance_template**](docs/ComplianceApi.md#create_compliance_template) | **POST** /api/compliance/templates/{scope} | [EARLY ACCESS] CreateComplianceTemplate: Create a Compliance Rule Template
*ComplianceApi* | [**delete_compliance_rule**](docs/ComplianceApi.md#delete_compliance_rule) | **DELETE** /api/compliance/rules/{scope}/{code} | [EARLY ACCESS] DeleteComplianceRule: Delete compliance rule.
*ComplianceApi* | [**delete_compliance_template**](docs/ComplianceApi.md#delete_compliance_template) | **DELETE** /api/compliance/templates/{scope}/{code} | [EARLY ACCESS] DeleteComplianceTemplate: Delete a ComplianceRuleTemplate
*ComplianceApi* | [**get_compliance_rule**](docs/ComplianceApi.md#get_compliance_rule) | **GET** /api/compliance/rules/{scope}/{code} | [EARLY ACCESS] GetComplianceRule: Get compliance rule.
*ComplianceApi* | [**get_compliance_rule_result**](docs/ComplianceApi.md#get_compliance_rule_result) | **GET** /api/compliance/runs/summary/{runScope}/{runCode}/{ruleScope}/{ruleCode} | [EARLY ACCESS] GetComplianceRuleResult: Get detailed results for a specific rule within a compliance run.
*ComplianceApi* | [**get_compliance_template**](docs/ComplianceApi.md#get_compliance_template) | **GET** /api/compliance/templates/{scope}/{code} | [EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.
*ComplianceApi* | [**get_decorated_compliance_run_summary**](docs/ComplianceApi.md#get_decorated_compliance_run_summary) | **GET** /api/compliance/runs/summary/{scope}/{code}/$decorate | [EARLY ACCESS] GetDecoratedComplianceRunSummary: Get decorated summary results for a specific compliance run.
*ComplianceApi* | [**list_compliance_rules**](docs/ComplianceApi.md#list_compliance_rules) | **GET** /api/compliance/rules | [EARLY ACCESS] ListComplianceRules: List compliance rules.
*ComplianceApi* | [**list_compliance_runs**](docs/ComplianceApi.md#list_compliance_runs) | **GET** /api/compliance/runs | [EARLY ACCESS] ListComplianceRuns: List historical compliance run identifiers.
*ComplianceApi* | [**list_compliance_templates**](docs/ComplianceApi.md#list_compliance_templates) | **GET** /api/compliance/templates | [EARLY ACCESS] ListComplianceTemplates: List compliance templates.
*ComplianceApi* | [**list_order_breach_history**](docs/ComplianceApi.md#list_order_breach_history) | **GET** /api/compliance/runs/breaches | [EXPERIMENTAL] ListOrderBreachHistory: List Historical Order Breaches.
*ComplianceApi* | [**run_compliance**](docs/ComplianceApi.md#run_compliance) | **POST** /api/compliance/runs | [EARLY ACCESS] RunCompliance: Run a compliance check.
*ComplianceApi* | [**run_compliance_preview**](docs/ComplianceApi.md#run_compliance_preview) | **POST** /api/compliance/preview/runs | [EARLY ACCESS] RunCompliancePreview: Run a compliance check.
*ComplianceApi* | [**update_compliance_template**](docs/ComplianceApi.md#update_compliance_template) | **PUT** /api/compliance/templates/{scope}/{code} | [EARLY ACCESS] UpdateComplianceTemplate: Update a ComplianceRuleTemplate
*ComplianceApi* | [**upsert_compliance_rule**](docs/ComplianceApi.md#upsert_compliance_rule) | **POST** /api/compliance/rules | [EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.
*ComplianceApi* | [**upsert_compliance_run_summary**](docs/ComplianceApi.md#upsert_compliance_run_summary) | **POST** /api/compliance/runs/summary | [EARLY ACCESS] UpsertComplianceRunSummary: Upsert a compliance run summary.
*ConfigurationRecipeApi* | [**delete_configuration_recipe**](docs/ConfigurationRecipeApi.md#delete_configuration_recipe) | **DELETE** /api/recipes/{scope}/{code} | DeleteConfigurationRecipe: Delete a Configuration Recipe, assuming that it is present.
*ConfigurationRecipeApi* | [**delete_recipe_composer**](docs/ConfigurationRecipeApi.md#delete_recipe_composer) | **DELETE** /api/recipes/composer/{scope}/{code} | DeleteRecipeComposer: Delete a Recipe Composer, assuming that it is present.
*ConfigurationRecipeApi* | [**get_configuration_recipe**](docs/ConfigurationRecipeApi.md#get_configuration_recipe) | **GET** /api/recipes/{scope}/{code} | GetConfigurationRecipe: Get Configuration Recipe
*ConfigurationRecipeApi* | [**get_derived_recipe**](docs/ConfigurationRecipeApi.md#get_derived_recipe) | **GET** /api/recipes/derived/{scope}/{code} | GetDerivedRecipe: Get Configuration Recipe either from the store or expanded from a Recipe Composer.
*ConfigurationRecipeApi* | [**get_recipe_composer**](docs/ConfigurationRecipeApi.md#get_recipe_composer) | **GET** /api/recipes/composer/{scope}/{code} | GetRecipeComposer: Get Recipe Composer
*ConfigurationRecipeApi* | [**get_recipe_composer_resolved_inline**](docs/ConfigurationRecipeApi.md#get_recipe_composer_resolved_inline) | **POST** /api/recipes/composer/resolvedinline$ | GetRecipeComposerResolvedInline: Given a Recipe Composer, this endpoint expands into a Configuration Recipe without persistence. Primarily used for testing purposes.
*ConfigurationRecipeApi* | [**list_configuration_recipes**](docs/ConfigurationRecipeApi.md#list_configuration_recipes) | **GET** /api/recipes | ListConfigurationRecipes: List the set of Configuration Recipes
*ConfigurationRecipeApi* | [**list_derived_recipes**](docs/ConfigurationRecipeApi.md#list_derived_recipes) | **GET** /api/recipes/derived | ListDerivedRecipes: List the complete set of all Configuration Recipes, both from the configuration recipe store and also from expanded recipe composers.
*ConfigurationRecipeApi* | [**list_recipe_composers**](docs/ConfigurationRecipeApi.md#list_recipe_composers) | **GET** /api/recipes/composer | ListRecipeComposers: List the set of Recipe Composers
*ConfigurationRecipeApi* | [**upsert_configuration_recipe**](docs/ConfigurationRecipeApi.md#upsert_configuration_recipe) | **POST** /api/recipes | UpsertConfigurationRecipe: Upsert a Configuration Recipe. This creates or updates the data in Lusid.
*ConfigurationRecipeApi* | [**upsert_recipe_composer**](docs/ConfigurationRecipeApi.md#upsert_recipe_composer) | **POST** /api/recipes/composer | UpsertRecipeComposer: Upsert a Recipe Composer. This creates or updates the data in Lusid.
*ConventionsApi* | [**delete_cds_flow_conventions**](docs/ConventionsApi.md#delete_cds_flow_conventions) | **DELETE** /api/conventions/credit/conventions/{scope}/{code} | [BETA] DeleteCdsFlowConventions: Delete the CDS Flow Conventions of given scope and code, assuming that it is present.
*ConventionsApi* | [**delete_flow_conventions**](docs/ConventionsApi.md#delete_flow_conventions) | **DELETE** /api/conventions/rates/flowconventions/{scope}/{code} | [BETA] DeleteFlowConventions: Delete the Flow Conventions of given scope and code, assuming that it is present.
*ConventionsApi* | [**delete_index_convention**](docs/ConventionsApi.md#delete_index_convention) | **DELETE** /api/conventions/rates/indexconventions/{scope}/{code} | [BETA] DeleteIndexConvention: Delete the Index Convention of given scope and code, assuming that it is present.
*ConventionsApi* | [**get_cds_flow_conventions**](docs/ConventionsApi.md#get_cds_flow_conventions) | **GET** /api/conventions/credit/conventions/{scope}/{code} | [BETA] GetCdsFlowConventions: Get CDS Flow Conventions
*ConventionsApi* | [**get_flow_conventions**](docs/ConventionsApi.md#get_flow_conventions) | **GET** /api/conventions/rates/flowconventions/{scope}/{code} | [BETA] GetFlowConventions: Get Flow Conventions
*ConventionsApi* | [**get_index_convention**](docs/ConventionsApi.md#get_index_convention) | **GET** /api/conventions/rates/indexconventions/{scope}/{code} | [BETA] GetIndexConvention: Get Index Convention
*ConventionsApi* | [**list_cds_flow_conventions**](docs/ConventionsApi.md#list_cds_flow_conventions) | **GET** /api/conventions/credit/conventions | [BETA] ListCdsFlowConventions: List the set of CDS Flow Conventions
*ConventionsApi* | [**list_flow_conventions**](docs/ConventionsApi.md#list_flow_conventions) | **GET** /api/conventions/rates/flowconventions | [BETA] ListFlowConventions: List the set of Flow Conventions
*ConventionsApi* | [**list_index_convention**](docs/ConventionsApi.md#list_index_convention) | **GET** /api/conventions/rates/indexconventions | [BETA] ListIndexConvention: List the set of Index Conventions
*ConventionsApi* | [**upsert_cds_flow_conventions**](docs/ConventionsApi.md#upsert_cds_flow_conventions) | **POST** /api/conventions/credit/conventions | [BETA] UpsertCdsFlowConventions: Upsert a set of CDS Flow Conventions. This creates or updates the data in Lusid.
*ConventionsApi* | [**upsert_flow_conventions**](docs/ConventionsApi.md#upsert_flow_conventions) | **POST** /api/conventions/rates/flowconventions | [BETA] UpsertFlowConventions: Upsert Flow Conventions. This creates or updates the data in Lusid.
*ConventionsApi* | [**upsert_index_convention**](docs/ConventionsApi.md#upsert_index_convention) | **POST** /api/conventions/rates/indexconventions | [BETA] UpsertIndexConvention: Upsert a set of Index Convention. This creates or updates the data in Lusid.
*CorporateActionSourcesApi* | [**batch_upsert_corporate_actions**](docs/CorporateActionSourcesApi.md#batch_upsert_corporate_actions) | **POST** /api/corporateactionsources/{scope}/{code}/corporateactions | [EARLY ACCESS] BatchUpsertCorporateActions: Batch upsert corporate actions (instrument transition events) to corporate action source.
*CorporateActionSourcesApi* | [**create_corporate_action_source**](docs/CorporateActionSourcesApi.md#create_corporate_action_source) | **POST** /api/corporateactionsources | [EARLY ACCESS] CreateCorporateActionSource: Create corporate action source
*CorporateActionSourcesApi* | [**delete_corporate_action_source**](docs/CorporateActionSourcesApi.md#delete_corporate_action_source) | **DELETE** /api/corporateactionsources/{scope}/{code} | [EARLY ACCESS] DeleteCorporateActionSource: Delete a corporate action source
*CorporateActionSourcesApi* | [**delete_corporate_actions**](docs/CorporateActionSourcesApi.md#delete_corporate_actions) | **DELETE** /api/corporateactionsources/{scope}/{code}/corporateactions | [EARLY ACCESS] DeleteCorporateActions: Delete corporate actions (instrument transition events) from a corporate action source
*CorporateActionSourcesApi* | [**delete_instrument_events**](docs/CorporateActionSourcesApi.md#delete_instrument_events) | **DELETE** /api/corporateactionsources/{scope}/{code}/instrumentevents | [EARLY ACCESS] DeleteInstrumentEvents: Delete instrument events from a corporate action source
*CorporateActionSourcesApi* | [**get_corporate_actions**](docs/CorporateActionSourcesApi.md#get_corporate_actions) | **GET** /api/corporateactionsources/{scope}/{code}/corporateactions | [EARLY ACCESS] GetCorporateActions: List corporate actions (instrument transition events) from the corporate action source.
*CorporateActionSourcesApi* | [**get_instrument_events**](docs/CorporateActionSourcesApi.md#get_instrument_events) | **GET** /api/corporateactionsources/{scope}/{code}/instrumentevents | [EARLY ACCESS] GetInstrumentEvents: Get extrinsic instrument events out of a given corporate actions source.
*CorporateActionSourcesApi* | [**list_corporate_action_sources**](docs/CorporateActionSourcesApi.md#list_corporate_action_sources) | **GET** /api/corporateactionsources | [EARLY ACCESS] ListCorporateActionSources: List corporate action sources
*CorporateActionSourcesApi* | [**upsert_instrument_events**](docs/CorporateActionSourcesApi.md#upsert_instrument_events) | **POST** /api/corporateactionsources/{scope}/{code}/instrumentevents | [EARLY ACCESS] UpsertInstrumentEvents: Upsert instrument events to the provided corporate actions source.
*CounterpartiesApi* | [**delete_counterparty_agreement**](docs/CounterpartiesApi.md#delete_counterparty_agreement) | **DELETE** /api/counterparties/counterpartyagreements/{scope}/{code} | [EARLY ACCESS] DeleteCounterpartyAgreement: Delete the Counterparty Agreement of given scope and code
*CounterpartiesApi* | [**delete_credit_support_annex**](docs/CounterpartiesApi.md#delete_credit_support_annex) | **DELETE** /api/counterparties/creditsupportannexes/{scope}/{code} | [EARLY ACCESS] DeleteCreditSupportAnnex: Delete the Credit Support Annex of given scope and code
*CounterpartiesApi* | [**get_counterparty_agreement**](docs/CounterpartiesApi.md#get_counterparty_agreement) | **GET** /api/counterparties/counterpartyagreements/{scope}/{code} | [EARLY ACCESS] GetCounterpartyAgreement: Get Counterparty Agreement
*CounterpartiesApi* | [**get_credit_support_annex**](docs/CounterpartiesApi.md#get_credit_support_annex) | **GET** /api/counterparties/creditsupportannexes/{scope}/{code} | [EARLY ACCESS] GetCreditSupportAnnex: Get Credit Support Annex
*CounterpartiesApi* | [**list_counterparty_agreements**](docs/CounterpartiesApi.md#list_counterparty_agreements) | **GET** /api/counterparties/counterpartyagreements | [EARLY ACCESS] ListCounterpartyAgreements: List the set of Counterparty Agreements
*CounterpartiesApi* | [**list_credit_support_annexes**](docs/CounterpartiesApi.md#list_credit_support_annexes) | **GET** /api/counterparties/creditsupportannexes | [EARLY ACCESS] ListCreditSupportAnnexes: List the set of Credit Support Annexes
*CounterpartiesApi* | [**upsert_counterparty_agreement**](docs/CounterpartiesApi.md#upsert_counterparty_agreement) | **POST** /api/counterparties/counterpartyagreements | [EARLY ACCESS] UpsertCounterpartyAgreement: Upsert Counterparty Agreement
*CounterpartiesApi* | [**upsert_credit_support_annex**](docs/CounterpartiesApi.md#upsert_credit_support_annex) | **POST** /api/counterparties/creditsupportannexes | [EARLY ACCESS] UpsertCreditSupportAnnex: Upsert Credit Support Annex
*CustomEntitiesApi* | [**delete_custom_entity**](docs/CustomEntitiesApi.md#delete_custom_entity) | **DELETE** /api/customentities/{entityType}/{identifierType}/{identifierValue} | DeleteCustomEntity: Delete a Custom Entity instance.
*CustomEntitiesApi* | [**delete_custom_entity_access_metadata**](docs/CustomEntitiesApi.md#delete_custom_entity_access_metadata) | **DELETE** /api/customentities/{entityType}/{identifierType}/{identifierValue}/metadata/{metadataKey} | [EARLY ACCESS] DeleteCustomEntityAccessMetadata: Delete a Custom Entity Access Metadata entry
*CustomEntitiesApi* | [**get_all_custom_entity_access_metadata**](docs/CustomEntitiesApi.md#get_all_custom_entity_access_metadata) | **GET** /api/customentities/{entityType}/{identifierType}/{identifierValue}/metadata | [EARLY ACCESS] GetAllCustomEntityAccessMetadata: Get all the Access Metadata rules for a Custom Entity
*CustomEntitiesApi* | [**get_all_custom_entity_properties**](docs/CustomEntitiesApi.md#get_all_custom_entity_properties) | **GET** /api/customentities/{entityType}/{identifierType}/{identifierValue}/properties | [EARLY ACCESS] GetAllCustomEntityProperties: Get all properties related to a Custom Entity instance.
*CustomEntitiesApi* | [**get_custom_entity**](docs/CustomEntitiesApi.md#get_custom_entity) | **GET** /api/customentities/{entityType}/{identifierType}/{identifierValue} | GetCustomEntity: Get a Custom Entity instance.
*CustomEntitiesApi* | [**get_custom_entity_access_metadata_by_key**](docs/CustomEntitiesApi.md#get_custom_entity_access_metadata_by_key) | **GET** /api/customentities/{entityType}/{identifierType}/{identifierValue}/metadata/{metadataKey} | [EARLY ACCESS] GetCustomEntityAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Custom Entity
*CustomEntitiesApi* | [**get_custom_entity_relationships**](docs/CustomEntitiesApi.md#get_custom_entity_relationships) | **GET** /api/customentities/{entityType}/{identifierType}/{identifierValue}/relationships | [EARLY ACCESS] GetCustomEntityRelationships: Get Relationships for Custom Entity
*CustomEntitiesApi* | [**list_custom_entities**](docs/CustomEntitiesApi.md#list_custom_entities) | **GET** /api/customentities/{entityType} | ListCustomEntities: List Custom Entities of the specified entityType.
*CustomEntitiesApi* | [**patch_custom_entity_access_metadata**](docs/CustomEntitiesApi.md#patch_custom_entity_access_metadata) | **PATCH** /api/customentities/{entityType}/{identifierType}/{identifierValue}/metadata | [EARLY ACCESS] PatchCustomEntityAccessMetadata: Patch Access Metadata rules for a Custom Entity.
*CustomEntitiesApi* | [**upsert_custom_entities**](docs/CustomEntitiesApi.md#upsert_custom_entities) | **POST** /api/customentities/{entityType}/$batchUpsert | [EARLY ACCESS] UpsertCustomEntities: Batch upsert instances of Custom Entities
*CustomEntitiesApi* | [**upsert_custom_entity**](docs/CustomEntitiesApi.md#upsert_custom_entity) | **POST** /api/customentities/{entityType} | UpsertCustomEntity: Upsert a Custom Entity instance
*CustomEntitiesApi* | [**upsert_custom_entity_access_metadata**](docs/CustomEntitiesApi.md#upsert_custom_entity_access_metadata) | **PUT** /api/customentities/{entityType}/{identifierType}/{identifierValue}/metadata/{metadataKey} | [EARLY ACCESS] UpsertCustomEntityAccessMetadata: Upsert a Custom Entity Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
*CustomEntityDefinitionsApi* | [**create_custom_entity_definition**](docs/CustomEntityDefinitionsApi.md#create_custom_entity_definition) | **POST** /api/customentities/entitytypes | [EARLY ACCESS] CreateCustomEntityDefinition: Define a new Custom Entity type.
*CustomEntityDefinitionsApi* | [**get_definition**](docs/CustomEntityDefinitionsApi.md#get_definition) | **GET** /api/customentities/entitytypes/{entityType} | [EARLY ACCESS] GetDefinition: Get a Custom Entity type definition.
*CustomEntityDefinitionsApi* | [**list_custom_entity_definitions**](docs/CustomEntityDefinitionsApi.md#list_custom_entity_definitions) | **GET** /api/customentities/entitytypes | [EARLY ACCESS] ListCustomEntityDefinitions: List the Custom Entity type definitions
*CustomEntityDefinitionsApi* | [**update_custom_entity_definition**](docs/CustomEntityDefinitionsApi.md#update_custom_entity_definition) | **PUT** /api/customentities/entitytypes/{entityType} | [EARLY ACCESS] UpdateCustomEntityDefinition: Modify an existing Custom Entity type.
*CustomDataModelsApi* | [**batch_amend**](docs/CustomDataModelsApi.md#batch_amend) | **POST** /api/datamodel/$batchamend | [EXPERIMENTAL] BatchAmend: Batch amend entities Custom Data Model membership.
*CustomDataModelsApi* | [**create_custom_data_model**](docs/CustomDataModelsApi.md#create_custom_data_model) | **POST** /api/datamodel/{entityType} | [EXPERIMENTAL] CreateCustomDataModel: Create a Custom Data Model
*CustomDataModelsApi* | [**delete_custom_data_model**](docs/CustomDataModelsApi.md#delete_custom_data_model) | **DELETE** /api/datamodel/{entityType}/{scope}/{code} | [EXPERIMENTAL] DeleteCustomDataModel: Delete a Custom Data Model
*CustomDataModelsApi* | [**get_custom_data_model**](docs/CustomDataModelsApi.md#get_custom_data_model) | **GET** /api/datamodel/{entityType}/{scope}/{code} | [EXPERIMENTAL] GetCustomDataModel: Get a Custom Data Model
*CustomDataModelsApi* | [**list_data_model_hierarchies**](docs/CustomDataModelsApi.md#list_data_model_hierarchies) | **GET** /api/datamodel/hierarchies | [EXPERIMENTAL] ListDataModelHierarchies: List Custom Data Model hierarchies.
*CustomDataModelsApi* | [**list_supported_entity_types**](docs/CustomDataModelsApi.md#list_supported_entity_types) | **GET** /api/datamodel/entitytype | [EXPERIMENTAL] ListSupportedEntityTypes: List the currently supported entity types for use in Custom Data Models.
*CustomDataModelsApi* | [**update_custom_data_model**](docs/CustomDataModelsApi.md#update_custom_data_model) | **PUT** /api/datamodel/{entityType}/{scope}/{code} | [EXPERIMENTAL] UpdateCustomDataModel: Update a Custom Data Model
*CustomEntityTypesApi* | [**create_custom_entity_type**](docs/CustomEntityTypesApi.md#create_custom_entity_type) | **POST** /api/customentitytypes | [EARLY ACCESS] CreateCustomEntityType: Define a new Custom Entity Type.
*CustomEntityTypesApi* | [**get_custom_entity_type**](docs/CustomEntityTypesApi.md#get_custom_entity_type) | **GET** /api/customentitytypes/{entityType} | [EARLY ACCESS] GetCustomEntityType: Get a Custom Entity Type.
*CustomEntityTypesApi* | [**list_custom_entity_types**](docs/CustomEntityTypesApi.md#list_custom_entity_types) | **GET** /api/customentitytypes | [EARLY ACCESS] ListCustomEntityTypes: List Custom Entity Types.
*CustomEntityTypesApi* | [**update_custom_entity_type**](docs/CustomEntityTypesApi.md#update_custom_entity_type) | **PUT** /api/customentitytypes/{entityType} | [EARLY ACCESS] UpdateCustomEntityType: Modify an existing Custom Entity Type.
*CutLabelDefinitionsApi* | [**create_cut_label_definition**](docs/CutLabelDefinitionsApi.md#create_cut_label_definition) | **POST** /api/systemconfiguration/cutlabels | CreateCutLabelDefinition: Create a Cut Label
*CutLabelDefinitionsApi* | [**delete_cut_label_definition**](docs/CutLabelDefinitionsApi.md#delete_cut_label_definition) | **DELETE** /api/systemconfiguration/cutlabels/{code} | DeleteCutLabelDefinition: Delete a Cut Label
*CutLabelDefinitionsApi* | [**get_cut_label_definition**](docs/CutLabelDefinitionsApi.md#get_cut_label_definition) | **GET** /api/systemconfiguration/cutlabels/{code} | GetCutLabelDefinition: Get a Cut Label
*CutLabelDefinitionsApi* | [**list_cut_label_definitions**](docs/CutLabelDefinitionsApi.md#list_cut_label_definitions) | **GET** /api/systemconfiguration/cutlabels | ListCutLabelDefinitions: List Existing Cut Labels
*CutLabelDefinitionsApi* | [**update_cut_label_definition**](docs/CutLabelDefinitionsApi.md#update_cut_label_definition) | **PUT** /api/systemconfiguration/cutlabels/{code} | UpdateCutLabelDefinition: Update a Cut Label
*DataTypesApi* | [**create_data_type**](docs/DataTypesApi.md#create_data_type) | **POST** /api/datatypes | [EARLY ACCESS] CreateDataType: Create data type definition
*DataTypesApi* | [**delete_data_type**](docs/DataTypesApi.md#delete_data_type) | **DELETE** /api/datatypes/{scope}/{code} | DeleteDataType: Delete a data type definition.
*DataTypesApi* | [**get_data_type**](docs/DataTypesApi.md#get_data_type) | **GET** /api/datatypes/{scope}/{code} | GetDataType: Get data type definition
*DataTypesApi* | [**get_units_from_data_type**](docs/DataTypesApi.md#get_units_from_data_type) | **GET** /api/datatypes/{scope}/{code}/units | [EARLY ACCESS] GetUnitsFromDataType: Get units from data type
*DataTypesApi* | [**list_data_type_summaries**](docs/DataTypesApi.md#list_data_type_summaries) | **GET** /api/datatypes | [EARLY ACCESS] ListDataTypeSummaries: List all data type summaries, without the reference data
*DataTypesApi* | [**list_data_types**](docs/DataTypesApi.md#list_data_types) | **GET** /api/datatypes/{scope} | ListDataTypes: List data types
*DataTypesApi* | [**update_data_type**](docs/DataTypesApi.md#update_data_type) | **PUT** /api/datatypes/{scope}/{code} | [EARLY ACCESS] UpdateDataType: Update data type definition
*DataTypesApi* | [**update_reference_data**](docs/DataTypesApi.md#update_reference_data) | **PUT** /api/datatypes/{scope}/{code}/referencedata | [EARLY ACCESS] UpdateReferenceData: Update all reference data on a data type, includes the reference values, the field definitions, field values
*DataTypesApi* | [**update_reference_values**](docs/DataTypesApi.md#update_reference_values) | **PUT** /api/datatypes/{scope}/{code}/referencedatavalues | [EARLY ACCESS] UpdateReferenceValues: Update reference data on a data type
*DerivedTransactionPortfoliosApi* | [**create_derived_portfolio**](docs/DerivedTransactionPortfoliosApi.md#create_derived_portfolio) | **POST** /api/derivedtransactionportfolios/{scope} | CreateDerivedPortfolio: Create derived portfolio
*DerivedTransactionPortfoliosApi* | [**delete_derived_portfolio_details**](docs/DerivedTransactionPortfoliosApi.md#delete_derived_portfolio_details) | **DELETE** /api/derivedtransactionportfolios/{scope}/{code}/details | [EARLY ACCESS] DeleteDerivedPortfolioDetails: Delete derived portfolio details
*EntitiesApi* | [**get_custom_entity_by_entity_unique_id**](docs/EntitiesApi.md#get_custom_entity_by_entity_unique_id) | **GET** /api/entities/customentities/{entityUniqueId} | GetCustomEntityByEntityUniqueId: Get a Custom Entity instance by its EntityUniqueId
*EntitiesApi* | [**get_data_type_by_entity_unique_id**](docs/EntitiesApi.md#get_data_type_by_entity_unique_id) | **GET** /api/entities/datatypes/{entityUniqueId} | GetDataTypeByEntityUniqueId: Get DataType by EntityUniqueId
*EntitiesApi* | [**get_entity_history**](docs/EntitiesApi.md#get_entity_history) | **GET** /api/entities/{entityType}/{entityUniqueId}/history | GetEntityHistory: List an entity's history information
*EntitiesApi* | [**get_instrument_by_entity_unique_id**](docs/EntitiesApi.md#get_instrument_by_entity_unique_id) | **GET** /api/entities/instruments/{entityUniqueId} | GetInstrumentByEntityUniqueId: Get instrument by EntityUniqueId
*EntitiesApi* | [**get_portfolio_by_entity_unique_id**](docs/EntitiesApi.md#get_portfolio_by_entity_unique_id) | **GET** /api/entities/portfolios/{entityUniqueId} | GetPortfolioByEntityUniqueId: Get portfolio by EntityUniqueId
*EntitiesApi* | [**get_portfolio_changes**](docs/EntitiesApi.md#get_portfolio_changes) | **GET** /api/entities/changes/portfolios | GetPortfolioChanges: Get the next change to each portfolio in a scope.
*EntitiesApi* | [**get_property_definition_by_entity_unique_id**](docs/EntitiesApi.md#get_property_definition_by_entity_unique_id) | **GET** /api/entities/propertydefinitions/{entityUniqueId} | GetPropertyDefinitionByEntityUniqueId: Get property definition by EntityUniqueId
*ExecutionsApi* | [**delete_execution**](docs/ExecutionsApi.md#delete_execution) | **DELETE** /api/executions/{scope}/{code} | [EARLY ACCESS] DeleteExecution: Delete execution
*ExecutionsApi* | [**get_execution**](docs/ExecutionsApi.md#get_execution) | **GET** /api/executions/{scope}/{code} | [EARLY ACCESS] GetExecution: Get Execution
*ExecutionsApi* | [**list_executions**](docs/ExecutionsApi.md#list_executions) | **GET** /api/executions | ListExecutions: List Executions
*ExecutionsApi* | [**upsert_executions**](docs/ExecutionsApi.md#upsert_executions) | **POST** /api/executions | UpsertExecutions: Upsert Execution
*FeeTypesApi* | [**create_fee_type**](docs/FeeTypesApi.md#create_fee_type) | **POST** /api/feetypes/{scope} | [EXPERIMENTAL] CreateFeeType: Create a FeeType.
*FeeTypesApi* | [**delete_fee_type**](docs/FeeTypesApi.md#delete_fee_type) | **DELETE** /api/feetypes/{scope}/{code} | [EXPERIMENTAL] DeleteFeeType: Delete a FeeType.
*FeeTypesApi* | [**get_fee_template_specifications**](docs/FeeTypesApi.md#get_fee_template_specifications) | **GET** /api/feetypes/feetransactiontemplatespecification | [EXPERIMENTAL] GetFeeTemplateSpecifications: Get FeeTemplateSpecifications used in the FeeType.
*FeeTypesApi* | [**get_fee_type**](docs/FeeTypesApi.md#get_fee_type) | **GET** /api/feetypes/{scope}/{code} | [EXPERIMENTAL] GetFeeType: Get a FeeType
*FeeTypesApi* | [**list_fee_types**](docs/FeeTypesApi.md#list_fee_types) | **GET** /api/feetypes | [EXPERIMENTAL] ListFeeTypes: List FeeTypes
*FeeTypesApi* | [**update_fee_type**](docs/FeeTypesApi.md#update_fee_type) | **PUT** /api/feetypes/{scope}/{code} | [EXPERIMENTAL] UpdateFeeType: Update a FeeType.
*FundConfigurationApi* | [**create_fund_configuration**](docs/FundConfigurationApi.md#create_fund_configuration) | **POST** /api/fundconfigurations/{scope} | [EXPERIMENTAL] CreateFundConfiguration: Create a FundConfiguration.
*FundConfigurationApi* | [**delete_fund_configuration**](docs/FundConfigurationApi.md#delete_fund_configuration) | **DELETE** /api/fundconfigurations/{scope}/{code} | [EXPERIMENTAL] DeleteFundConfiguration: Delete a FundConfiguration.
*FundConfigurationApi* | [**get_fund_configuration**](docs/FundConfigurationApi.md#get_fund_configuration) | **GET** /api/fundconfigurations/{scope}/{code} | [EXPERIMENTAL] GetFundConfiguration: Get FundConfiguration.
*FundConfigurationApi* | [**list_fund_configurations**](docs/FundConfigurationApi.md#list_fund_configurations) | **GET** /api/fundconfigurations | [EXPERIMENTAL] ListFundConfigurations: List FundConfiguration.
*FundConfigurationApi* | [**patch_fund_configuration**](docs/FundConfigurationApi.md#patch_fund_configuration) | **PATCH** /api/fundconfigurations/{scope}/{code} | [EXPERIMENTAL] PatchFundConfiguration: Patch Fund Configuration.
*FundConfigurationApi* | [**upsert_fund_configuration_properties**](docs/FundConfigurationApi.md#upsert_fund_configuration_properties) | **POST** /api/fundconfigurations/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertFundConfigurationProperties: Upsert FundConfiguration properties
*FundsApi* | [**accept_estimate_valuation_point**](docs/FundsApi.md#accept_estimate_valuation_point) | **POST** /api/funds/{scope}/{code}/valuationpoints/$acceptestimate | [EXPERIMENTAL] AcceptEstimateValuationPoint: Accepts an Estimate Valuation Point.
*FundsApi* | [**create_fee**](docs/FundsApi.md#create_fee) | **POST** /api/funds/{scope}/{code}/fees | [EXPERIMENTAL] CreateFee: Create a Fee.
*FundsApi* | [**create_fund**](docs/FundsApi.md#create_fund) | **POST** /api/funds/{scope} | [EXPERIMENTAL] CreateFund: Create a Fund.
*FundsApi* | [**create_fund_v2**](docs/FundsApi.md#create_fund_v2) | **POST** /api/funds/v2/{scope} | [EXPERIMENTAL] CreateFundV2: Create a Fund V2 (Preview).
*FundsApi* | [**delete_bookmark**](docs/FundsApi.md#delete_bookmark) | **DELETE** /api/funds/{scope}/{code}/bookmarks/{bookmarkCode} | [EXPERIMENTAL] DeleteBookmark: Delete a Bookmark.
*FundsApi* | [**delete_fee**](docs/FundsApi.md#delete_fee) | **DELETE** /api/funds/{scope}/{code}/fees/{feeCode} | [EXPERIMENTAL] DeleteFee: Delete a Fee.
*FundsApi* | [**delete_fund**](docs/FundsApi.md#delete_fund) | **DELETE** /api/funds/{scope}/{code} | [EXPERIMENTAL] DeleteFund: Delete a Fund.
*FundsApi* | [**delete_nav_activity_adjustments**](docs/FundsApi.md#delete_nav_activity_adjustments) | **POST** /api/funds/{scope}/{code}/navAdjustment/$delete | [EXPERIMENTAL] DeleteNavActivityAdjustments: Delete Nav activity adjustments.
*FundsApi* | [**delete_valuation_point**](docs/FundsApi.md#delete_valuation_point) | **DELETE** /api/funds/{scope}/{code}/valuationpoints/{diaryEntryCode} | [EXPERIMENTAL] DeleteValuationPoint: Delete a Valuation Point.
*FundsApi* | [**finalise_candidate_valuation_point**](docs/FundsApi.md#finalise_candidate_valuation_point) | **POST** /api/funds/{scope}/{code}/valuationpoints/$finalisecandidate | [EXPERIMENTAL] FinaliseCandidateValuationPoint: Finalise a Candidate Valuation Point.
*FundsApi* | [**get_fee**](docs/FundsApi.md#get_fee) | **GET** /api/funds/{scope}/{code}/fees/{feeCode} | [EXPERIMENTAL] GetFee: Get a Fee for a specified Fund.
*FundsApi* | [**get_fee_properties**](docs/FundsApi.md#get_fee_properties) | **GET** /api/funds/{scope}/{code}/fees/{feeCode}/properties | [EXPERIMENTAL] GetFeeProperties: Get Fee properties.
*FundsApi* | [**get_fund**](docs/FundsApi.md#get_fund) | **GET** /api/funds/{scope}/{code} | [EXPERIMENTAL] GetFund: Get a Fund.
*FundsApi* | [**get_fund_properties**](docs/FundsApi.md#get_fund_properties) | **GET** /api/funds/{scope}/{code}/properties | [EXPERIMENTAL] GetFundProperties: Get Fund properties.
*FundsApi* | [**get_holdings_for_fund**](docs/FundsApi.md#get_holdings_for_fund) | **POST** /api/funds/{scope}/{code}/$holdings | [EXPERIMENTAL] GetHoldingsForFund: Get holdings for transaction portfolios in a Fund.
*FundsApi* | [**get_valuation_for_fund**](docs/FundsApi.md#get_valuation_for_fund) | **POST** /api/funds/{scope}/{code}/$valuation | [EXPERIMENTAL] GetValuationForFund: Perform valuation for a Fund.
*FundsApi* | [**get_valuation_point_data**](docs/FundsApi.md#get_valuation_point_data) | **POST** /api/funds/{scope}/{code}/valuationpoints/$query | [EXPERIMENTAL] GetValuationPointData: Get Valuation Point Data for a Fund.
*FundsApi* | [**get_valuation_point_journal_entry_lines**](docs/FundsApi.md#get_valuation_point_journal_entry_lines) | **POST** /api/funds/{scope}/{code}/valuationpoints/journalentrylines/$query | [EXPERIMENTAL] GetValuationPointJournalEntryLines: Get the Journal Entry Lines for the given Fund.
*FundsApi* | [**get_valuation_point_pnl_summary**](docs/FundsApi.md#get_valuation_point_pnl_summary) | **POST** /api/funds/{scope}/{code}/valuationpoints/pnlsummary/$query | [EXPERIMENTAL] GetValuationPointPnlSummary: Get a PnL summary for the given Valuation Point in the Fund.
*FundsApi* | [**get_valuation_point_transactions**](docs/FundsApi.md#get_valuation_point_transactions) | **POST** /api/funds/{scope}/{code}/valuationpoints/transactions/$query | [EXPERIMENTAL] GetValuationPointTransactions: Get the Transactions for the given Fund.
*FundsApi* | [**get_valuation_point_trial_balance**](docs/FundsApi.md#get_valuation_point_trial_balance) | **POST** /api/funds/{scope}/{code}/valuationpoints/trialbalance/$query | [EXPERIMENTAL] GetValuationPointTrialBalance: Get Trial Balance for the given Fund.
*FundsApi* | [**list_fees**](docs/FundsApi.md#list_fees) | **GET** /api/funds/{scope}/{code}/fees | [EXPERIMENTAL] ListFees: List Fees for a specified Fund.
*FundsApi* | [**list_fund_calendar**](docs/FundsApi.md#list_fund_calendar) | **GET** /api/funds/{scope}/{code}/calendar | [EXPERIMENTAL] ListFundCalendar: List Fund Calendar.
*FundsApi* | [**list_funds**](docs/FundsApi.md#list_funds) | **GET** /api/funds | [EXPERIMENTAL] ListFunds: List Funds.
*FundsApi* | [**list_nav_activity_adjustments**](docs/FundsApi.md#list_nav_activity_adjustments) | **GET** /api/funds/{scope}/{code}/navAdjustment | [EXPERIMENTAL] ListNavActivityAdjustments: List NAV adjustment activities applied to a valuation point
*FundsApi* | [**list_valuation_point_overview**](docs/FundsApi.md#list_valuation_point_overview) | **GET** /api/funds/{scope}/{code}/valuationPointOverview | [EXPERIMENTAL] ListValuationPointOverview: List Valuation Points Overview for a given Fund.
*FundsApi* | [**patch_fee**](docs/FundsApi.md#patch_fee) | **PATCH** /api/funds/{scope}/{code}/fees/{feeCode} | [EXPERIMENTAL] PatchFee: Patch Fee.
*FundsApi* | [**patch_fund**](docs/FundsApi.md#patch_fund) | **PATCH** /api/funds/{scope}/{code} | [EXPERIMENTAL] PatchFund: Patch a Fund.
*FundsApi* | [**revert_valuation_point_to_estimate**](docs/FundsApi.md#revert_valuation_point_to_estimate) | **POST** /api/funds/{scope}/{code}/valuationpoints/$reverttoestimate | [EXPERIMENTAL] RevertValuationPointToEstimate: Reverts a Final Valuation Point to Estimate.
*FundsApi* | [**set_share_class_instruments**](docs/FundsApi.md#set_share_class_instruments) | **PUT** /api/funds/{scope}/{code}/shareclasses | [EXPERIMENTAL] SetShareClassInstruments: Set the ShareClass Instruments on a Fund.
*FundsApi* | [**upsert_bookmark**](docs/FundsApi.md#upsert_bookmark) | **POST** /api/funds/{scope}/{code}/bookmarks | [EXPERIMENTAL] UpsertBookmark: Upsert a bookmark.
*FundsApi* | [**upsert_diary_entry_type_valuation_point**](docs/FundsApi.md#upsert_diary_entry_type_valuation_point) | **POST** /api/funds/{scope}/{code}/valuationpoints | [EXPERIMENTAL] UpsertDiaryEntryTypeValuationPoint: Upsert a Valuation Point.
*FundsApi* | [**upsert_fee_properties**](docs/FundsApi.md#upsert_fee_properties) | **POST** /api/funds/{scope}/{code}/fees/{feeCode}/properties/$upsert | [EXPERIMENTAL] UpsertFeeProperties: Upsert Fee properties.
*FundsApi* | [**upsert_fund_properties**](docs/FundsApi.md#upsert_fund_properties) | **POST** /api/funds/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertFundProperties: Upsert Fund properties.
*FundsApi* | [**upsert_nav_activity_adjustments**](docs/FundsApi.md#upsert_nav_activity_adjustments) | **POST** /api/funds/{scope}/{code}/navAdjustment | [EXPERIMENTAL] UpsertNavActivityAdjustments: Upsert NAV adjustment activities to a valuation point
*GroupReconciliationsApi* | [**batch_update_comparison_results**](docs/GroupReconciliationsApi.md#batch_update_comparison_results) | **POST** /api/reconciliations/groupreconciliationdefinitions/{scope}/{code}/comparisonresults/$batchReview | [EXPERIMENTAL] BatchUpdateComparisonResults: Add User Review entries for a range of comparison results related to a specific GroupReconciliationDefinition.
*GroupReconciliationsApi* | [**create_comparison_ruleset**](docs/GroupReconciliationsApi.md#create_comparison_ruleset) | **POST** /api/reconciliations/comparisonrulesets | [EXPERIMENTAL] CreateComparisonRuleset: Create a Group Reconciliation Comparison Ruleset
*GroupReconciliationsApi* | [**create_group_reconciliation_definition**](docs/GroupReconciliationsApi.md#create_group_reconciliation_definition) | **POST** /api/reconciliations/groupreconciliationdefinitions | [EXPERIMENTAL] CreateGroupReconciliationDefinition: Create Group Reconciliation Definition
*GroupReconciliationsApi* | [**delete_comparison_ruleset**](docs/GroupReconciliationsApi.md#delete_comparison_ruleset) | **DELETE** /api/reconciliations/comparisonrulesets/{scope}/{code} | [EXPERIMENTAL] DeleteComparisonRuleset: Deletes a particular Group Reconciliation Comparison Ruleset
*GroupReconciliationsApi* | [**delete_group_reconciliation_definition**](docs/GroupReconciliationsApi.md#delete_group_reconciliation_definition) | **DELETE** /api/reconciliations/groupreconciliationdefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteGroupReconciliationDefinition: Delete Group Reconciliation Definition
*GroupReconciliationsApi* | [**get_comparison_result**](docs/GroupReconciliationsApi.md#get_comparison_result) | **GET** /api/reconciliations/groupreconciliationdefinitions/{scope}/{code}/{resultId} | [EXPERIMENTAL] GetComparisonResult: Get a single Group Reconciliation Comparison Result by scope and code.
*GroupReconciliationsApi* | [**get_comparison_ruleset**](docs/GroupReconciliationsApi.md#get_comparison_ruleset) | **GET** /api/reconciliations/comparisonrulesets/{scope}/{code} | [EXPERIMENTAL] GetComparisonRuleset: Get a single Group Reconciliation Comparison Ruleset by scope and code.
*GroupReconciliationsApi* | [**get_group_reconciliation_definition**](docs/GroupReconciliationsApi.md#get_group_reconciliation_definition) | **GET** /api/reconciliations/groupreconciliationdefinitions/{scope}/{code} | [EXPERIMENTAL] GetGroupReconciliationDefinition: Get group reconciliation definition
*GroupReconciliationsApi* | [**list_comparison_results**](docs/GroupReconciliationsApi.md#list_comparison_results) | **GET** /api/reconciliations/comparisonresults | [EXPERIMENTAL] ListComparisonResults: Get a set of Group Reconciliation Comparison Results.
*GroupReconciliationsApi* | [**list_comparison_rulesets**](docs/GroupReconciliationsApi.md#list_comparison_rulesets) | **GET** /api/reconciliations/comparisonrulesets | [EXPERIMENTAL] ListComparisonRulesets: Get a set of Group Reconciliation Comparison Rulesets
*GroupReconciliationsApi* | [**list_group_reconciliation_definitions**](docs/GroupReconciliationsApi.md#list_group_reconciliation_definitions) | **GET** /api/reconciliations/groupreconciliationdefinitions | [EXPERIMENTAL] ListGroupReconciliationDefinitions: List group reconciliation definitions
*GroupReconciliationsApi* | [**run_reconciliation**](docs/GroupReconciliationsApi.md#run_reconciliation) | **POST** /api/reconciliations/groupreconciliationdefinitions/{scope}/{code}/$run | [EXPERIMENTAL] RunReconciliation: Runs a Group Reconciliation
*GroupReconciliationsApi* | [**update_comparison_ruleset**](docs/GroupReconciliationsApi.md#update_comparison_ruleset) | **PUT** /api/reconciliations/comparisonrulesets/{scope}/{code} | [EXPERIMENTAL] UpdateComparisonRuleset: Update Group Reconciliation Comparison Ruleset defined by scope and code
*GroupReconciliationsApi* | [**update_group_reconciliation_definition**](docs/GroupReconciliationsApi.md#update_group_reconciliation_definition) | **PUT** /api/reconciliations/groupreconciliationdefinitions/{scope}/{code} | [EXPERIMENTAL] UpdateGroupReconciliationDefinition: Update group reconciliation definition
*IdentifierDefinitionsApi* | [**create_identifier_definition**](docs/IdentifierDefinitionsApi.md#create_identifier_definition) | **POST** /api/identifierdefinitions | [EXPERIMENTAL] CreateIdentifierDefinition: Create an Identifier Definition
*IdentifierDefinitionsApi* | [**delete_identifier_definition**](docs/IdentifierDefinitionsApi.md#delete_identifier_definition) | **DELETE** /api/identifierdefinitions/{domain}/{identifierScope}/{identifierType} | [EXPERIMENTAL] DeleteIdentifierDefinition: Delete a particular Identifier Definition
*IdentifierDefinitionsApi* | [**get_identifier_definition**](docs/IdentifierDefinitionsApi.md#get_identifier_definition) | **GET** /api/identifierdefinitions/{domain}/{identifierScope}/{identifierType} | [EXPERIMENTAL] GetIdentifierDefinition: Get a single Identifier Definition
*IdentifierDefinitionsApi* | [**list_identifier_definitions**](docs/IdentifierDefinitionsApi.md#list_identifier_definitions) | **GET** /api/identifierdefinitions | [EXPERIMENTAL] ListIdentifierDefinitions: List Identifier Definitions
*IdentifierDefinitionsApi* | [**update_identifier_definition**](docs/IdentifierDefinitionsApi.md#update_identifier_definition) | **PUT** /api/identifierdefinitions/{domain}/{identifierScope}/{identifierType} | [EXPERIMENTAL] UpdateIdentifierDefinition: Update Identifier Definition defined by domain, identifierScope, and identifierType
*InstrumentEventTypesApi* | [**create_transaction_template**](docs/InstrumentEventTypesApi.md#create_transaction_template) | **POST** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | CreateTransactionTemplate: Create Transaction Template
*InstrumentEventTypesApi* | [**delete_transaction_template**](docs/InstrumentEventTypesApi.md#delete_transaction_template) | **DELETE** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | DeleteTransactionTemplate: Delete Transaction Template
*InstrumentEventTypesApi* | [**get_transaction_template**](docs/InstrumentEventTypesApi.md#get_transaction_template) | **GET** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | GetTransactionTemplate: Get Transaction Template
*InstrumentEventTypesApi* | [**get_transaction_template_specification**](docs/InstrumentEventTypesApi.md#get_transaction_template_specification) | **GET** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplatespecification | GetTransactionTemplateSpecification: Get Transaction Template Specification.
*InstrumentEventTypesApi* | [**list_transaction_template_specifications**](docs/InstrumentEventTypesApi.md#list_transaction_template_specifications) | **GET** /api/instrumenteventtypes/transactiontemplatespecifications | ListTransactionTemplateSpecifications: List Transaction Template Specifications.
*InstrumentEventTypesApi* | [**list_transaction_templates**](docs/InstrumentEventTypesApi.md#list_transaction_templates) | **GET** /api/instrumenteventtypes/transactiontemplates | ListTransactionTemplates: List Transaction Templates
*InstrumentEventTypesApi* | [**update_transaction_template**](docs/InstrumentEventTypesApi.md#update_transaction_template) | **PUT** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | UpdateTransactionTemplate: Update Transaction Template
*InstrumentEventsApi* | [**query_applicable_instrument_events**](docs/InstrumentEventsApi.md#query_applicable_instrument_events) | **POST** /api/instrumentevents/$queryApplicableInstrumentEvents | QueryApplicableInstrumentEvents: Returns a list of applicable instrument events based on the holdings of the portfolios and date range specified in the query.
*InstrumentEventsApi* | [**query_bucketed_cash_flows**](docs/InstrumentEventsApi.md#query_bucketed_cash_flows) | **POST** /api/instrumentevents/$queryBucketedCashFlows | QueryBucketedCashFlows: Returns bucketed cashflows based on the holdings of the portfolios and date range specified in the query.
*InstrumentEventsApi* | [**query_cash_flows**](docs/InstrumentEventsApi.md#query_cash_flows) | **POST** /api/instrumentevents/$queryCashFlows | QueryCashFlows: Returns a list of cashflows based on the holdings of the portfolios and date range specified in the query.
*InstrumentEventsApi* | [**query_instrument_events**](docs/InstrumentEventsApi.md#query_instrument_events) | **POST** /api/instrumentevents/$query | QueryInstrumentEvents: Returns a list of instrument events based on the holdings of the portfolios and date range specified in the query.
*InstrumentEventsApi* | [**query_trade_tickets**](docs/InstrumentEventsApi.md#query_trade_tickets) | **POST** /api/instrumentevents/$queryTradeTickets | QueryTradeTickets: Returns a list of trade tickets based on the holdings of the portfolios and date range specified in the query.
*InstrumentsApi* | [**batch_upsert_instrument_properties**](docs/InstrumentsApi.md#batch_upsert_instrument_properties) | **POST** /api/instruments/$batchupsertproperties | BatchUpsertInstrumentProperties: Batch upsert instruments properties
*InstrumentsApi* | [**calculate_settlement_date**](docs/InstrumentsApi.md#calculate_settlement_date) | **GET** /api/instruments/{identifierType}/{identifier}/settlementdate | CalculateSettlementDate: Get the settlement date for an instrument.
*InstrumentsApi* | [**delete_instrument**](docs/InstrumentsApi.md#delete_instrument) | **DELETE** /api/instruments/{identifierType}/{identifier} | DeleteInstrument: Soft delete a single instrument
*InstrumentsApi* | [**delete_instrument_properties**](docs/InstrumentsApi.md#delete_instrument_properties) | **POST** /api/instruments/{identifierType}/{identifier}/properties/$delete | DeleteInstrumentProperties: Delete instrument properties
*InstrumentsApi* | [**delete_instruments**](docs/InstrumentsApi.md#delete_instruments) | **POST** /api/instruments/$delete | DeleteInstruments: Soft or hard delete multiple instruments
*InstrumentsApi* | [**get_all_possible_features**](docs/InstrumentsApi.md#get_all_possible_features) | **GET** /api/instruments/{instrumentType}/allfeatures | GetAllPossibleFeatures: Provides list of all possible features for instrument type.
*InstrumentsApi* | [**get_existing_instrument_capabilities**](docs/InstrumentsApi.md#get_existing_instrument_capabilities) | **GET** /api/instruments/{identifier}/capabilities | GetExistingInstrumentCapabilities: Retrieve capabilities of an existing instrument identified by LUID. These include instrument features, and if model is provided it also includes supported address keys and economic dependencies.  Given an lusid instrument id provides instrument capabilities, outlining features, and, given the model, the capabilities also include supported addresses as well as economic dependencies.
*InstrumentsApi* | [**get_existing_instrument_models**](docs/InstrumentsApi.md#get_existing_instrument_models) | **GET** /api/instruments/{identifier}/models | GetExistingInstrumentModels: Retrieve supported pricing models for an existing instrument identified by LUID.
*InstrumentsApi* | [**get_instrument**](docs/InstrumentsApi.md#get_instrument) | **GET** /api/instruments/{identifierType}/{identifier} | GetInstrument: Get instrument
*InstrumentsApi* | [**get_instrument_identifier_types**](docs/InstrumentsApi.md#get_instrument_identifier_types) | **GET** /api/instruments/identifierTypes | GetInstrumentIdentifierTypes: Get instrument identifier types
*InstrumentsApi* | [**get_instrument_payment_diary**](docs/InstrumentsApi.md#get_instrument_payment_diary) | **GET** /api/instruments/{identifierType}/{identifier}/paymentdiary | GetInstrumentPaymentDiary: Get instrument payment diary
*InstrumentsApi* | [**get_instrument_properties**](docs/InstrumentsApi.md#get_instrument_properties) | **GET** /api/instruments/{identifierType}/{identifier}/properties | GetInstrumentProperties: Get instrument properties
*InstrumentsApi* | [**get_instrument_property_time_series**](docs/InstrumentsApi.md#get_instrument_property_time_series) | **GET** /api/instruments/{identifierType}/{identifier}/properties/time-series | GetInstrumentPropertyTimeSeries: Get instrument property time series
*InstrumentsApi* | [**get_instrument_relationships**](docs/InstrumentsApi.md#get_instrument_relationships) | **GET** /api/instruments/{identifierType}/{identifier}/relationships | GetInstrumentRelationships: Get Instrument relationships
*InstrumentsApi* | [**get_instruments**](docs/InstrumentsApi.md#get_instruments) | **POST** /api/instruments/$get | GetInstruments: Get instruments
*InstrumentsApi* | [**list_instrument_properties**](docs/InstrumentsApi.md#list_instrument_properties) | **GET** /api/instruments/{identifierType}/{identifier}/properties/list | ListInstrumentProperties: Get instrument properties (with Pagination)
*InstrumentsApi* | [**list_instruments**](docs/InstrumentsApi.md#list_instruments) | **GET** /api/instruments | ListInstruments: List instruments
*InstrumentsApi* | [**query_instrument_capabilities**](docs/InstrumentsApi.md#query_instrument_capabilities) | **POST** /api/instruments/capabilities | QueryInstrumentCapabilities: Query capabilities of a particular instrument in advance of creating it. These include instrument features, and if model is provided it also includes supported address keys and economic dependencies.
*InstrumentsApi* | [**update_instrument_identifier**](docs/InstrumentsApi.md#update_instrument_identifier) | **POST** /api/instruments/{identifierType}/{identifier} | UpdateInstrumentIdentifier: Update instrument identifier
*InstrumentsApi* | [**upsert_instruments**](docs/InstrumentsApi.md#upsert_instruments) | **POST** /api/instruments | UpsertInstruments: Upsert instruments
*InstrumentsApi* | [**upsert_instruments_properties**](docs/InstrumentsApi.md#upsert_instruments_properties) | **POST** /api/instruments/$upsertproperties | UpsertInstrumentsProperties: Upsert instruments properties
*InvestmentAccountsApi* | [**delete_investment_account**](docs/InvestmentAccountsApi.md#delete_investment_account) | **DELETE** /api/investmentaccounts/{identifierType}/{identifierValue} | [EXPERIMENTAL] DeleteInvestmentAccount: Delete Investment Account
*InvestmentAccountsApi* | [**get_investment_account**](docs/InvestmentAccountsApi.md#get_investment_account) | **GET** /api/investmentaccounts/{identifierType}/{identifierValue} | [EXPERIMENTAL] GetInvestmentAccount: Get Investment Account
*InvestmentAccountsApi* | [**list_all_investment_accounts**](docs/InvestmentAccountsApi.md#list_all_investment_accounts) | **GET** /api/investmentaccounts | [EXPERIMENTAL] ListAllInvestmentAccounts: List Investment Accounts
*InvestmentAccountsApi* | [**upsert_investment_accounts**](docs/InvestmentAccountsApi.md#upsert_investment_accounts) | **POST** /api/investmentaccounts/$batchUpsert | [EXPERIMENTAL] UpsertInvestmentAccounts: Upsert Investment Accounts
*InvestorRecordsApi* | [**delete_investor_record**](docs/InvestorRecordsApi.md#delete_investor_record) | **DELETE** /api/investorrecords/{identifierType}/{identifierValue} | [EARLY ACCESS] DeleteInvestorRecord: Delete Investor Record
*InvestorRecordsApi* | [**get_investor_record**](docs/InvestorRecordsApi.md#get_investor_record) | **GET** /api/investorrecords/{identifierType}/{identifierValue} | [EARLY ACCESS] GetInvestorRecord: Get Investor Record
*InvestorRecordsApi* | [**list_all_investor_records**](docs/InvestorRecordsApi.md#list_all_investor_records) | **GET** /api/investorrecords | [EARLY ACCESS] ListAllInvestorRecords: List Investor Records
*InvestorRecordsApi* | [**upsert_investor_records**](docs/InvestorRecordsApi.md#upsert_investor_records) | **POST** /api/investorrecords/$batchUpsert | [EARLY ACCESS] UpsertInvestorRecords: Upsert investor records
*LegacyComplianceApi* | [**delete_legacy_compliance_rule**](docs/LegacyComplianceApi.md#delete_legacy_compliance_rule) | **DELETE** /api/legacy/compliance/rules/{scope}/{code} | [EXPERIMENTAL] DeleteLegacyComplianceRule: Deletes a compliance rule.
*LegacyComplianceApi* | [**get_legacy_breached_orders_info**](docs/LegacyComplianceApi.md#get_legacy_breached_orders_info) | **GET** /api/legacy/compliance/runs/breached/{runId} | [EXPERIMENTAL] GetLegacyBreachedOrdersInfo: Get the Ids of Breached orders in a given compliance run and the corresponding list of rules that could have caused it.
*LegacyComplianceApi* | [**get_legacy_compliance_rule**](docs/LegacyComplianceApi.md#get_legacy_compliance_rule) | **GET** /api/legacy/compliance/rules/{scope}/{code} | [EXPERIMENTAL] GetLegacyComplianceRule: Retrieve the definition of single compliance rule.
*LegacyComplianceApi* | [**get_legacy_compliance_run_results**](docs/LegacyComplianceApi.md#get_legacy_compliance_run_results) | **GET** /api/legacy/compliance/runs/{runId} | [EXPERIMENTAL] GetLegacyComplianceRunResults: Get the details of a single compliance run.
*LegacyComplianceApi* | [**list_legacy_compliance_rules**](docs/LegacyComplianceApi.md#list_legacy_compliance_rules) | **GET** /api/legacy/compliance/rules | [EXPERIMENTAL] ListLegacyComplianceRules: List compliance rules, with optional filtering.
*LegacyComplianceApi* | [**list_legacy_compliance_run_info**](docs/LegacyComplianceApi.md#list_legacy_compliance_run_info) | **GET** /api/legacy/compliance/runs | [EXPERIMENTAL] ListLegacyComplianceRunInfo: List historical compliance run ids.
*LegacyComplianceApi* | [**run_legacy_compliance**](docs/LegacyComplianceApi.md#run_legacy_compliance) | **POST** /api/legacy/compliance/runs | [EXPERIMENTAL] RunLegacyCompliance: Kick off the compliance check process
*LegacyComplianceApi* | [**upsert_legacy_compliance_rules**](docs/LegacyComplianceApi.md#upsert_legacy_compliance_rules) | **POST** /api/legacy/compliance/rules | [EXPERIMENTAL] UpsertLegacyComplianceRules: Upsert compliance rules.
*LegalEntitiesApi* | [**delete_legal_entity**](docs/LegalEntitiesApi.md#delete_legal_entity) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code} | DeleteLegalEntity: Delete Legal Entity
*LegalEntitiesApi* | [**delete_legal_entity_access_metadata**](docs/LegalEntitiesApi.md#delete_legal_entity_access_metadata) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | DeleteLegalEntityAccessMetadata: Delete a Legal Entity Access Metadata entry
*LegalEntitiesApi* | [**delete_legal_entity_identifiers**](docs/LegalEntitiesApi.md#delete_legal_entity_identifiers) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EARLY ACCESS] DeleteLegalEntityIdentifiers: Delete Legal Entity Identifiers
*LegalEntitiesApi* | [**delete_legal_entity_properties**](docs/LegalEntitiesApi.md#delete_legal_entity_properties) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/properties | [EARLY ACCESS] DeleteLegalEntityProperties: Delete Legal Entity Properties
*LegalEntitiesApi* | [**get_all_legal_entity_access_metadata**](docs/LegalEntitiesApi.md#get_all_legal_entity_access_metadata) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata | GetAllLegalEntityAccessMetadata: Get Access Metadata rules for a Legal Entity
*LegalEntitiesApi* | [**get_legal_entity**](docs/LegalEntitiesApi.md#get_legal_entity) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code} | GetLegalEntity: Get Legal Entity
*LegalEntitiesApi* | [**get_legal_entity_access_metadata_by_key**](docs/LegalEntitiesApi.md#get_legal_entity_access_metadata_by_key) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetLegalEntityAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Legal Entity
*LegalEntitiesApi* | [**get_legal_entity_property_time_series**](docs/LegalEntitiesApi.md#get_legal_entity_property_time_series) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/properties/time-series | GetLegalEntityPropertyTimeSeries: Get Legal Entity Property Time Series
*LegalEntitiesApi* | [**get_legal_entity_relations**](docs/LegalEntitiesApi.md#get_legal_entity_relations) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/relations | GetLegalEntityRelations: Get Relations for Legal Entity
*LegalEntitiesApi* | [**get_legal_entity_relationships**](docs/LegalEntitiesApi.md#get_legal_entity_relationships) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/relationships | GetLegalEntityRelationships: Get Relationships for Legal Entity
*LegalEntitiesApi* | [**list_all_legal_entities**](docs/LegalEntitiesApi.md#list_all_legal_entities) | **GET** /api/legalentities | ListAllLegalEntities: List Legal Entities
*LegalEntitiesApi* | [**list_legal_entities**](docs/LegalEntitiesApi.md#list_legal_entities) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode} | ListLegalEntities: List Legal Entities
*LegalEntitiesApi* | [**patch_legal_entity_access_metadata**](docs/LegalEntitiesApi.md#patch_legal_entity_access_metadata) | **PATCH** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata | [EARLY ACCESS] PatchLegalEntityAccessMetadata: Patch Access Metadata rules for a Legal Entity.
*LegalEntitiesApi* | [**set_legal_entity_identifiers**](docs/LegalEntitiesApi.md#set_legal_entity_identifiers) | **POST** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EARLY ACCESS] SetLegalEntityIdentifiers: Set Legal Entity Identifiers
*LegalEntitiesApi* | [**set_legal_entity_properties**](docs/LegalEntitiesApi.md#set_legal_entity_properties) | **POST** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/properties | SetLegalEntityProperties: Set Legal Entity Properties
*LegalEntitiesApi* | [**upsert_legal_entities**](docs/LegalEntitiesApi.md#upsert_legal_entities) | **POST** /api/legalentities/$batchUpsert | [EARLY ACCESS] UpsertLegalEntities: Batch upsert Legal Entities
*LegalEntitiesApi* | [**upsert_legal_entity**](docs/LegalEntitiesApi.md#upsert_legal_entity) | **POST** /api/legalentities | UpsertLegalEntity: Upsert Legal Entity
*LegalEntitiesApi* | [**upsert_legal_entity_access_metadata**](docs/LegalEntitiesApi.md#upsert_legal_entity_access_metadata) | **PUT** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | UpsertLegalEntityAccessMetadata: Upsert a Legal Entity Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
*OrderGraphApi* | [**list_order_graph_blocks**](docs/OrderGraphApi.md#list_order_graph_blocks) | **GET** /api/ordergraph/blocks | ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.
*OrderGraphApi* | [**list_order_graph_placement_children**](docs/OrderGraphApi.md#list_order_graph_placement_children) | **GET** /api/ordergraph/placementchildren/{scope}/{code} | [EARLY ACCESS] ListOrderGraphPlacementChildren: Lists all placements for the parent placement specified by the scope and code, and builds a summary picture of the state of their associated order entities.
*OrderGraphApi* | [**list_order_graph_placements**](docs/OrderGraphApi.md#list_order_graph_placements) | **GET** /api/ordergraph/placements | ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.
*OrderInstructionsApi* | [**delete_order_instruction**](docs/OrderInstructionsApi.md#delete_order_instruction) | **DELETE** /api/orderinstructions/{scope}/{code} | DeleteOrderInstruction: Delete orderInstruction
*OrderInstructionsApi* | [**get_order_instruction**](docs/OrderInstructionsApi.md#get_order_instruction) | **GET** /api/orderinstructions/{scope}/{code} | GetOrderInstruction: Get OrderInstruction
*OrderInstructionsApi* | [**list_order_instructions**](docs/OrderInstructionsApi.md#list_order_instructions) | **GET** /api/orderinstructions | ListOrderInstructions: List OrderInstructions
*OrderInstructionsApi* | [**upsert_order_instructions**](docs/OrderInstructionsApi.md#upsert_order_instructions) | **POST** /api/orderinstructions | UpsertOrderInstructions: Upsert OrderInstruction
*OrderManagementApi* | [**book_transactions**](docs/OrderManagementApi.md#book_transactions) | **POST** /api/ordermanagement/booktransactions | BookTransactions: Books transactions using specific allocations as a source.
*OrderManagementApi* | [**cancel_orders**](docs/OrderManagementApi.md#cancel_orders) | **POST** /api/ordermanagement/cancelorders | [EARLY ACCESS] CancelOrders: Cancel existing orders
*OrderManagementApi* | [**cancel_orders_and_move_remaining**](docs/OrderManagementApi.md#cancel_orders_and_move_remaining) | **POST** /api/ordermanagement/cancelordersandmoveremaining | [EARLY ACCESS] CancelOrdersAndMoveRemaining: Cancel existing orders and move any unplaced quantities to new orders in new blocks
*OrderManagementApi* | [**cancel_placements**](docs/OrderManagementApi.md#cancel_placements) | **POST** /api/ordermanagement/$cancelplacements | [EARLY ACCESS] CancelPlacements: Cancel existing placements
*OrderManagementApi* | [**create_orders**](docs/OrderManagementApi.md#create_orders) | **POST** /api/ordermanagement/createorders | CreateOrders: Upsert a Block and associated orders
*OrderManagementApi* | [**get_order_history**](docs/OrderManagementApi.md#get_order_history) | **GET** /api/ordermanagement/order/{scope}/{code}/$history | GetOrderHistory: Get the history of an order and related entity changes
*OrderManagementApi* | [**move_orders**](docs/OrderManagementApi.md#move_orders) | **POST** /api/ordermanagement/moveorders | [EARLY ACCESS] MoveOrders: Move orders to new or existing block
*OrderManagementApi* | [**place_blocks**](docs/OrderManagementApi.md#place_blocks) | **POST** /api/ordermanagement/placeblocks | [EARLY ACCESS] PlaceBlocks: Places blocks for a given list of placement requests.
*OrderManagementApi* | [**run_allocation_service**](docs/OrderManagementApi.md#run_allocation_service) | **POST** /api/ordermanagement/allocate | RunAllocationService: Runs the Allocation Service
*OrderManagementApi* | [**sweep_blocks**](docs/OrderManagementApi.md#sweep_blocks) | **POST** /api/ordermanagement/SweepBlocks | [EXPERIMENTAL] SweepBlocks: Sweeps specified blocks, for each block that meets the requirements. The request may be partially successful.
*OrderManagementApi* | [**update_orders**](docs/OrderManagementApi.md#update_orders) | **POST** /api/ordermanagement/updateorders | [EARLY ACCESS] UpdateOrders: Update existing orders
*OrderManagementApi* | [**update_placements**](docs/OrderManagementApi.md#update_placements) | **POST** /api/ordermanagement/$updateplacements | [EARLY ACCESS] UpdatePlacements: Update existing placements
*OrdersApi* | [**delete_order**](docs/OrdersApi.md#delete_order) | **DELETE** /api/orders/{scope}/{code} | [EARLY ACCESS] DeleteOrder: Delete order
*OrdersApi* | [**get_order**](docs/OrdersApi.md#get_order) | **GET** /api/orders/{scope}/{code} | [EARLY ACCESS] GetOrder: Get Order
*OrdersApi* | [**list_orders**](docs/OrdersApi.md#list_orders) | **GET** /api/orders | ListOrders: List Orders
*OrdersApi* | [**upsert_orders**](docs/OrdersApi.md#upsert_orders) | **POST** /api/orders | UpsertOrders: Upsert Order
*PackagesApi* | [**delete_package**](docs/PackagesApi.md#delete_package) | **DELETE** /api/packages/{scope}/{code} | [EXPERIMENTAL] DeletePackage: Delete package
*PackagesApi* | [**get_package**](docs/PackagesApi.md#get_package) | **GET** /api/packages/{scope}/{code} | [EXPERIMENTAL] GetPackage: Get Package
*PackagesApi* | [**list_packages**](docs/PackagesApi.md#list_packages) | **GET** /api/packages | [EXPERIMENTAL] ListPackages: List Packages
*PackagesApi* | [**upsert_packages**](docs/PackagesApi.md#upsert_packages) | **POST** /api/packages | [EXPERIMENTAL] UpsertPackages: Upsert Package
*ParticipationsApi* | [**delete_participation**](docs/ParticipationsApi.md#delete_participation) | **DELETE** /api/participations/{scope}/{code} | [EARLY ACCESS] DeleteParticipation: Delete participation
*ParticipationsApi* | [**get_participation**](docs/ParticipationsApi.md#get_participation) | **GET** /api/participations/{scope}/{code} | [EARLY ACCESS] GetParticipation: Get Participation
*ParticipationsApi* | [**list_participations**](docs/ParticipationsApi.md#list_participations) | **GET** /api/participations | [EARLY ACCESS] ListParticipations: List Participations
*ParticipationsApi* | [**upsert_participations**](docs/ParticipationsApi.md#upsert_participations) | **POST** /api/participations | [EARLY ACCESS] UpsertParticipations: Upsert Participation
*PersonsApi* | [**delete_person**](docs/PersonsApi.md#delete_person) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code} | DeletePerson: Delete person
*PersonsApi* | [**delete_person_access_metadata**](docs/PersonsApi.md#delete_person_access_metadata) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeletePersonAccessMetadata: Delete a Person Access Metadata entry
*PersonsApi* | [**delete_person_identifiers**](docs/PersonsApi.md#delete_person_identifiers) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EARLY ACCESS] DeletePersonIdentifiers: Delete Person Identifiers
*PersonsApi* | [**delete_person_properties**](docs/PersonsApi.md#delete_person_properties) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties | [EARLY ACCESS] DeletePersonProperties: Delete Person Properties
*PersonsApi* | [**get_all_person_access_metadata**](docs/PersonsApi.md#get_all_person_access_metadata) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata | [EARLY ACCESS] GetAllPersonAccessMetadata: Get Access Metadata rules for a Person
*PersonsApi* | [**get_person**](docs/PersonsApi.md#get_person) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code} | [EARLY ACCESS] GetPerson: Get Person
*PersonsApi* | [**get_person_access_metadata_by_key**](docs/PersonsApi.md#get_person_access_metadata_by_key) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPersonAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Person
*PersonsApi* | [**get_person_property_time_series**](docs/PersonsApi.md#get_person_property_time_series) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties/time-series | [EARLY ACCESS] GetPersonPropertyTimeSeries: Get Person Property Time Series
*PersonsApi* | [**get_person_relations**](docs/PersonsApi.md#get_person_relations) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/relations | [EARLY ACCESS] GetPersonRelations: Get Relations for Person
*PersonsApi* | [**get_person_relationships**](docs/PersonsApi.md#get_person_relationships) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/relationships | [EARLY ACCESS] GetPersonRelationships: Get Relationships for Person
*PersonsApi* | [**list_all_persons**](docs/PersonsApi.md#list_all_persons) | **GET** /api/persons | [EARLY ACCESS] ListAllPersons: List All Persons
*PersonsApi* | [**list_persons**](docs/PersonsApi.md#list_persons) | **GET** /api/persons/{idTypeScope}/{idTypeCode} | [EARLY ACCESS] ListPersons: List Persons
*PersonsApi* | [**patch_person_access_metadata**](docs/PersonsApi.md#patch_person_access_metadata) | **PATCH** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata | [EARLY ACCESS] PatchPersonAccessMetadata: Patch Access Metadata rules for a Person.
*PersonsApi* | [**set_person_identifiers**](docs/PersonsApi.md#set_person_identifiers) | **POST** /api/persons/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EARLY ACCESS] SetPersonIdentifiers: Set Person Identifiers
*PersonsApi* | [**set_person_properties**](docs/PersonsApi.md#set_person_properties) | **POST** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties | [EARLY ACCESS] SetPersonProperties: Set Person Properties
*PersonsApi* | [**upsert_person**](docs/PersonsApi.md#upsert_person) | **POST** /api/persons | UpsertPerson: Upsert Person
*PersonsApi* | [**upsert_person_access_metadata**](docs/PersonsApi.md#upsert_person_access_metadata) | **PUT** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] UpsertPersonAccessMetadata: Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
*PersonsApi* | [**upsert_persons**](docs/PersonsApi.md#upsert_persons) | **POST** /api/persons/$batchUpsert | [EARLY ACCESS] UpsertPersons: Batch upsert Persons
*PlacementsApi* | [**delete_placement**](docs/PlacementsApi.md#delete_placement) | **DELETE** /api/placements/{scope}/{code} | [EARLY ACCESS] DeletePlacement: Delete placement
*PlacementsApi* | [**get_placement**](docs/PlacementsApi.md#get_placement) | **GET** /api/placements/{scope}/{code} | [EARLY ACCESS] GetPlacement: Get Placement
*PlacementsApi* | [**list_placements**](docs/PlacementsApi.md#list_placements) | **GET** /api/placements | [EARLY ACCESS] ListPlacements: List Placements
*PlacementsApi* | [**upsert_placements**](docs/PlacementsApi.md#upsert_placements) | **POST** /api/placements | [EARLY ACCESS] UpsertPlacements: Upsert Placement
*PortfolioGroupsApi* | [**add_portfolio_to_group**](docs/PortfolioGroupsApi.md#add_portfolio_to_group) | **POST** /api/portfoliogroups/{scope}/{code}/portfolios | [EARLY ACCESS] AddPortfolioToGroup: Add portfolio to group
*PortfolioGroupsApi* | [**add_sub_group_to_group**](docs/PortfolioGroupsApi.md#add_sub_group_to_group) | **POST** /api/portfoliogroups/{scope}/{code}/subgroups | [EARLY ACCESS] AddSubGroupToGroup: Add sub group to group
*PortfolioGroupsApi* | [**build_transactions_for_portfolio_group**](docs/PortfolioGroupsApi.md#build_transactions_for_portfolio_group) | **POST** /api/portfoliogroups/{scope}/{code}/transactions/$build | BuildTransactionsForPortfolioGroup: Build transactions for transaction portfolios in a portfolio group
*PortfolioGroupsApi* | [**create_portfolio_group**](docs/PortfolioGroupsApi.md#create_portfolio_group) | **POST** /api/portfoliogroups/{scope} | CreatePortfolioGroup: Create portfolio group
*PortfolioGroupsApi* | [**delete_group_properties**](docs/PortfolioGroupsApi.md#delete_group_properties) | **POST** /api/portfoliogroups/{scope}/{code}/properties/$delete | [EARLY ACCESS] DeleteGroupProperties: Delete group properties
*PortfolioGroupsApi* | [**delete_key_from_portfolio_group_access_metadata**](docs/PortfolioGroupsApi.md#delete_key_from_portfolio_group_access_metadata) | **DELETE** /api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeleteKeyFromPortfolioGroupAccessMetadata: Delete a Portfolio Group Access Metadata entry
*PortfolioGroupsApi* | [**delete_portfolio_from_group**](docs/PortfolioGroupsApi.md#delete_portfolio_from_group) | **DELETE** /api/portfoliogroups/{scope}/{code}/portfolios/{portfolioScope}/{portfolioCode} | [EARLY ACCESS] DeletePortfolioFromGroup: Delete portfolio from group
*PortfolioGroupsApi* | [**delete_portfolio_group**](docs/PortfolioGroupsApi.md#delete_portfolio_group) | **DELETE** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] DeletePortfolioGroup: Delete portfolio group
*PortfolioGroupsApi* | [**delete_sub_group_from_group**](docs/PortfolioGroupsApi.md#delete_sub_group_from_group) | **DELETE** /api/portfoliogroups/{scope}/{code}/subgroups/{subgroupScope}/{subgroupCode} | [EARLY ACCESS] DeleteSubGroupFromGroup: Delete sub group from group
*PortfolioGroupsApi* | [**get_a2_b_data_for_portfolio_group**](docs/PortfolioGroupsApi.md#get_a2_b_data_for_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code}/a2b | [EARLY ACCESS] GetA2BDataForPortfolioGroup: Get A2B data for a Portfolio Group
*PortfolioGroupsApi* | [**get_group_properties**](docs/PortfolioGroupsApi.md#get_group_properties) | **GET** /api/portfoliogroups/{scope}/{code}/properties | [EARLY ACCESS] GetGroupProperties: Get group properties
*PortfolioGroupsApi* | [**get_holdings_for_portfolio_group**](docs/PortfolioGroupsApi.md#get_holdings_for_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code}/holdings | GetHoldingsForPortfolioGroup: Get holdings for transaction portfolios in portfolio group
*PortfolioGroupsApi* | [**get_portfolio_group**](docs/PortfolioGroupsApi.md#get_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code} | GetPortfolioGroup: Get portfolio group
*PortfolioGroupsApi* | [**get_portfolio_group_access_metadata_by_key**](docs/PortfolioGroupsApi.md#get_portfolio_group_access_metadata_by_key) | **GET** /api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPortfolioGroupAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Portfolio Group
*PortfolioGroupsApi* | [**get_portfolio_group_commands**](docs/PortfolioGroupsApi.md#get_portfolio_group_commands) | **GET** /api/portfoliogroups/{scope}/{code}/commands | GetPortfolioGroupCommands: Get portfolio group commands
*PortfolioGroupsApi* | [**get_portfolio_group_expansion**](docs/PortfolioGroupsApi.md#get_portfolio_group_expansion) | **GET** /api/portfoliogroups/{scope}/{code}/expansion | [EARLY ACCESS] GetPortfolioGroupExpansion: Get portfolio group expansion
*PortfolioGroupsApi* | [**get_portfolio_group_metadata**](docs/PortfolioGroupsApi.md#get_portfolio_group_metadata) | **GET** /api/portfoliogroups/{scope}/{code}/metadata | [EARLY ACCESS] GetPortfolioGroupMetadata: Get Access Metadata rules for Portfolio Group
*PortfolioGroupsApi* | [**get_portfolio_group_property_time_series**](docs/PortfolioGroupsApi.md#get_portfolio_group_property_time_series) | **GET** /api/portfoliogroups/{scope}/{code}/properties/time-series | [EARLY ACCESS] GetPortfolioGroupPropertyTimeSeries: Get the time series of a portfolio group property
*PortfolioGroupsApi* | [**get_portfolio_group_relations**](docs/PortfolioGroupsApi.md#get_portfolio_group_relations) | **GET** /api/portfoliogroups/{scope}/{code}/relations | [EXPERIMENTAL] GetPortfolioGroupRelations: Get Relations for Portfolio Group
*PortfolioGroupsApi* | [**get_portfolio_group_relationships**](docs/PortfolioGroupsApi.md#get_portfolio_group_relationships) | **GET** /api/portfoliogroups/{scope}/{code}/relationships | [EARLY ACCESS] GetPortfolioGroupRelationships: Get Relationships for Portfolio Group
*PortfolioGroupsApi* | [**get_transactions_for_portfolio_group**](docs/PortfolioGroupsApi.md#get_transactions_for_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code}/transactions | GetTransactionsForPortfolioGroup: Get transactions for transaction portfolios in a portfolio group
*PortfolioGroupsApi* | [**list_portfolio_groups**](docs/PortfolioGroupsApi.md#list_portfolio_groups) | **GET** /api/portfoliogroups/{scope} | ListPortfolioGroups: List portfolio groups
*PortfolioGroupsApi* | [**patch_portfolio_group_access_metadata**](docs/PortfolioGroupsApi.md#patch_portfolio_group_access_metadata) | **PATCH** /api/portfoliogroups/{scope}/{code}/metadata | [EARLY ACCESS] PatchPortfolioGroupAccessMetadata: Patch Access Metadata rules for a Portfolio Group.
*PortfolioGroupsApi* | [**update_portfolio_group**](docs/PortfolioGroupsApi.md#update_portfolio_group) | **PUT** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] UpdatePortfolioGroup: Update portfolio group
*PortfolioGroupsApi* | [**upsert_group_properties**](docs/PortfolioGroupsApi.md#upsert_group_properties) | **POST** /api/portfoliogroups/{scope}/{code}/properties/$upsert | [EARLY ACCESS] UpsertGroupProperties: Upsert group properties
*PortfolioGroupsApi* | [**upsert_portfolio_group_access_metadata**](docs/PortfolioGroupsApi.md#upsert_portfolio_group_access_metadata) | **PUT** /api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | UpsertPortfolioGroupAccessMetadata: Upsert a Portfolio Group Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
*PortfoliosApi* | [**batch_upsert_portfolio_access_metadata**](docs/PortfoliosApi.md#batch_upsert_portfolio_access_metadata) | **PUT** /api/portfolios/metadata | [EARLY ACCESS] BatchUpsertPortfolioAccessMetadata: Upsert multiple Portfolio Access Metadata Rules to multiple Portfolios
*PortfoliosApi* | [**delete_instrument_event_instruction**](docs/PortfoliosApi.md#delete_instrument_event_instruction) | **DELETE** /api/portfolios/{scope}/{code}/instrumenteventinstructions/{instrumentEventInstructionId} | [EARLY ACCESS] DeleteInstrumentEventInstruction: Delete Instrument Event Instruction
*PortfoliosApi* | [**delete_key_from_portfolio_access_metadata**](docs/PortfoliosApi.md#delete_key_from_portfolio_access_metadata) | **DELETE** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | DeleteKeyFromPortfolioAccessMetadata: Delete a Portfolio Access Metadata Rule
*PortfoliosApi* | [**delete_portfolio**](docs/PortfoliosApi.md#delete_portfolio) | **DELETE** /api/portfolios/{scope}/{code} | DeletePortfolio: Delete portfolio
*PortfoliosApi* | [**delete_portfolio_properties**](docs/PortfoliosApi.md#delete_portfolio_properties) | **DELETE** /api/portfolios/{scope}/{code}/properties | DeletePortfolioProperties: Delete portfolio properties
*PortfoliosApi* | [**delete_portfolio_returns**](docs/PortfoliosApi.md#delete_portfolio_returns) | **DELETE** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/$delete | [EARLY ACCESS] DeletePortfolioReturns: Delete Returns
*PortfoliosApi* | [**get_aggregated_returns_dispersion_metrics**](docs/PortfoliosApi.md#get_aggregated_returns_dispersion_metrics) | **POST** /api/portfolios/{scope}/{code}/returns/dispersion/$aggregated | [EARLY ACCESS] GetAggregatedReturnsDispersionMetrics: Get the Aggregated Returns Dispersion metric
*PortfoliosApi* | [**get_composite_breakdown**](docs/PortfoliosApi.md#get_composite_breakdown) | **POST** /api/portfolios/{scope}/{code}/returns/breakdown | [EARLY ACCESS] GetCompositeBreakdown: Get the Composite Breakdown on how the composite Returns are calculated
*PortfoliosApi* | [**get_instrument_event_instruction**](docs/PortfoliosApi.md#get_instrument_event_instruction) | **GET** /api/portfolios/{scope}/{code}/instrumenteventinstructions/{instrumentEventInstructionId} | [EARLY ACCESS] GetInstrumentEventInstruction: Get Instrument Event Instruction
*PortfoliosApi* | [**get_portfolio**](docs/PortfoliosApi.md#get_portfolio) | **GET** /api/portfolios/{scope}/{code} | GetPortfolio: Get portfolio
*PortfoliosApi* | [**get_portfolio_aggregate_returns**](docs/PortfoliosApi.md#get_portfolio_aggregate_returns) | **GET** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/aggregated | [DEPRECATED] GetPortfolioAggregateReturns: Aggregate Returns (This is a deprecated endpoint).
*PortfoliosApi* | [**get_portfolio_aggregated_returns**](docs/PortfoliosApi.md#get_portfolio_aggregated_returns) | **POST** /api/portfolios/{scope}/{code}/returns/$aggregated | GetPortfolioAggregatedReturns: Aggregated Returns
*PortfoliosApi* | [**get_portfolio_commands**](docs/PortfoliosApi.md#get_portfolio_commands) | **GET** /api/portfolios/{scope}/{code}/commands | GetPortfolioCommands: Get portfolio commands
*PortfoliosApi* | [**get_portfolio_metadata**](docs/PortfoliosApi.md#get_portfolio_metadata) | **GET** /api/portfolios/{scope}/{code}/metadata | GetPortfolioMetadata: Get access metadata rules for a portfolio
*PortfoliosApi* | [**get_portfolio_properties**](docs/PortfoliosApi.md#get_portfolio_properties) | **GET** /api/portfolios/{scope}/{code}/properties | GetPortfolioProperties: Get portfolio properties
*PortfoliosApi* | [**get_portfolio_property_time_series**](docs/PortfoliosApi.md#get_portfolio_property_time_series) | **GET** /api/portfolios/{scope}/{code}/properties/time-series | GetPortfolioPropertyTimeSeries: Get portfolio property time series
*PortfoliosApi* | [**get_portfolio_relations**](docs/PortfoliosApi.md#get_portfolio_relations) | **GET** /api/portfolios/{scope}/{code}/relations | [EXPERIMENTAL] GetPortfolioRelations: Get portfolio relations
*PortfoliosApi* | [**get_portfolio_relationships**](docs/PortfoliosApi.md#get_portfolio_relationships) | **GET** /api/portfolios/{scope}/{code}/relationships | GetPortfolioRelationships: Get portfolio relationships
*PortfoliosApi* | [**get_portfolio_returns**](docs/PortfoliosApi.md#get_portfolio_returns) | **GET** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode} | GetPortfolioReturns: Get Returns
*PortfoliosApi* | [**get_portfolios_access_metadata_by_key**](docs/PortfoliosApi.md#get_portfolios_access_metadata_by_key) | **GET** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPortfoliosAccessMetadataByKey: Get an entry identified by a metadataKey in the access metadata object
*PortfoliosApi* | [**list_instrument_event_instructions**](docs/PortfoliosApi.md#list_instrument_event_instructions) | **GET** /api/portfolios/{scope}/{code}/instrumenteventinstructions | [EARLY ACCESS] ListInstrumentEventInstructions: List Instrument Event Instructions
*PortfoliosApi* | [**list_portfolio_properties**](docs/PortfoliosApi.md#list_portfolio_properties) | **GET** /api/portfolios/{scope}/{code}/properties/list | [EARLY ACCESS] ListPortfolioProperties: Get portfolio properties
*PortfoliosApi* | [**list_portfolios**](docs/PortfoliosApi.md#list_portfolios) | **GET** /api/portfolios | ListPortfolios: List portfolios
*PortfoliosApi* | [**list_portfolios_for_scope**](docs/PortfoliosApi.md#list_portfolios_for_scope) | **GET** /api/portfolios/{scope} | ListPortfoliosForScope: List portfolios for scope
*PortfoliosApi* | [**patch_portfolio**](docs/PortfoliosApi.md#patch_portfolio) | **PATCH** /api/portfolios/{scope}/{code} | PatchPortfolio: Patch portfolio.
*PortfoliosApi* | [**patch_portfolio_access_metadata**](docs/PortfoliosApi.md#patch_portfolio_access_metadata) | **PATCH** /api/portfolios/{scope}/{code}/metadata | [EARLY ACCESS] PatchPortfolioAccessMetadata: Patch Access Metadata rules for a Portfolio.
*PortfoliosApi* | [**update_portfolio**](docs/PortfoliosApi.md#update_portfolio) | **PUT** /api/portfolios/{scope}/{code} | UpdatePortfolio: Update portfolio
*PortfoliosApi* | [**upsert_instrument_event_instructions**](docs/PortfoliosApi.md#upsert_instrument_event_instructions) | **POST** /api/portfolios/{scope}/{code}/instrumenteventinstructions | [EARLY ACCESS] UpsertInstrumentEventInstructions: Upsert Instrument Event Instructions
*PortfoliosApi* | [**upsert_portfolio_access_metadata**](docs/PortfoliosApi.md#upsert_portfolio_access_metadata) | **PUT** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | UpsertPortfolioAccessMetadata: Upsert a Portfolio Access Metadata Rule associated with specific metadataKey. This creates or updates the data in LUSID.
*PortfoliosApi* | [**upsert_portfolio_properties**](docs/PortfoliosApi.md#upsert_portfolio_properties) | **POST** /api/portfolios/{scope}/{code}/properties | UpsertPortfolioProperties: Upsert portfolio properties
*PortfoliosApi* | [**upsert_portfolio_returns**](docs/PortfoliosApi.md#upsert_portfolio_returns) | **POST** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode} | UpsertPortfolioReturns: Upsert Returns
*PropertyDefinitionsApi* | [**create_derived_property_definition**](docs/PropertyDefinitionsApi.md#create_derived_property_definition) | **POST** /api/propertydefinitions/derived | [EARLY ACCESS] CreateDerivedPropertyDefinition: Create derived property definition
*PropertyDefinitionsApi* | [**create_property_definition**](docs/PropertyDefinitionsApi.md#create_property_definition) | **POST** /api/propertydefinitions | CreatePropertyDefinition: Create property definition
*PropertyDefinitionsApi* | [**delete_property_definition**](docs/PropertyDefinitionsApi.md#delete_property_definition) | **DELETE** /api/propertydefinitions/{domain}/{scope}/{code} | DeletePropertyDefinition: Delete property definition
*PropertyDefinitionsApi* | [**delete_property_definition_properties**](docs/PropertyDefinitionsApi.md#delete_property_definition_properties) | **POST** /api/propertydefinitions/{domain}/{scope}/{code}/properties/$delete | [EARLY ACCESS] DeletePropertyDefinitionProperties: Delete property definition properties
*PropertyDefinitionsApi* | [**get_derived_formula_explanation**](docs/PropertyDefinitionsApi.md#get_derived_formula_explanation) | **POST** /api/propertydefinitions/derived/$formulaExplanation | GetDerivedFormulaExplanation: Get explanation of a derived property formula
*PropertyDefinitionsApi* | [**get_multiple_property_definitions**](docs/PropertyDefinitionsApi.md#get_multiple_property_definitions) | **GET** /api/propertydefinitions | GetMultiplePropertyDefinitions: Get multiple property definitions
*PropertyDefinitionsApi* | [**get_property_definition**](docs/PropertyDefinitionsApi.md#get_property_definition) | **GET** /api/propertydefinitions/{domain}/{scope}/{code} | GetPropertyDefinition: Get property definition
*PropertyDefinitionsApi* | [**get_property_definition_property_time_series**](docs/PropertyDefinitionsApi.md#get_property_definition_property_time_series) | **GET** /api/propertydefinitions/{domain}/{scope}/{code}/properties/time-series | [EARLY ACCESS] GetPropertyDefinitionPropertyTimeSeries: Get Property Definition Property Time Series
*PropertyDefinitionsApi* | [**list_property_definitions**](docs/PropertyDefinitionsApi.md#list_property_definitions) | **GET** /api/propertydefinitions/$list | ListPropertyDefinitions: List property definitions
*PropertyDefinitionsApi* | [**update_derived_property_definition**](docs/PropertyDefinitionsApi.md#update_derived_property_definition) | **PUT** /api/propertydefinitions/derived/{domain}/{scope}/{code} | [EARLY ACCESS] UpdateDerivedPropertyDefinition: Update a pre-existing derived property definition
*PropertyDefinitionsApi* | [**update_property_definition**](docs/PropertyDefinitionsApi.md#update_property_definition) | **PUT** /api/propertydefinitions/{domain}/{scope}/{code} | UpdatePropertyDefinition: Update property definition
*PropertyDefinitionsApi* | [**upsert_property_definition_properties**](docs/PropertyDefinitionsApi.md#upsert_property_definition_properties) | **POST** /api/propertydefinitions/{domain}/{scope}/{code}/properties | UpsertPropertyDefinitionProperties: Upsert properties to a property definition
*QueryableKeysApi* | [**get_all_queryable_keys**](docs/QueryableKeysApi.md#get_all_queryable_keys) | **GET** /api/queryablekeys | [EARLY ACCESS] GetAllQueryableKeys: Query the set of supported \"addresses\" that can be queried from all endpoints.
*QuotesApi* | [**delete_quote_access_metadata_rule**](docs/QuotesApi.md#delete_quote_access_metadata_rule) | **DELETE** /api/metadata/quotes/rules/{scope} | [EXPERIMENTAL] DeleteQuoteAccessMetadataRule: Delete a Quote Access Metadata Rule
*QuotesApi* | [**delete_quotes**](docs/QuotesApi.md#delete_quotes) | **POST** /api/quotes/{scope}/$delete | DeleteQuotes: Delete quotes
*QuotesApi* | [**get_quotes**](docs/QuotesApi.md#get_quotes) | **POST** /api/quotes/{scope}/$get | GetQuotes: Get quotes
*QuotesApi* | [**get_quotes_access_metadata_rule**](docs/QuotesApi.md#get_quotes_access_metadata_rule) | **GET** /api/metadata/quotes/rules | [EXPERIMENTAL] GetQuotesAccessMetadataRule: Get a quote access metadata rule
*QuotesApi* | [**list_quotes**](docs/QuotesApi.md#list_quotes) | **GET** /api/quotes/{scope}/$deprecated | [DEPRECATED] ListQuotes: List quotes
*QuotesApi* | [**list_quotes_access_metadata_rules**](docs/QuotesApi.md#list_quotes_access_metadata_rules) | **GET** /api/metadata/quotes/rules/{scope} | [EXPERIMENTAL] ListQuotesAccessMetadataRules: List all quote access metadata rules in a scope
*QuotesApi* | [**list_quotes_for_scope**](docs/QuotesApi.md#list_quotes_for_scope) | **GET** /api/quotes/{scope} | ListQuotesForScope: List quotes for scope
*QuotesApi* | [**upsert_quote_access_metadata_rule**](docs/QuotesApi.md#upsert_quote_access_metadata_rule) | **POST** /api/metadata/quotes/rules/{scope} | [EXPERIMENTAL] UpsertQuoteAccessMetadataRule: Upsert a Quote Access Metadata Rule. This creates or updates the data in LUSID.
*QuotesApi* | [**upsert_quotes**](docs/QuotesApi.md#upsert_quotes) | **POST** /api/quotes/{scope} | UpsertQuotes: Upsert quotes
*ReconciliationsApi* | [**create_scheduled_reconciliation**](docs/ReconciliationsApi.md#create_scheduled_reconciliation) | **POST** /api/portfolios/$scheduledReconciliations/{scope} | [EXPERIMENTAL] CreateScheduledReconciliation: Create a scheduled reconciliation
*ReconciliationsApi* | [**delete_reconciliation**](docs/ReconciliationsApi.md#delete_reconciliation) | **DELETE** /api/portfolios/$scheduledReconciliations/{scope}/{code} | [EXPERIMENTAL] DeleteReconciliation: Delete scheduled reconciliation
*ReconciliationsApi* | [**delete_reconciliation_mapping**](docs/ReconciliationsApi.md#delete_reconciliation_mapping) | **DELETE** /api/portfolios/mapping/{scope}/{code} | [EARLY ACCESS] DeleteReconciliationMapping: Delete a mapping
*ReconciliationsApi* | [**get_reconciliation**](docs/ReconciliationsApi.md#get_reconciliation) | **GET** /api/portfolios/$scheduledReconciliations/{scope}/{code} | [EXPERIMENTAL] GetReconciliation: Get scheduled reconciliation
*ReconciliationsApi* | [**get_reconciliation_mapping**](docs/ReconciliationsApi.md#get_reconciliation_mapping) | **GET** /api/portfolios/mapping/{scope}/{code} | [EARLY ACCESS] GetReconciliationMapping: Get a mapping
*ReconciliationsApi* | [**list_reconciliation_mappings**](docs/ReconciliationsApi.md#list_reconciliation_mappings) | **GET** /api/portfolios/mapping | [EARLY ACCESS] ListReconciliationMappings: List the reconciliation mappings
*ReconciliationsApi* | [**list_reconciliations**](docs/ReconciliationsApi.md#list_reconciliations) | **GET** /api/portfolios/$scheduledReconciliations | [EXPERIMENTAL] ListReconciliations: List scheduled reconciliations
*ReconciliationsApi* | [**reconcile_generic**](docs/ReconciliationsApi.md#reconcile_generic) | **POST** /api/portfolios/$reconcileGeneric | ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.                The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings,  and elision of resulting differences where they are 'empty' or null or zero.
*ReconciliationsApi* | [**reconcile_holdings**](docs/ReconciliationsApi.md#reconcile_holdings) | **POST** /api/portfolios/$reconcileholdings | [EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings
*ReconciliationsApi* | [**reconcile_inline**](docs/ReconciliationsApi.md#reconcile_inline) | **POST** /api/portfolios/$reconcileInline | ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.
*ReconciliationsApi* | [**reconcile_transactions**](docs/ReconciliationsApi.md#reconcile_transactions) | **POST** /api/portfolios/$reconcileTransactions | [EARLY ACCESS] ReconcileTransactions: Perform a Transactions Reconciliation.
*ReconciliationsApi* | [**reconcile_transactions_v2**](docs/ReconciliationsApi.md#reconcile_transactions_v2) | **POST** /api/portfolios/$reconcileTransactionsV2 | [EXPERIMENTAL] ReconcileTransactionsV2: Perform a Transactions Reconciliation.
*ReconciliationsApi* | [**reconcile_valuation**](docs/ReconciliationsApi.md#reconcile_valuation) | **POST** /api/portfolios/$reconcileValuation | ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.
*ReconciliationsApi* | [**update_reconciliation**](docs/ReconciliationsApi.md#update_reconciliation) | **POST** /api/portfolios/$scheduledReconciliations/{scope}/{code} | [EXPERIMENTAL] UpdateReconciliation: Update scheduled reconciliation
*ReconciliationsApi* | [**upsert_reconciliation_mapping**](docs/ReconciliationsApi.md#upsert_reconciliation_mapping) | **POST** /api/portfolios/mapping | [EARLY ACCESS] UpsertReconciliationMapping: Create or update a mapping
*ReferenceListsApi* | [**delete_reference_list**](docs/ReferenceListsApi.md#delete_reference_list) | **DELETE** /api/referencelists/{scope}/{code} | [EARLY ACCESS] DeleteReferenceList: Delete Reference List
*ReferenceListsApi* | [**get_reference_list**](docs/ReferenceListsApi.md#get_reference_list) | **GET** /api/referencelists/{scope}/{code} | GetReferenceList: Get Reference List
*ReferenceListsApi* | [**list_reference_lists**](docs/ReferenceListsApi.md#list_reference_lists) | **GET** /api/referencelists | [EARLY ACCESS] ListReferenceLists: List Reference Lists
*ReferenceListsApi* | [**upsert_reference_list**](docs/ReferenceListsApi.md#upsert_reference_list) | **POST** /api/referencelists | [EARLY ACCESS] UpsertReferenceList: Upsert Reference List
*ReferencePortfolioApi* | [**create_reference_portfolio**](docs/ReferencePortfolioApi.md#create_reference_portfolio) | **POST** /api/referenceportfolios/{scope} | CreateReferencePortfolio: Create reference portfolio
*ReferencePortfolioApi* | [**get_reference_portfolio_constituents**](docs/ReferencePortfolioApi.md#get_reference_portfolio_constituents) | **GET** /api/referenceportfolios/{scope}/{code}/constituents | GetReferencePortfolioConstituents: Get reference portfolio constituents
*ReferencePortfolioApi* | [**list_constituents_adjustments**](docs/ReferencePortfolioApi.md#list_constituents_adjustments) | **GET** /api/referenceportfolios/{scope}/{code}/constituentsadjustments | ListConstituentsAdjustments: List constituents adjustments
*ReferencePortfolioApi* | [**upsert_reference_portfolio_constituent_properties**](docs/ReferencePortfolioApi.md#upsert_reference_portfolio_constituent_properties) | **POST** /api/referenceportfolios/{scope}/{code}/constituents/properties | [EARLY ACCESS] UpsertReferencePortfolioConstituentProperties: Upsert constituent properties
*ReferencePortfolioApi* | [**upsert_reference_portfolio_constituents**](docs/ReferencePortfolioApi.md#upsert_reference_portfolio_constituents) | **POST** /api/referenceportfolios/{scope}/{code}/constituents | UpsertReferencePortfolioConstituents: Upsert reference portfolio constituents
*RelationDefinitionsApi* | [**create_relation_definition**](docs/RelationDefinitionsApi.md#create_relation_definition) | **POST** /api/relationdefinitions | [EXPERIMENTAL] CreateRelationDefinition: Create a relation definition
*RelationDefinitionsApi* | [**delete_relation_definition**](docs/RelationDefinitionsApi.md#delete_relation_definition) | **DELETE** /api/relationdefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteRelationDefinition: Delete relation definition
*RelationDefinitionsApi* | [**get_relation_definition**](docs/RelationDefinitionsApi.md#get_relation_definition) | **GET** /api/relationdefinitions/{scope}/{code} | [EXPERIMENTAL] GetRelationDefinition: Get relation definition
*RelationalDatasetDefinitionApi* | [**create_relational_dataset_definition**](docs/RelationalDatasetDefinitionApi.md#create_relational_dataset_definition) | **POST** /api/relationaldatasetdefinitions | [EARLY ACCESS] CreateRelationalDatasetDefinition: Create a Relational Dataset Definition
*RelationalDatasetDefinitionApi* | [**delete_relational_dataset_definition**](docs/RelationalDatasetDefinitionApi.md#delete_relational_dataset_definition) | **DELETE** /api/relationaldatasetdefinitions/{scope}/{code} | [EARLY ACCESS] DeleteRelationalDatasetDefinition: Delete a Relational Dataset Definition
*RelationalDatasetDefinitionApi* | [**get_relational_dataset_definition**](docs/RelationalDatasetDefinitionApi.md#get_relational_dataset_definition) | **GET** /api/relationaldatasetdefinitions/{scope}/{code} | [EARLY ACCESS] GetRelationalDatasetDefinition: Get a Relational Dataset Definition
*RelationalDatasetDefinitionApi* | [**list_relational_dataset_definitions**](docs/RelationalDatasetDefinitionApi.md#list_relational_dataset_definitions) | **GET** /api/relationaldatasetdefinitions | [EARLY ACCESS] ListRelationalDatasetDefinitions: List Relational Dataset Definitions
*RelationalDatasetDefinitionApi* | [**update_relational_dataset_definition**](docs/RelationalDatasetDefinitionApi.md#update_relational_dataset_definition) | **PUT** /api/relationaldatasetdefinitions/{scope}/{code} | [EARLY ACCESS] UpdateRelationalDatasetDefinition: Update a Relational Dataset Definition
*RelationalDatasetDefinitionApi* | [**update_relational_dataset_details**](docs/RelationalDatasetDefinitionApi.md#update_relational_dataset_details) | **POST** /api/relationaldatasetdefinitions/{scope}/{code}/details/$update | [EARLY ACCESS] UpdateRelationalDatasetDetails: Update Relational Dataset Details: DisplayName, Description and ApplicableEntityTypes
*RelationalDatasetDefinitionApi* | [**update_relational_dataset_field_schema**](docs/RelationalDatasetDefinitionApi.md#update_relational_dataset_field_schema) | **POST** /api/relationaldatasetdefinitions/{scope}/{code}/fieldschema/$update | [EARLY ACCESS] UpdateRelationalDatasetFieldSchema: Update Relational Dataset Field Schema
*RelationalDatasetsApi* | [**batch_delete_relational_data**](docs/RelationalDatasetsApi.md#batch_delete_relational_data) | **POST** /api/relationaldatasets/{relationalDatasetDefinitionScope}/{relationalDatasetDefinitionCode}/$batchDelete | [EXPERIMENTAL] BatchDeleteRelationalData: Batch Delete Relational Data Points for a given Relational Dataset Definition.
*RelationalDatasetsApi* | [**batch_upsert_relational_data**](docs/RelationalDatasetsApi.md#batch_upsert_relational_data) | **POST** /api/relationaldatasets/{relationalDatasetDefinitionScope}/{relationalDatasetDefinitionCode}/$batchUpsert | [EXPERIMENTAL] BatchUpsertRelationalData: Batch Upsert Relational Data Points for a given Relational Dataset Definition.
*RelationalDatasetsApi* | [**query_relational_data**](docs/RelationalDatasetsApi.md#query_relational_data) | **POST** /api/relationaldatasets/{relationalDatasetDefinitionScope}/{relationalDatasetDefinitionCode}/$query | [EXPERIMENTAL] QueryRelationalData: Query Relational Data Points for a given Relational Dataset Definition.
*RelationsApi* | [**create_relation**](docs/RelationsApi.md#create_relation) | **POST** /api/relations/{scope}/{code} | [EXPERIMENTAL] CreateRelation: Create Relation
*RelationsApi* | [**delete_relation**](docs/RelationsApi.md#delete_relation) | **POST** /api/relations/{scope}/{code}/$delete | [EXPERIMENTAL] DeleteRelation: Delete a relation
*RelationshipDefinitionsApi* | [**create_relationship_definition**](docs/RelationshipDefinitionsApi.md#create_relationship_definition) | **POST** /api/relationshipdefinitions | [EARLY ACCESS] CreateRelationshipDefinition: Create Relationship Definition
*RelationshipDefinitionsApi* | [**delete_relationship_definition**](docs/RelationshipDefinitionsApi.md#delete_relationship_definition) | **DELETE** /api/relationshipdefinitions/{scope}/{code} | [EARLY ACCESS] DeleteRelationshipDefinition: Delete Relationship Definition
*RelationshipDefinitionsApi* | [**get_relationship_definition**](docs/RelationshipDefinitionsApi.md#get_relationship_definition) | **GET** /api/relationshipdefinitions/{scope}/{code} | [EARLY ACCESS] GetRelationshipDefinition: Get relationship definition
*RelationshipDefinitionsApi* | [**list_relationship_definitions**](docs/RelationshipDefinitionsApi.md#list_relationship_definitions) | **GET** /api/relationshipdefinitions | [EARLY ACCESS] ListRelationshipDefinitions: List relationship definitions
*RelationshipDefinitionsApi* | [**update_relationship_definition**](docs/RelationshipDefinitionsApi.md#update_relationship_definition) | **PUT** /api/relationshipdefinitions/{scope}/{code} | [EARLY ACCESS] UpdateRelationshipDefinition: Update Relationship Definition
*RelationshipsApi* | [**create_relationship**](docs/RelationshipsApi.md#create_relationship) | **POST** /api/relationshipdefinitions/{scope}/{code}/relationships | CreateRelationship: Create Relationship
*RelationshipsApi* | [**delete_relationship**](docs/RelationshipsApi.md#delete_relationship) | **POST** /api/relationshipdefinitions/{scope}/{code}/relationships/$delete | [EARLY ACCESS] DeleteRelationship: Delete Relationship
*SchemasApi* | [**get_entity_schema**](docs/SchemasApi.md#get_entity_schema) | **GET** /api/schemas/entities/{entity} | [EARLY ACCESS] GetEntitySchema: Get schema
*SchemasApi* | [**get_property_schema**](docs/SchemasApi.md#get_property_schema) | **GET** /api/schemas/properties | [EARLY ACCESS] GetPropertySchema: Get property schema
*SchemasApi* | [**get_value_types**](docs/SchemasApi.md#get_value_types) | **GET** /api/schemas/types | [EARLY ACCESS] GetValueTypes: Get value types
*SchemasApi* | [**list_entities**](docs/SchemasApi.md#list_entities) | **GET** /api/schemas/entities | [EARLY ACCESS] ListEntities: List entities
*ScopesApi* | [**list_entity_scopes**](docs/ScopesApi.md#list_entity_scopes) | **GET** /api/scopes/{entityType} | ListEntityScopes: List Entity Scopes
*ScopesApi* | [**list_scopes**](docs/ScopesApi.md#list_scopes) | **GET** /api/scopes | ListScopes: List Scopes
*ScriptedTranslationApi* | [**get_translation_dialect**](docs/ScriptedTranslationApi.md#get_translation_dialect) | **GET** /api/scriptedtranslation/dialects/{scope}/{vendor}/{sourceSystem}/{entityType}/{serialisationFormat}/{version} | [EARLY ACCESS] GetTranslationDialect: Get a dialect.
*ScriptedTranslationApi* | [**get_translation_script**](docs/ScriptedTranslationApi.md#get_translation_script) | **GET** /api/scriptedtranslation/scripts/{scope}/{code}/{version} | [EARLY ACCESS] GetTranslationScript: Retrieve a translation script by its identifier.
*ScriptedTranslationApi* | [**list_dialect_ids**](docs/ScriptedTranslationApi.md#list_dialect_ids) | **GET** /api/scriptedtranslation/dialects/ids | [EARLY ACCESS] ListDialectIds: List dialect identifiers matching an optional filter.
*ScriptedTranslationApi* | [**list_translation_script_ids**](docs/ScriptedTranslationApi.md#list_translation_script_ids) | **GET** /api/scriptedtranslation/scripts/ids | [EARLY ACCESS] ListTranslationScriptIds: List translation script identifiers.
*ScriptedTranslationApi* | [**translate_entities**](docs/ScriptedTranslationApi.md#translate_entities) | **POST** /api/scriptedtranslation/translateentities | [EARLY ACCESS] TranslateEntities: Translate a collection of entities with a specified translation script.
*ScriptedTranslationApi* | [**translate_entities_inlined**](docs/ScriptedTranslationApi.md#translate_entities_inlined) | **POST** /api/scriptedtranslation/translateentitiesinlined | [EARLY ACCESS] TranslateEntitiesInlined: Translate a collection of entities, inlining the body of the translation script.
*ScriptedTranslationApi* | [**upsert_translation_dialect**](docs/ScriptedTranslationApi.md#upsert_translation_dialect) | **POST** /api/scriptedtranslation/dialects | [EARLY ACCESS] UpsertTranslationDialect: Upsert a Dialect.
*ScriptedTranslationApi* | [**upsert_translation_script**](docs/ScriptedTranslationApi.md#upsert_translation_script) | **POST** /api/scriptedtranslation/scripts | [EARLY ACCESS] UpsertTranslationScript: Upsert a translation script.
*SearchApi* | [**instruments_search**](docs/SearchApi.md#instruments_search) | **POST** /api/search/instruments | [EARLY ACCESS] InstrumentsSearch: Instruments search
*SearchApi* | [**search_portfolio_groups**](docs/SearchApi.md#search_portfolio_groups) | **GET** /api/search/portfoliogroups | SearchPortfolioGroups: Search Portfolio Groups
*SearchApi* | [**search_portfolios**](docs/SearchApi.md#search_portfolios) | **GET** /api/search/portfolios | SearchPortfolios: Search Portfolios
*SearchApi* | [**search_properties**](docs/SearchApi.md#search_properties) | **GET** /api/search/propertydefinitions | SearchProperties: Search Property Definitions
*SequencesApi* | [**create_sequence**](docs/SequencesApi.md#create_sequence) | **POST** /api/sequences/{scope} | [EARLY ACCESS] CreateSequence: Create a new sequence
*SequencesApi* | [**get_sequence**](docs/SequencesApi.md#get_sequence) | **GET** /api/sequences/{scope}/{code} | [EARLY ACCESS] GetSequence: Get a specified sequence
*SequencesApi* | [**list_sequences**](docs/SequencesApi.md#list_sequences) | **GET** /api/sequences | [EARLY ACCESS] ListSequences: List Sequences
*SequencesApi* | [**next**](docs/SequencesApi.md#next) | **GET** /api/sequences/{scope}/{code}/next | [EARLY ACCESS] Next: Get next values from sequence
*SimplePositionPortfoliosApi* | [**create_simple_position_portfolio**](docs/SimplePositionPortfoliosApi.md#create_simple_position_portfolio) | **POST** /api/simpleposition/{scope} | [EARLY ACCESS] CreateSimplePositionPortfolio: Create simple position portfolio
*StagedModificationsApi* | [**add_decision**](docs/StagedModificationsApi.md#add_decision) | **POST** /api/stagedmodifications/{id}/decision | AddDecision: AddDecision
*StagedModificationsApi* | [**get_staged_modification**](docs/StagedModificationsApi.md#get_staged_modification) | **GET** /api/stagedmodifications/{id} | GetStagedModification: GetStagedModification
*StagedModificationsApi* | [**list_requested_changes**](docs/StagedModificationsApi.md#list_requested_changes) | **GET** /api/stagedmodifications/{id}/requestedChanges | ListRequestedChanges: ListRequestedChanges
*StagedModificationsApi* | [**list_staged_modifications**](docs/StagedModificationsApi.md#list_staged_modifications) | **GET** /api/stagedmodifications | ListStagedModifications: ListStagedModifications
*StagingRuleSetApi* | [**create_staging_rule_set**](docs/StagingRuleSetApi.md#create_staging_rule_set) | **POST** /api/stagingrulesets/{entityType} | CreateStagingRuleSet: Create a StagingRuleSet
*StagingRuleSetApi* | [**delete_staging_rule_set**](docs/StagingRuleSetApi.md#delete_staging_rule_set) | **DELETE** /api/stagingrulesets/{entityType} | DeleteStagingRuleSet: Delete a StagingRuleSet
*StagingRuleSetApi* | [**get_staging_rule_set**](docs/StagingRuleSetApi.md#get_staging_rule_set) | **GET** /api/stagingrulesets/{entityType} | GetStagingRuleSet: Get a StagingRuleSet
*StagingRuleSetApi* | [**list_staging_rule_sets**](docs/StagingRuleSetApi.md#list_staging_rule_sets) | **GET** /api/stagingrulesets | ListStagingRuleSets: List StagingRuleSets
*StagingRuleSetApi* | [**update_staging_rule_set**](docs/StagingRuleSetApi.md#update_staging_rule_set) | **PUT** /api/stagingrulesets/{entityType} | UpdateStagingRuleSet: Update a StagingRuleSet
*StructuredResultDataApi* | [**create_data_map**](docs/StructuredResultDataApi.md#create_data_map) | **POST** /api/unitresults/datamap/{scope} | CreateDataMap: Create data map
*StructuredResultDataApi* | [**delete_structured_result_data**](docs/StructuredResultDataApi.md#delete_structured_result_data) | **POST** /api/unitresults/{scope}/$delete | DeleteStructuredResultData: Delete structured result data
*StructuredResultDataApi* | [**get_address_key_definitions_for_document**](docs/StructuredResultDataApi.md#get_address_key_definitions_for_document) | **GET** /api/unitresults/virtualdocument/{scope}/{code}/{source}/{resultType}/addresskeydefinitions | GetAddressKeyDefinitionsForDocument: Get AddressKeyDefinitions for a virtual document.
*StructuredResultDataApi* | [**get_data_map**](docs/StructuredResultDataApi.md#get_data_map) | **POST** /api/unitresults/datamap/{scope}/$get | GetDataMap: Get data map
*StructuredResultDataApi* | [**get_structured_result_data**](docs/StructuredResultDataApi.md#get_structured_result_data) | **POST** /api/unitresults/{scope}/$get | GetStructuredResultData: Get structured result data
*StructuredResultDataApi* | [**get_virtual_document**](docs/StructuredResultDataApi.md#get_virtual_document) | **POST** /api/unitresults/virtualdocument/{scope}/$get | GetVirtualDocument: Get Virtual Documents
*StructuredResultDataApi* | [**get_virtual_document_rows**](docs/StructuredResultDataApi.md#get_virtual_document_rows) | **GET** /api/unitresults/virtualdocument/{scope}/{code}/{source}/{resultType} | GetVirtualDocumentRows: Get Virtual Document Rows
*StructuredResultDataApi* | [**upsert_result_value**](docs/StructuredResultDataApi.md#upsert_result_value) | **POST** /api/unitresults/resultvalue/{scope} | UpsertResultValue: Upsert result value
*StructuredResultDataApi* | [**upsert_structured_result_data**](docs/StructuredResultDataApi.md#upsert_structured_result_data) | **POST** /api/unitresults/{scope} | UpsertStructuredResultData: Upsert structured result data
*SystemConfigurationApi* | [**create_configuration_transaction_type**](docs/SystemConfigurationApi.md#create_configuration_transaction_type) | **POST** /api/systemconfiguration/transactions/type | [EARLY ACCESS] CreateConfigurationTransactionType: Create transaction type
*SystemConfigurationApi* | [**create_side_definition**](docs/SystemConfigurationApi.md#create_side_definition) | **POST** /api/systemconfiguration/transactions/side | [EXPERIMENTAL] CreateSideDefinition: Create side definition
*SystemConfigurationApi* | [**delete_transaction_configuration_source**](docs/SystemConfigurationApi.md#delete_transaction_configuration_source) | **DELETE** /api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] DeleteTransactionConfigurationSource: Delete all transaction configurations for a source
*SystemConfigurationApi* | [**get_transaction_configuration_source**](docs/SystemConfigurationApi.md#get_transaction_configuration_source) | **GET** /api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] GetTransactionConfigurationSource: Get all transaction configurations for a source
*SystemConfigurationApi* | [**list_configuration_transaction_types**](docs/SystemConfigurationApi.md#list_configuration_transaction_types) | **GET** /api/systemconfiguration/transactions | [EARLY ACCESS] ListConfigurationTransactionTypes: List transaction types
*SystemConfigurationApi* | [**set_configuration_transaction_types**](docs/SystemConfigurationApi.md#set_configuration_transaction_types) | **PUT** /api/systemconfiguration/transactions | [EXPERIMENTAL] SetConfigurationTransactionTypes: Set transaction types
*SystemConfigurationApi* | [**set_transaction_configuration_source**](docs/SystemConfigurationApi.md#set_transaction_configuration_source) | **PUT** /api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] SetTransactionConfigurationSource: Set transaction types for a source
*TaxRuleSetsApi* | [**create_tax_rule_set**](docs/TaxRuleSetsApi.md#create_tax_rule_set) | **POST** /api/tax/rulesets | [EXPERIMENTAL] CreateTaxRuleSet: Create a tax rule set.
*TaxRuleSetsApi* | [**delete_tax_rule_set**](docs/TaxRuleSetsApi.md#delete_tax_rule_set) | **DELETE** /api/tax/rulesets/{scope}/{code} | [EXPERIMENTAL] DeleteTaxRuleSet: Delete a tax rule set.
*TaxRuleSetsApi* | [**get_tax_rule_set**](docs/TaxRuleSetsApi.md#get_tax_rule_set) | **GET** /api/tax/rulesets/{scope}/{code} | [EXPERIMENTAL] GetTaxRuleSet: Retrieve the definition of single tax rule set.
*TaxRuleSetsApi* | [**list_tax_rule_sets**](docs/TaxRuleSetsApi.md#list_tax_rule_sets) | **GET** /api/tax/rulesets | [EXPERIMENTAL] ListTaxRuleSets: List tax rule sets.
*TaxRuleSetsApi* | [**update_tax_rule_set**](docs/TaxRuleSetsApi.md#update_tax_rule_set) | **PUT** /api/tax/rulesets/{scope}/{code} | [EXPERIMENTAL] UpdateTaxRuleSet: Update a tax rule set.
*TimelinesApi* | [**confirm_closed_period**](docs/TimelinesApi.md#confirm_closed_period) | **POST** /api/timelines/{scope}/{code}/closedperiods/{closedPeriodId}/$confirm | [EXPERIMENTAL] ConfirmClosedPeriod: Confirm a Closed Period against a Timeline Entity
*TimelinesApi* | [**create_closed_period**](docs/TimelinesApi.md#create_closed_period) | **POST** /api/timelines/{scope}/{code}/closedperiods | [EXPERIMENTAL] CreateClosedPeriod: Create a new closed period against a timeline entity
*TimelinesApi* | [**create_closed_period_candidate**](docs/TimelinesApi.md#create_closed_period_candidate) | **POST** /api/timelines/{scope}/{code}/closedperiods/candidate | [EXPERIMENTAL] CreateClosedPeriodCandidate: Create a new closed period candidate against a timeline entity
*TimelinesApi* | [**create_timeline**](docs/TimelinesApi.md#create_timeline) | **POST** /api/timelines | [EXPERIMENTAL] CreateTimeline: Create a Timeline
*TimelinesApi* | [**delete_timeline**](docs/TimelinesApi.md#delete_timeline) | **DELETE** /api/timelines/{scope}/{code} | [EXPERIMENTAL] DeleteTimeline: Deletes a particular Timeline
*TimelinesApi* | [**get_closed_period**](docs/TimelinesApi.md#get_closed_period) | **GET** /api/timelines/{scope}/{code}/closedperiods/{closedPeriodId} | [EXPERIMENTAL] GetClosedPeriod: Gets a Closed Period entity.
*TimelinesApi* | [**get_timeline**](docs/TimelinesApi.md#get_timeline) | **GET** /api/timelines/{scope}/{code} | [EXPERIMENTAL] GetTimeline: Get a single Timeline by scope and code.
*TimelinesApi* | [**list_closed_periods**](docs/TimelinesApi.md#list_closed_periods) | **GET** /api/timelines/{scope}/{code}/closedperiods | [EXPERIMENTAL] ListClosedPeriods: List ClosedPeriods for a specified Timeline.
*TimelinesApi* | [**list_timelines**](docs/TimelinesApi.md#list_timelines) | **GET** /api/timelines | [EXPERIMENTAL] ListTimelines: List Timelines
*TimelinesApi* | [**set_post_close_activity**](docs/TimelinesApi.md#set_post_close_activity) | **POST** /api/timelines/{scope}/{code}/closedperiods/{closedPeriodId}/postcloseactivity | [EXPERIMENTAL] SetPostCloseActivity: Sets post close activities to a closed period.
*TimelinesApi* | [**unconfirm_closed_period**](docs/TimelinesApi.md#unconfirm_closed_period) | **POST** /api/timelines/{scope}/{code}/closedperiods/{closedPeriodId}/$unconfirm | [EXPERIMENTAL] UnconfirmClosedPeriod: Unconfirm the last confirmed Closed Period against a Timeline Entity
*TimelinesApi* | [**update_timeline**](docs/TimelinesApi.md#update_timeline) | **PUT** /api/timelines/{scope}/{code} | [EXPERIMENTAL] UpdateTimeline: Update Timeline defined by scope and code
*TransactionConfigurationApi* | [**delete_side_definition**](docs/TransactionConfigurationApi.md#delete_side_definition) | **DELETE** /api/transactionconfiguration/sides/{side}/$delete | DeleteSideDefinition: Delete the given side definition
*TransactionConfigurationApi* | [**delete_transaction_type**](docs/TransactionConfigurationApi.md#delete_transaction_type) | **DELETE** /api/transactionconfiguration/types/{source}/{type} | DeleteTransactionType: Delete a transaction type
*TransactionConfigurationApi* | [**delete_transaction_type_source**](docs/TransactionConfigurationApi.md#delete_transaction_type_source) | **DELETE** /api/transactionconfiguration/types/{source}/$delete | DeleteTransactionTypeSource: Delete all transaction types for the given source and scope
*TransactionConfigurationApi* | [**get_side_definition**](docs/TransactionConfigurationApi.md#get_side_definition) | **GET** /api/transactionconfiguration/sides/{side} | GetSideDefinition: Get the side definition for a given side name( or label)
*TransactionConfigurationApi* | [**get_transaction_type**](docs/TransactionConfigurationApi.md#get_transaction_type) | **GET** /api/transactionconfiguration/types/{source}/{type} | GetTransactionType: Get a single transaction configuration type
*TransactionConfigurationApi* | [**list_side_definitions**](docs/TransactionConfigurationApi.md#list_side_definitions) | **GET** /api/transactionconfiguration/sides | ListSideDefinitions: List the side definitions
*TransactionConfigurationApi* | [**list_transaction_types**](docs/TransactionConfigurationApi.md#list_transaction_types) | **GET** /api/transactionconfiguration/types | ListTransactionTypes: List transaction types
*TransactionConfigurationApi* | [**set_side_definition**](docs/TransactionConfigurationApi.md#set_side_definition) | **PUT** /api/transactionconfiguration/sides/{side} | SetSideDefinition: Set a side definition
*TransactionConfigurationApi* | [**set_side_definitions**](docs/TransactionConfigurationApi.md#set_side_definitions) | **PUT** /api/transactionconfiguration/sides | SetSideDefinitions: Set the given side definitions
*TransactionConfigurationApi* | [**set_transaction_type**](docs/TransactionConfigurationApi.md#set_transaction_type) | **PUT** /api/transactionconfiguration/types/{source}/{type} | SetTransactionType: Set a specific transaction type
*TransactionConfigurationApi* | [**set_transaction_type_source**](docs/TransactionConfigurationApi.md#set_transaction_type_source) | **PUT** /api/transactionconfiguration/types/{source} | SetTransactionTypeSource: Set the transaction types for the given source and scope
*TransactionFeesApi* | [**delete_transaction_fee_rule**](docs/TransactionFeesApi.md#delete_transaction_fee_rule) | **DELETE** /api/transactions/fees/rules/{code} | DeleteTransactionFeeRule: Deletes a fee rule.
*TransactionFeesApi* | [**get_applicable_transaction_fees**](docs/TransactionFeesApi.md#get_applicable_transaction_fees) | **POST** /api/transactions/fees/$GetApplicableFees | GetApplicableTransactionFees: Get the Fees and Commissions that may be applicable to a transaction.
*TransactionFeesApi* | [**get_transaction_fee_rule**](docs/TransactionFeesApi.md#get_transaction_fee_rule) | **GET** /api/transactions/fees/rules/{code} | GetTransactionFeeRule: Retrieve the definition of single fee rule.
*TransactionFeesApi* | [**list_transaction_fee_rules**](docs/TransactionFeesApi.md#list_transaction_fee_rules) | **GET** /api/transactions/fees/rules | ListTransactionFeeRules: List fee rules, with optional filtering.
*TransactionFeesApi* | [**upsert_transaction_fee_rules**](docs/TransactionFeesApi.md#upsert_transaction_fee_rules) | **POST** /api/transactions/fees/rules | UpsertTransactionFeeRules: Upsert fee rules.
*TransactionPortfoliosApi* | [**adjust_holdings**](docs/TransactionPortfoliosApi.md#adjust_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings | AdjustHoldings: Adjust holdings
*TransactionPortfoliosApi* | [**batch_adjust_holdings**](docs/TransactionPortfoliosApi.md#batch_adjust_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings/$batchAdjust | BatchAdjustHoldings: Batch adjust holdings
*TransactionPortfoliosApi* | [**batch_create_trade_tickets**](docs/TransactionPortfoliosApi.md#batch_create_trade_tickets) | **POST** /api/transactionportfolios/{scope}/{code}/$batchtradetickets | BatchCreateTradeTickets: Batch Create Trade Tickets
*TransactionPortfoliosApi* | [**batch_set_holdings**](docs/TransactionPortfoliosApi.md#batch_set_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings/$batchSet | BatchSetHoldings: Batch set holdings
*TransactionPortfoliosApi* | [**batch_upsert_settlement_instructions**](docs/TransactionPortfoliosApi.md#batch_upsert_settlement_instructions) | **POST** /api/transactionportfolios/{scope}/{code}/settlementinstructions/$batchUpsert | [EARLY ACCESS] BatchUpsertSettlementInstructions: Batch Upsert Settlement Instructions.
*TransactionPortfoliosApi* | [**batch_upsert_transactions**](docs/TransactionPortfoliosApi.md#batch_upsert_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/$batchUpsert | BatchUpsertTransactions: Batch upsert transactions
*TransactionPortfoliosApi* | [**build_settlement_instructions**](docs/TransactionPortfoliosApi.md#build_settlement_instructions) | **POST** /api/transactionportfolios/{scope}/{code}/settlementinstructions/$build | [EARLY ACCESS] BuildSettlementInstructions: Build Settlement Instructions
*TransactionPortfoliosApi* | [**build_transactions**](docs/TransactionPortfoliosApi.md#build_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/$build | BuildTransactions: Build transactions
*TransactionPortfoliosApi* | [**cancel_adjust_holdings**](docs/TransactionPortfoliosApi.md#cancel_adjust_holdings) | **DELETE** /api/transactionportfolios/{scope}/{code}/holdings | CancelAdjustHoldings: Cancel adjust holdings
*TransactionPortfoliosApi* | [**cancel_single_adjust_holding**](docs/TransactionPortfoliosApi.md#cancel_single_adjust_holding) | **POST** /api/transactionportfolios/{scope}/{code}/holdings/$cancelAdjustment | CancelSingleAdjustHolding: Cancel single holding adjustment.
*TransactionPortfoliosApi* | [**cancel_transactions**](docs/TransactionPortfoliosApi.md#cancel_transactions) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions | CancelTransactions: Cancel transactions
*TransactionPortfoliosApi* | [**create_portfolio**](docs/TransactionPortfoliosApi.md#create_portfolio) | **POST** /api/transactionportfolios/{scope} | CreatePortfolio: Create portfolio
*TransactionPortfoliosApi* | [**create_trade_ticket**](docs/TransactionPortfoliosApi.md#create_trade_ticket) | **POST** /api/transactionportfolios/{scope}/{code}/$tradeticket | CreateTradeTicket: Create Trade Ticket
*TransactionPortfoliosApi* | [**delete_custodian_accounts**](docs/TransactionPortfoliosApi.md#delete_custodian_accounts) | **POST** /api/transactionportfolios/{scope}/{code}/custodianaccounts/$delete | DeleteCustodianAccounts: Soft or hard delete multiple custodian accounts
*TransactionPortfoliosApi* | [**delete_properties_from_transaction**](docs/TransactionPortfoliosApi.md#delete_properties_from_transaction) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | DeletePropertiesFromTransaction: Delete properties from transaction
*TransactionPortfoliosApi* | [**delete_settlement_instructions**](docs/TransactionPortfoliosApi.md#delete_settlement_instructions) | **DELETE** /api/transactionportfolios/{scope}/{code}/settlementinstructions | [EARLY ACCESS] DeleteSettlementInstructions: Delete Settlement Instructions.
*TransactionPortfoliosApi* | [**get_a2_b_data**](docs/TransactionPortfoliosApi.md#get_a2_b_data) | **GET** /api/transactionportfolios/{scope}/{code}/a2b | GetA2BData: Get A2B data
*TransactionPortfoliosApi* | [**get_a2_b_movements**](docs/TransactionPortfoliosApi.md#get_a2_b_movements) | **GET** /api/transactionportfolios/{scope}/{code}/a2bmovements | GetA2BMovements: Get an A2B report at the movement level for the given portfolio.
*TransactionPortfoliosApi* | [**get_bucketed_cash_flows**](docs/TransactionPortfoliosApi.md#get_bucketed_cash_flows) | **POST** /api/transactionportfolios/{scope}/{code}/bucketedCashFlows | GetBucketedCashFlows: Get bucketed cash flows from a list of portfolios
*TransactionPortfoliosApi* | [**get_custodian_account**](docs/TransactionPortfoliosApi.md#get_custodian_account) | **GET** /api/transactionportfolios/{scope}/{code}/custodianaccounts/{custodianAccountScope}/{custodianAccountCode} | GetCustodianAccount: Get Custodian Account
*TransactionPortfoliosApi* | [**get_details**](docs/TransactionPortfoliosApi.md#get_details) | **GET** /api/transactionportfolios/{scope}/{code}/details | GetDetails: Get details
*TransactionPortfoliosApi* | [**get_holding_contributors**](docs/TransactionPortfoliosApi.md#get_holding_contributors) | **GET** /api/transactionportfolios/{scope}/{code}/holdings/{holdingId}/contributors | GetHoldingContributors: Get Holdings Contributors
*TransactionPortfoliosApi* | [**get_holdings**](docs/TransactionPortfoliosApi.md#get_holdings) | **GET** /api/transactionportfolios/{scope}/{code}/holdings | GetHoldings: Get holdings
*TransactionPortfoliosApi* | [**get_holdings_adjustment**](docs/TransactionPortfoliosApi.md#get_holdings_adjustment) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments/{effectiveAt} | GetHoldingsAdjustment: Get holdings adjustment
*TransactionPortfoliosApi* | [**get_holdings_with_orders**](docs/TransactionPortfoliosApi.md#get_holdings_with_orders) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsWithOrders | GetHoldingsWithOrders: Get holdings with orders
*TransactionPortfoliosApi* | [**get_multiple_holding_contributors**](docs/TransactionPortfoliosApi.md#get_multiple_holding_contributors) | **POST** /api/transactionportfolios/{scope}/{code}/holdings/contributors/$get | GetMultipleHoldingContributors: Get Multiple Holding Contributors
*TransactionPortfoliosApi* | [**get_portfolio_cash_flows**](docs/TransactionPortfoliosApi.md#get_portfolio_cash_flows) | **GET** /api/transactionportfolios/{scope}/{code}/cashflows | GetPortfolioCashFlows: Get portfolio cash flows
*TransactionPortfoliosApi* | [**get_portfolio_cash_ladder**](docs/TransactionPortfoliosApi.md#get_portfolio_cash_ladder) | **GET** /api/transactionportfolios/{scope}/{code}/cashladder | GetPortfolioCashLadder: Get portfolio cash ladder
*TransactionPortfoliosApi* | [**get_portfolio_cash_statement**](docs/TransactionPortfoliosApi.md#get_portfolio_cash_statement) | **GET** /api/transactionportfolios/{scope}/{code}/cashstatement | GetPortfolioCashStatement: Get portfolio cash statement
*TransactionPortfoliosApi* | [**get_transaction_history**](docs/TransactionPortfoliosApi.md#get_transaction_history) | **GET** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/history | GetTransactionHistory: Get the history of a transaction
*TransactionPortfoliosApi* | [**get_transaction_settlement_status**](docs/TransactionPortfoliosApi.md#get_transaction_settlement_status) | **GET** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/settlementstatus | [EARLY ACCESS] GetTransactionSettlementStatus: Gets the Transaction Settlement Status for the requested transaction.
*TransactionPortfoliosApi* | [**get_transactions**](docs/TransactionPortfoliosApi.md#get_transactions) | **GET** /api/transactionportfolios/{scope}/{code}/transactions | GetTransactions: Get transactions
*TransactionPortfoliosApi* | [**get_upsertable_portfolio_cash_flows**](docs/TransactionPortfoliosApi.md#get_upsertable_portfolio_cash_flows) | **GET** /api/transactionportfolios/{scope}/{code}/upsertablecashflows | GetUpsertablePortfolioCashFlows: Get upsertable portfolio cash flows.
*TransactionPortfoliosApi* | [**list_custodian_accounts**](docs/TransactionPortfoliosApi.md#list_custodian_accounts) | **GET** /api/transactionportfolios/{scope}/{code}/custodianaccounts | ListCustodianAccounts: List Custodian Accounts
*TransactionPortfoliosApi* | [**list_holdings_adjustments**](docs/TransactionPortfoliosApi.md#list_holdings_adjustments) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments | ListHoldingsAdjustments: List holdings adjustments
*TransactionPortfoliosApi* | [**list_settlement_instructions**](docs/TransactionPortfoliosApi.md#list_settlement_instructions) | **GET** /api/transactionportfolios/{scope}/{code}/settlementinstructions | [EARLY ACCESS] ListSettlementInstructions: List Settlement Instructions.
*TransactionPortfoliosApi* | [**patch_portfolio_details**](docs/TransactionPortfoliosApi.md#patch_portfolio_details) | **PATCH** /api/transactionportfolios/{scope}/{code}/details | PatchPortfolioDetails: Patch portfolio details
*TransactionPortfoliosApi* | [**preview_transaction**](docs/TransactionPortfoliosApi.md#preview_transaction) | **POST** /api/transactionportfolios/{scope}/{code}/previewTransaction | PreviewTransaction: Preview a transaction
*TransactionPortfoliosApi* | [**resolve_instrument**](docs/TransactionPortfoliosApi.md#resolve_instrument) | **POST** /api/transactionportfolios/{scope}/{code}/$resolve | ResolveInstrument: Resolve instrument
*TransactionPortfoliosApi* | [**set_holdings**](docs/TransactionPortfoliosApi.md#set_holdings) | **PUT** /api/transactionportfolios/{scope}/{code}/holdings | SetHoldings: Set holdings
*TransactionPortfoliosApi* | [**upsert_custodian_accounts**](docs/TransactionPortfoliosApi.md#upsert_custodian_accounts) | **POST** /api/transactionportfolios/{scope}/{code}/custodianaccounts | UpsertCustodianAccounts: Upsert Custodian Accounts
*TransactionPortfoliosApi* | [**upsert_custodian_accounts_properties**](docs/TransactionPortfoliosApi.md#upsert_custodian_accounts_properties) | **POST** /api/transactionportfolios/{scope}/{code}/custodianaccounts/{custodianAccountScope}/{custodianAccountCode}/properties/$upsert | UpsertCustodianAccountsProperties: Upsert custodian accounts properties
*TransactionPortfoliosApi* | [**upsert_portfolio_details**](docs/TransactionPortfoliosApi.md#upsert_portfolio_details) | **POST** /api/transactionportfolios/{scope}/{code}/details | UpsertPortfolioDetails: Upsert portfolio details
*TransactionPortfoliosApi* | [**upsert_settlement_instructions**](docs/TransactionPortfoliosApi.md#upsert_settlement_instructions) | **POST** /api/transactionportfolios/{scope}/{code}/settlementinstructions | [EARLY ACCESS] UpsertSettlementInstructions: Upsert Settlement Instructions.
*TransactionPortfoliosApi* | [**upsert_transaction_properties**](docs/TransactionPortfoliosApi.md#upsert_transaction_properties) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | UpsertTransactionProperties: Upsert transaction properties
*TransactionPortfoliosApi* | [**upsert_transactions**](docs/TransactionPortfoliosApi.md#upsert_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions | UpsertTransactions: Upsert transactions
*TransferAgencyApi* | [**calculate_order_dates**](docs/TransferAgencyApi.md#calculate_order_dates) | **POST** /api/transferagency/orderdates | [EXPERIMENTAL] CalculateOrderDates: Calculate the key dates associated with transfer agency orders
*TranslationApi* | [**translate_instrument_definitions**](docs/TranslationApi.md#translate_instrument_definitions) | **POST** /api/translation/instrumentdefinitions | [EXPERIMENTAL] TranslateInstrumentDefinitions: Translate instruments
*TranslationApi* | [**translate_trade_tickets**](docs/TranslationApi.md#translate_trade_tickets) | **POST** /api/translation/tradetickets | [EXPERIMENTAL] TranslateTradeTickets: Translate trade ticket
*WorkspaceApi* | [**create_item**](docs/WorkspaceApi.md#create_item) | **POST** /api/workspaces/{visibility}/{workspaceName}/items | [EXPERIMENTAL] CreateItem: Create a new item in a workspace.
*WorkspaceApi* | [**create_workspace**](docs/WorkspaceApi.md#create_workspace) | **POST** /api/workspaces/{visibility} | [EXPERIMENTAL] CreateWorkspace: Create a new workspace.
*WorkspaceApi* | [**delete_item**](docs/WorkspaceApi.md#delete_item) | **DELETE** /api/workspaces/{visibility}/{workspaceName}/items/{groupName}/{itemName} | [EXPERIMENTAL] DeleteItem: Delete an item from a workspace.
*WorkspaceApi* | [**delete_workspace**](docs/WorkspaceApi.md#delete_workspace) | **DELETE** /api/workspaces/{visibility}/{workspaceName} | [EXPERIMENTAL] DeleteWorkspace: Delete a workspace.
*WorkspaceApi* | [**get_item**](docs/WorkspaceApi.md#get_item) | **GET** /api/workspaces/{visibility}/{workspaceName}/items/{groupName}/{itemName} | [EXPERIMENTAL] GetItem: Get a single workspace item.
*WorkspaceApi* | [**get_workspace**](docs/WorkspaceApi.md#get_workspace) | **GET** /api/workspaces/{visibility}/{workspaceName} | [EXPERIMENTAL] GetWorkspace: Get a workspace.
*WorkspaceApi* | [**list_items**](docs/WorkspaceApi.md#list_items) | **GET** /api/workspaces/{visibility}/{workspaceName}/items | [EXPERIMENTAL] ListItems: List the items in a workspace.
*WorkspaceApi* | [**list_workspaces**](docs/WorkspaceApi.md#list_workspaces) | **GET** /api/workspaces/{visibility} | [EXPERIMENTAL] ListWorkspaces: List workspaces.
*WorkspaceApi* | [**search_items**](docs/WorkspaceApi.md#search_items) | **GET** /api/workspaces/{visibility}/items | [EXPERIMENTAL] SearchItems: List items across all workspaces.
*WorkspaceApi* | [**update_item**](docs/WorkspaceApi.md#update_item) | **PUT** /api/workspaces/{visibility}/{workspaceName}/items/{groupName}/{itemName} | [EXPERIMENTAL] UpdateItem: Update an item in a workspace.
*WorkspaceApi* | [**update_workspace**](docs/WorkspaceApi.md#update_workspace) | **PUT** /api/workspaces/{visibility}/{workspaceName} | [EXPERIMENTAL] UpdateWorkspace: Update a workspace.


<a id="documentation-for-models"></a>
## Documentation for Models

 - [A2BBreakdown](docs/A2BBreakdown.md)
 - [A2BCategory](docs/A2BCategory.md)
 - [A2BDataRecord](docs/A2BDataRecord.md)
 - [A2BMovementRecord](docs/A2BMovementRecord.md)
 - [Abor](docs/Abor.md)
 - [AborConfiguration](docs/AborConfiguration.md)
 - [AborConfigurationProperties](docs/AborConfigurationProperties.md)
 - [AborConfigurationRequest](docs/AborConfigurationRequest.md)
 - [AborProperties](docs/AborProperties.md)
 - [AborRequest](docs/AborRequest.md)
 - [AcceptEstimateValuationPointResponse](docs/AcceptEstimateValuationPointResponse.md)
 - [AccessControlledAction](docs/AccessControlledAction.md)
 - [AccessControlledResource](docs/AccessControlledResource.md)
 - [AccessMetadataOperation](docs/AccessMetadataOperation.md)
 - [AccessMetadataValue](docs/AccessMetadataValue.md)
 - [Account](docs/Account.md)
 - [AccountHolder](docs/AccountHolder.md)
 - [AccountHolderIdentifier](docs/AccountHolderIdentifier.md)
 - [AccountProperties](docs/AccountProperties.md)
 - [AccountedTransaction](docs/AccountedTransaction.md)
 - [AccountingMethod](docs/AccountingMethod.md)
 - [AccountsUpsertResponse](docs/AccountsUpsertResponse.md)
 - [AccumulationEvent](docs/AccumulationEvent.md)
 - [ActionId](docs/ActionId.md)
 - [AddBusinessDaysToDateRequest](docs/AddBusinessDaysToDateRequest.md)
 - [AddBusinessDaysToDateResponse](docs/AddBusinessDaysToDateResponse.md)
 - [AdditionalPayment](docs/AdditionalPayment.md)
 - [AddressDefinition](docs/AddressDefinition.md)
 - [AddressKeyComplianceParameter](docs/AddressKeyComplianceParameter.md)
 - [AddressKeyDefinition](docs/AddressKeyDefinition.md)
 - [AddressKeyFilter](docs/AddressKeyFilter.md)
 - [AddressKeyList](docs/AddressKeyList.md)
 - [AddressKeyListComplianceParameter](docs/AddressKeyListComplianceParameter.md)
 - [AddressKeyOptionDefinition](docs/AddressKeyOptionDefinition.md)
 - [AdjustGlobalCommitmentEvent](docs/AdjustGlobalCommitmentEvent.md)
 - [AdjustHolding](docs/AdjustHolding.md)
 - [AdjustHoldingForDateRequest](docs/AdjustHoldingForDateRequest.md)
 - [AdjustHoldingRequest](docs/AdjustHoldingRequest.md)
 - [AggregateSpec](docs/AggregateSpec.md)
 - [AggregatedReturn](docs/AggregatedReturn.md)
 - [AggregatedReturnsDispersionRequest](docs/AggregatedReturnsDispersionRequest.md)
 - [AggregatedReturnsRequest](docs/AggregatedReturnsRequest.md)
 - [AggregatedReturnsResponse](docs/AggregatedReturnsResponse.md)
 - [AggregatedTransactionsRequest](docs/AggregatedTransactionsRequest.md)
 - [AggregationContext](docs/AggregationContext.md)
 - [AggregationMeasureFailureDetail](docs/AggregationMeasureFailureDetail.md)
 - [AggregationOp](docs/AggregationOp.md)
 - [AggregationOptions](docs/AggregationOptions.md)
 - [AggregationQuery](docs/AggregationQuery.md)
 - [AggregationType](docs/AggregationType.md)
 - [Alias](docs/Alias.md)
 - [Allocation](docs/Allocation.md)
 - [AllocationRequest](docs/AllocationRequest.md)
 - [AllocationServiceRunResponse](docs/AllocationServiceRunResponse.md)
 - [AllocationSetRequest](docs/AllocationSetRequest.md)
 - [AmortisationEvent](docs/AmortisationEvent.md)
 - [AmortisationRule](docs/AmortisationRule.md)
 - [AmortisationRuleSet](docs/AmortisationRuleSet.md)
 - [Amount](docs/Amount.md)
 - [AnnulQuotesResponse](docs/AnnulQuotesResponse.md)
 - [AnnulSingleStructuredDataResponse](docs/AnnulSingleStructuredDataResponse.md)
 - [AnnulStructuredDataResponse](docs/AnnulStructuredDataResponse.md)
 - [AppendComplexMarketDataRequest](docs/AppendComplexMarketDataRequest.md)
 - [AppendFxForwardCurveByQuoteReference](docs/AppendFxForwardCurveByQuoteReference.md)
 - [AppendFxForwardCurveData](docs/AppendFxForwardCurveData.md)
 - [AppendFxForwardPipsCurveData](docs/AppendFxForwardPipsCurveData.md)
 - [AppendFxForwardTenorCurveData](docs/AppendFxForwardTenorCurveData.md)
 - [AppendFxForwardTenorPipsCurveData](docs/AppendFxForwardTenorPipsCurveData.md)
 - [AppendMarketData](docs/AppendMarketData.md)
 - [AppendMarketDataType](docs/AppendMarketDataType.md)
 - [ApplicableEntity](docs/ApplicableEntity.md)
 - [ApplicableEntityTypes](docs/ApplicableEntityTypes.md)
 - [ApplicableInstrumentEvent](docs/ApplicableInstrumentEvent.md)
 - [AssetClass](docs/AssetClass.md)
 - [AssetLeg](docs/AssetLeg.md)
 - [Barrier](docs/Barrier.md)
 - [Basket](docs/Basket.md)
 - [BasketIdentifier](docs/BasketIdentifier.md)
 - [BatchAdjustHoldingsResponse](docs/BatchAdjustHoldingsResponse.md)
 - [BatchAmendCustomDataModelMembershipResponse](docs/BatchAmendCustomDataModelMembershipResponse.md)
 - [BatchDeleteRelationalDataResponse](docs/BatchDeleteRelationalDataResponse.md)
 - [BatchUpdateUserReviewForComparisonResultRequest](docs/BatchUpdateUserReviewForComparisonResultRequest.md)
 - [BatchUpdateUserReviewForComparisonResultResponse](docs/BatchUpdateUserReviewForComparisonResultResponse.md)
 - [BatchUpsertDatesForCalendarResponse](docs/BatchUpsertDatesForCalendarResponse.md)
 - [BatchUpsertInstrumentPropertiesResponse](docs/BatchUpsertInstrumentPropertiesResponse.md)
 - [BatchUpsertPortfolioAccessMetadataRequest](docs/BatchUpsertPortfolioAccessMetadataRequest.md)
 - [BatchUpsertPortfolioAccessMetadataResponse](docs/BatchUpsertPortfolioAccessMetadataResponse.md)
 - [BatchUpsertPortfolioAccessMetadataResponseItem](docs/BatchUpsertPortfolioAccessMetadataResponseItem.md)
 - [BatchUpsertPortfolioTransactionsResponse](docs/BatchUpsertPortfolioTransactionsResponse.md)
 - [BatchUpsertPropertyDefinitionPropertiesResponse](docs/BatchUpsertPropertyDefinitionPropertiesResponse.md)
 - [BatchUpsertRelationalDatasetsResponse](docs/BatchUpsertRelationalDatasetsResponse.md)
 - [BatchUpsertTransactionSettlementInstructionResponse](docs/BatchUpsertTransactionSettlementInstructionResponse.md)
 - [Block](docs/Block.md)
 - [BlockAndOrderIdRequest](docs/BlockAndOrderIdRequest.md)
 - [BlockAndOrders](docs/BlockAndOrders.md)
 - [BlockAndOrdersCreateRequest](docs/BlockAndOrdersCreateRequest.md)
 - [BlockAndOrdersRequest](docs/BlockAndOrdersRequest.md)
 - [BlockRequest](docs/BlockRequest.md)
 - [BlockSetRequest](docs/BlockSetRequest.md)
 - [BlockedOrderRequest](docs/BlockedOrderRequest.md)
 - [Bond](docs/Bond.md)
 - [BondConversionEntry](docs/BondConversionEntry.md)
 - [BondConversionSchedule](docs/BondConversionSchedule.md)
 - [BondCouponEvent](docs/BondCouponEvent.md)
 - [BondDefaultEvent](docs/BondDefaultEvent.md)
 - [BondPrincipalEvent](docs/BondPrincipalEvent.md)
 - [BonusIssueEvent](docs/BonusIssueEvent.md)
 - [BookTransactionsRequest](docs/BookTransactionsRequest.md)
 - [BookTransactionsResponse](docs/BookTransactionsResponse.md)
 - [BoolComplianceParameter](docs/BoolComplianceParameter.md)
 - [BoolListComplianceParameter](docs/BoolListComplianceParameter.md)
 - [BranchStep](docs/BranchStep.md)
 - [BranchStepRequest](docs/BranchStepRequest.md)
 - [BreakCodeSource](docs/BreakCodeSource.md)
 - [Bucket](docs/Bucket.md)
 - [BucketedCashFlowRequest](docs/BucketedCashFlowRequest.md)
 - [BucketedCashFlowResponse](docs/BucketedCashFlowResponse.md)
 - [BucketingSchedule](docs/BucketingSchedule.md)
 - [CalculateOrderDatesRequest](docs/CalculateOrderDatesRequest.md)
 - [CalculateOrderDatesResponse](docs/CalculateOrderDatesResponse.md)
 - [CalculationInfo](docs/CalculationInfo.md)
 - [Calendar](docs/Calendar.md)
 - [CalendarDate](docs/CalendarDate.md)
 - [CalendarDependency](docs/CalendarDependency.md)
 - [CallOnIntermediateSecuritiesEvent](docs/CallOnIntermediateSecuritiesEvent.md)
 - [CancelOrderAndMoveRemainingResult](docs/CancelOrderAndMoveRemainingResult.md)
 - [CancelOrdersAndMoveRemainingRequest](docs/CancelOrdersAndMoveRemainingRequest.md)
 - [CancelOrdersAndMoveRemainingResponse](docs/CancelOrdersAndMoveRemainingResponse.md)
 - [CancelOrdersResponse](docs/CancelOrdersResponse.md)
 - [CancelPlacementsResponse](docs/CancelPlacementsResponse.md)
 - [CancelSingleHoldingAdjustmentRequest](docs/CancelSingleHoldingAdjustmentRequest.md)
 - [CancelledOrderResult](docs/CancelledOrderResult.md)
 - [CancelledPlacementResult](docs/CancelledPlacementResult.md)
 - [CapFloor](docs/CapFloor.md)
 - [CapitalDistributionEvent](docs/CapitalDistributionEvent.md)
 - [CapletFloorletCashFlowEvent](docs/CapletFloorletCashFlowEvent.md)
 - [Cash](docs/Cash.md)
 - [CashAndSecurityOfferElection](docs/CashAndSecurityOfferElection.md)
 - [CashDependency](docs/CashDependency.md)
 - [CashDividendEvent](docs/CashDividendEvent.md)
 - [CashElection](docs/CashElection.md)
 - [CashFlowEvent](docs/CashFlowEvent.md)
 - [CashFlowLineage](docs/CashFlowLineage.md)
 - [CashFlowValue](docs/CashFlowValue.md)
 - [CashFlowValueSet](docs/CashFlowValueSet.md)
 - [CashLadderRecord](docs/CashLadderRecord.md)
 - [CashOfferElection](docs/CashOfferElection.md)
 - [CashPerpetual](docs/CashPerpetual.md)
 - [CategorySettlementStatus](docs/CategorySettlementStatus.md)
 - [CdsCreditEvent](docs/CdsCreditEvent.md)
 - [CdsFlowConventions](docs/CdsFlowConventions.md)
 - [CdsIndex](docs/CdsIndex.md)
 - [CdsModelOptions](docs/CdsModelOptions.md)
 - [CdsProtectionDetailSpecification](docs/CdsProtectionDetailSpecification.md)
 - [CdxCreditEvent](docs/CdxCreditEvent.md)
 - [Change](docs/Change.md)
 - [ChangeHistory](docs/ChangeHistory.md)
 - [ChangeHistoryAction](docs/ChangeHistoryAction.md)
 - [ChangeInterval](docs/ChangeInterval.md)
 - [ChangeIntervalWithOrderManagementDetail](docs/ChangeIntervalWithOrderManagementDetail.md)
 - [ChangeItem](docs/ChangeItem.md)
 - [ChartOfAccounts](docs/ChartOfAccounts.md)
 - [ChartOfAccountsProperties](docs/ChartOfAccountsProperties.md)
 - [ChartOfAccountsRequest](docs/ChartOfAccountsRequest.md)
 - [CheckDefinition](docs/CheckDefinition.md)
 - [CheckDefinitionDatasetSchema](docs/CheckDefinitionDatasetSchema.md)
 - [CheckDefinitionRule](docs/CheckDefinitionRule.md)
 - [CheckDefinitionRuleSet](docs/CheckDefinitionRuleSet.md)
 - [CheckStep](docs/CheckStep.md)
 - [CheckStepRequest](docs/CheckStepRequest.md)
 - [CleardownModuleDetails](docs/CleardownModuleDetails.md)
 - [CleardownModuleRequest](docs/CleardownModuleRequest.md)
 - [CleardownModuleResponse](docs/CleardownModuleResponse.md)
 - [CleardownModuleRule](docs/CleardownModuleRule.md)
 - [CleardownModuleRulesUpdatedResponse](docs/CleardownModuleRulesUpdatedResponse.md)
 - [Client](docs/Client.md)
 - [CloseEvent](docs/CloseEvent.md)
 - [ClosePeriodDiaryEntryRequest](docs/ClosePeriodDiaryEntryRequest.md)
 - [ClosedPeriod](docs/ClosedPeriod.md)
 - [Collateral](docs/Collateral.md)
 - [CollateralInstrument](docs/CollateralInstrument.md)
 - [ComparisonAttributeValuePair](docs/ComparisonAttributeValuePair.md)
 - [CompletePortfolio](docs/CompletePortfolio.md)
 - [CompleteRelation](docs/CompleteRelation.md)
 - [CompleteRelationship](docs/CompleteRelationship.md)
 - [ComplexBond](docs/ComplexBond.md)
 - [ComplexMarketData](docs/ComplexMarketData.md)
 - [ComplexMarketDataId](docs/ComplexMarketDataId.md)
 - [ComplianceBreachedOrderInfo](docs/ComplianceBreachedOrderInfo.md)
 - [ComplianceParameter](docs/ComplianceParameter.md)
 - [ComplianceParameterType](docs/ComplianceParameterType.md)
 - [ComplianceRule](docs/ComplianceRule.md)
 - [ComplianceRuleBreakdown](docs/ComplianceRuleBreakdown.md)
 - [ComplianceRuleBreakdownRequest](docs/ComplianceRuleBreakdownRequest.md)
 - [ComplianceRuleResponse](docs/ComplianceRuleResponse.md)
 - [ComplianceRuleResult](docs/ComplianceRuleResult.md)
 - [ComplianceRuleResultDetail](docs/ComplianceRuleResultDetail.md)
 - [ComplianceRuleResultPortfolioDetail](docs/ComplianceRuleResultPortfolioDetail.md)
 - [ComplianceRuleResultV2](docs/ComplianceRuleResultV2.md)
 - [ComplianceRuleTemplate](docs/ComplianceRuleTemplate.md)
 - [ComplianceRuleUpsertRequest](docs/ComplianceRuleUpsertRequest.md)
 - [ComplianceRuleUpsertResponse](docs/ComplianceRuleUpsertResponse.md)
 - [ComplianceRunConfiguration](docs/ComplianceRunConfiguration.md)
 - [ComplianceRunInfo](docs/ComplianceRunInfo.md)
 - [ComplianceRunInfoV2](docs/ComplianceRunInfoV2.md)
 - [ComplianceStep](docs/ComplianceStep.md)
 - [ComplianceStepRequest](docs/ComplianceStepRequest.md)
 - [ComplianceStepType](docs/ComplianceStepType.md)
 - [ComplianceStepTypeRequest](docs/ComplianceStepTypeRequest.md)
 - [ComplianceSummaryRuleResult](docs/ComplianceSummaryRuleResult.md)
 - [ComplianceSummaryRuleResultRequest](docs/ComplianceSummaryRuleResultRequest.md)
 - [ComplianceTemplate](docs/ComplianceTemplate.md)
 - [ComplianceTemplateParameter](docs/ComplianceTemplateParameter.md)
 - [ComplianceTemplateVariation](docs/ComplianceTemplateVariation.md)
 - [ComplianceTemplateVariationDto](docs/ComplianceTemplateVariationDto.md)
 - [ComplianceTemplateVariationRequest](docs/ComplianceTemplateVariationRequest.md)
 - [ComponentFilter](docs/ComponentFilter.md)
 - [ComponentTransaction](docs/ComponentTransaction.md)
 - [CompositeBreakdown](docs/CompositeBreakdown.md)
 - [CompositeBreakdownRequest](docs/CompositeBreakdownRequest.md)
 - [CompositeBreakdownResponse](docs/CompositeBreakdownResponse.md)
 - [CompositeDispersion](docs/CompositeDispersion.md)
 - [CompositeDispersionResponse](docs/CompositeDispersionResponse.md)
 - [Compounding](docs/Compounding.md)
 - [ConfigurationRecipe](docs/ConfigurationRecipe.md)
 - [ConstantVolatilitySurface](docs/ConstantVolatilitySurface.md)
 - [ConstituentsAdjustmentHeader](docs/ConstituentsAdjustmentHeader.md)
 - [ContractDetails](docs/ContractDetails.md)
 - [ContractForDifference](docs/ContractForDifference.md)
 - [ContractInitialisationEvent](docs/ContractInitialisationEvent.md)
 - [ContributionToNonPassingRuleDetail](docs/ContributionToNonPassingRuleDetail.md)
 - [ConversionEvent](docs/ConversionEvent.md)
 - [CorporateAction](docs/CorporateAction.md)
 - [CorporateActionSource](docs/CorporateActionSource.md)
 - [CorporateActionTransition](docs/CorporateActionTransition.md)
 - [CorporateActionTransitionComponent](docs/CorporateActionTransitionComponent.md)
 - [CorporateActionTransitionComponentRequest](docs/CorporateActionTransitionComponentRequest.md)
 - [CorporateActionTransitionRequest](docs/CorporateActionTransitionRequest.md)
 - [CounterpartyAgreement](docs/CounterpartyAgreement.md)
 - [CounterpartyRiskInformation](docs/CounterpartyRiskInformation.md)
 - [CounterpartySignatory](docs/CounterpartySignatory.md)
 - [CreateAddressKeyDefinitionRequest](docs/CreateAddressKeyDefinitionRequest.md)
 - [CreateAmortisationRuleSetRequest](docs/CreateAmortisationRuleSetRequest.md)
 - [CreateCalendarRequest](docs/CreateCalendarRequest.md)
 - [CreateCheckDefinitionRequest](docs/CreateCheckDefinitionRequest.md)
 - [CreateClosedPeriodRequest](docs/CreateClosedPeriodRequest.md)
 - [CreateComplianceTemplateRequest](docs/CreateComplianceTemplateRequest.md)
 - [CreateCorporateActionSourceRequest](docs/CreateCorporateActionSourceRequest.md)
 - [CreateCustomDataModelRequest](docs/CreateCustomDataModelRequest.md)
 - [CreateCustomEntityTypeRequest](docs/CreateCustomEntityTypeRequest.md)
 - [CreateCutLabelDefinitionRequest](docs/CreateCutLabelDefinitionRequest.md)
 - [CreateDataMapRequest](docs/CreateDataMapRequest.md)
 - [CreateDataTypeRequest](docs/CreateDataTypeRequest.md)
 - [CreateDateRequest](docs/CreateDateRequest.md)
 - [CreateDerivedPropertyDefinitionRequest](docs/CreateDerivedPropertyDefinitionRequest.md)
 - [CreateDerivedTransactionPortfolioRequest](docs/CreateDerivedTransactionPortfolioRequest.md)
 - [CreateGroupReconciliationComparisonRulesetRequest](docs/CreateGroupReconciliationComparisonRulesetRequest.md)
 - [CreateGroupReconciliationDefinitionRequest](docs/CreateGroupReconciliationDefinitionRequest.md)
 - [CreateIdentifierDefinitionRequest](docs/CreateIdentifierDefinitionRequest.md)
 - [CreatePortfolioDetails](docs/CreatePortfolioDetails.md)
 - [CreatePortfolioGroupRequest](docs/CreatePortfolioGroupRequest.md)
 - [CreatePropertyDefinitionRequest](docs/CreatePropertyDefinitionRequest.md)
 - [CreateRecipeRequest](docs/CreateRecipeRequest.md)
 - [CreateReconciliationRequest](docs/CreateReconciliationRequest.md)
 - [CreateReferencePortfolioRequest](docs/CreateReferencePortfolioRequest.md)
 - [CreateRelationDefinitionRequest](docs/CreateRelationDefinitionRequest.md)
 - [CreateRelationRequest](docs/CreateRelationRequest.md)
 - [CreateRelationalDatasetDefinitionRequest](docs/CreateRelationalDatasetDefinitionRequest.md)
 - [CreateRelationshipDefinitionRequest](docs/CreateRelationshipDefinitionRequest.md)
 - [CreateRelationshipRequest](docs/CreateRelationshipRequest.md)
 - [CreateSequenceRequest](docs/CreateSequenceRequest.md)
 - [CreateSeriesIdentifierField](docs/CreateSeriesIdentifierField.md)
 - [CreateSimplePositionPortfolioRequest](docs/CreateSimplePositionPortfolioRequest.md)
 - [CreateStagingRuleSetRequest](docs/CreateStagingRuleSetRequest.md)
 - [CreateTaxRuleSetRequest](docs/CreateTaxRuleSetRequest.md)
 - [CreateTimelineRequest](docs/CreateTimelineRequest.md)
 - [CreateTradeTicketsResponse](docs/CreateTradeTicketsResponse.md)
 - [CreateTransactionPortfolioRequest](docs/CreateTransactionPortfolioRequest.md)
 - [CreateUnitDefinition](docs/CreateUnitDefinition.md)
 - [CreditDefaultSwap](docs/CreditDefaultSwap.md)
 - [CreditPremiumCashFlowEvent](docs/CreditPremiumCashFlowEvent.md)
 - [CreditRating](docs/CreditRating.md)
 - [CreditSpreadCurveData](docs/CreditSpreadCurveData.md)
 - [CreditSupportAnnex](docs/CreditSupportAnnex.md)
 - [CriterionType](docs/CriterionType.md)
 - [CurrencyAndAmount](docs/CurrencyAndAmount.md)
 - [CurveOptions](docs/CurveOptions.md)
 - [CustodianAccount](docs/CustodianAccount.md)
 - [CustodianAccountProperties](docs/CustodianAccountProperties.md)
 - [CustodianAccountRequest](docs/CustodianAccountRequest.md)
 - [CustodianAccountsUpsertResponse](docs/CustodianAccountsUpsertResponse.md)
 - [CustomDataModel](docs/CustomDataModel.md)
 - [CustomDataModelCriteria](docs/CustomDataModelCriteria.md)
 - [CustomDataModelIdentifierTypeSpecification](docs/CustomDataModelIdentifierTypeSpecification.md)
 - [CustomDataModelIdentifierTypeSpecificationWithDisplayName](docs/CustomDataModelIdentifierTypeSpecificationWithDisplayName.md)
 - [CustomDataModelPropertySpecification](docs/CustomDataModelPropertySpecification.md)
 - [CustomDataModelPropertySpecificationWithDisplayName](docs/CustomDataModelPropertySpecificationWithDisplayName.md)
 - [CustomEntityDefinition](docs/CustomEntityDefinition.md)
 - [CustomEntityDefinitionRequest](docs/CustomEntityDefinitionRequest.md)
 - [CustomEntityEntity](docs/CustomEntityEntity.md)
 - [CustomEntityField](docs/CustomEntityField.md)
 - [CustomEntityFieldDefinition](docs/CustomEntityFieldDefinition.md)
 - [CustomEntityId](docs/CustomEntityId.md)
 - [CustomEntityProperties](docs/CustomEntityProperties.md)
 - [CustomEntityRequest](docs/CustomEntityRequest.md)
 - [CustomEntityResponse](docs/CustomEntityResponse.md)
 - [CustomEntityType](docs/CustomEntityType.md)
 - [CustomSortBy](docs/CustomSortBy.md)
 - [CutLabelDefinition](docs/CutLabelDefinition.md)
 - [CutLocalTime](docs/CutLocalTime.md)
 - [DataDefinition](docs/DataDefinition.md)
 - [DataMapKey](docs/DataMapKey.md)
 - [DataMapping](docs/DataMapping.md)
 - [DataModelMembership](docs/DataModelMembership.md)
 - [DataModelSummary](docs/DataModelSummary.md)
 - [DataPointVersion](docs/DataPointVersion.md)
 - [DataQualityCheckResult](docs/DataQualityCheckResult.md)
 - [DataScope](docs/DataScope.md)
 - [DataSeries](docs/DataSeries.md)
 - [DataType](docs/DataType.md)
 - [DataTypeEntity](docs/DataTypeEntity.md)
 - [DataTypeSummary](docs/DataTypeSummary.md)
 - [DataTypeValueRange](docs/DataTypeValueRange.md)
 - [DateAttributes](docs/DateAttributes.md)
 - [DateOrDiaryEntry](docs/DateOrDiaryEntry.md)
 - [DateRange](docs/DateRange.md)
 - [DateTimeComparisonType](docs/DateTimeComparisonType.md)
 - [DateTimeComplianceParameter](docs/DateTimeComplianceParameter.md)
 - [DateTimeListComplianceParameter](docs/DateTimeListComplianceParameter.md)
 - [DayMonth](docs/DayMonth.md)
 - [DayOfWeek](docs/DayOfWeek.md)
 - [DecimalComplianceParameter](docs/DecimalComplianceParameter.md)
 - [DecimalList](docs/DecimalList.md)
 - [DecimalListComplianceParameter](docs/DecimalListComplianceParameter.md)
 - [DecoratedComplianceRunSummary](docs/DecoratedComplianceRunSummary.md)
 - [DeleteAccountsResponse](docs/DeleteAccountsResponse.md)
 - [DeleteCustodianAccountsResponse](docs/DeleteCustodianAccountsResponse.md)
 - [DeleteDataQualityRule](docs/DeleteDataQualityRule.md)
 - [DeleteInstrumentPropertiesResponse](docs/DeleteInstrumentPropertiesResponse.md)
 - [DeleteInstrumentResponse](docs/DeleteInstrumentResponse.md)
 - [DeleteInstrumentsResponse](docs/DeleteInstrumentsResponse.md)
 - [DeleteModes](docs/DeleteModes.md)
 - [DeleteRelationRequest](docs/DeleteRelationRequest.md)
 - [DeleteRelationalDataPointRequest](docs/DeleteRelationalDataPointRequest.md)
 - [DeleteRelationshipRequest](docs/DeleteRelationshipRequest.md)
 - [DeletedEntityResponse](docs/DeletedEntityResponse.md)
 - [DependencySourceFilter](docs/DependencySourceFilter.md)
 - [DepositCloseEvent](docs/DepositCloseEvent.md)
 - [DepositInterestPaymentEvent](docs/DepositInterestPaymentEvent.md)
 - [DepositRollEvent](docs/DepositRollEvent.md)
 - [DerivationFormulaExplainRequest](docs/DerivationFormulaExplainRequest.md)
 - [DerivedPropertyComponent](docs/DerivedPropertyComponent.md)
 - [DescribedAddressKey](docs/DescribedAddressKey.md)
 - [Dialect](docs/Dialect.md)
 - [DialectId](docs/DialectId.md)
 - [DialectSchema](docs/DialectSchema.md)
 - [DiaryEntry](docs/DiaryEntry.md)
 - [DiaryEntryRequest](docs/DiaryEntryRequest.md)
 - [DiscountFactorCurveData](docs/DiscountFactorCurveData.md)
 - [DiscountingDependency](docs/DiscountingDependency.md)
 - [DiscountingMethod](docs/DiscountingMethod.md)
 - [DividendOptionEvent](docs/DividendOptionEvent.md)
 - [DividendReinvestmentEvent](docs/DividendReinvestmentEvent.md)
 - [DrawdownEvent](docs/DrawdownEvent.md)
 - [EarlyCloseOutEvent](docs/EarlyCloseOutEvent.md)
 - [EarlyRedemptionElection](docs/EarlyRedemptionElection.md)
 - [EarlyRedemptionEvent](docs/EarlyRedemptionEvent.md)
 - [EconomicDependency](docs/EconomicDependency.md)
 - [EconomicDependencyType](docs/EconomicDependencyType.md)
 - [EconomicDependencyWithComplexMarketData](docs/EconomicDependencyWithComplexMarketData.md)
 - [EconomicDependencyWithQuote](docs/EconomicDependencyWithQuote.md)
 - [Economics](docs/Economics.md)
 - [EffectiveRange](docs/EffectiveRange.md)
 - [ElectionSpecification](docs/ElectionSpecification.md)
 - [EligibilityCalculation](docs/EligibilityCalculation.md)
 - [EmptyModelOptions](docs/EmptyModelOptions.md)
 - [EntityIdentifier](docs/EntityIdentifier.md)
 - [Equity](docs/Equity.md)
 - [EquityAllOfIdentifiers](docs/EquityAllOfIdentifiers.md)
 - [EquityCurveByPricesData](docs/EquityCurveByPricesData.md)
 - [EquityCurveDependency](docs/EquityCurveDependency.md)
 - [EquityModelOptions](docs/EquityModelOptions.md)
 - [EquityOption](docs/EquityOption.md)
 - [EquitySwap](docs/EquitySwap.md)
 - [EquityVolDependency](docs/EquityVolDependency.md)
 - [EquityVolSurfaceData](docs/EquityVolSurfaceData.md)
 - [ErrorDetail](docs/ErrorDetail.md)
 - [EventDateRange](docs/EventDateRange.md)
 - [ExDividendConfiguration](docs/ExDividendConfiguration.md)
 - [ExchangeTradedOption](docs/ExchangeTradedOption.md)
 - [ExchangeTradedOptionContractDetails](docs/ExchangeTradedOptionContractDetails.md)
 - [Execution](docs/Execution.md)
 - [ExecutionRequest](docs/ExecutionRequest.md)
 - [ExecutionSetRequest](docs/ExecutionSetRequest.md)
 - [ExerciseEvent](docs/ExerciseEvent.md)
 - [ExoticInstrument](docs/ExoticInstrument.md)
 - [ExpandedGroup](docs/ExpandedGroup.md)
 - [ExpiryEvent](docs/ExpiryEvent.md)
 - [ExternalFeeComponentFilter](docs/ExternalFeeComponentFilter.md)
 - [Fee](docs/Fee.md)
 - [FeeAccrual](docs/FeeAccrual.md)
 - [FeeProperties](docs/FeeProperties.md)
 - [FeeRequest](docs/FeeRequest.md)
 - [FeeRule](docs/FeeRule.md)
 - [FeeRuleUpsertRequest](docs/FeeRuleUpsertRequest.md)
 - [FeeRuleUpsertResponse](docs/FeeRuleUpsertResponse.md)
 - [FeeTransactionTemplateSpecification](docs/FeeTransactionTemplateSpecification.md)
 - [FeeType](docs/FeeType.md)
 - [FeeTypeRequest](docs/FeeTypeRequest.md)
 - [FieldDefinition](docs/FieldDefinition.md)
 - [FieldSchema](docs/FieldSchema.md)
 - [FieldValue](docs/FieldValue.md)
 - [FileResponse](docs/FileResponse.md)
 - [FilterPredicateComplianceParameter](docs/FilterPredicateComplianceParameter.md)
 - [FilterStep](docs/FilterStep.md)
 - [FilterStepRequest](docs/FilterStepRequest.md)
 - [FixedLeg](docs/FixedLeg.md)
 - [FixedLegAllOfOverrides](docs/FixedLegAllOfOverrides.md)
 - [FixedSchedule](docs/FixedSchedule.md)
 - [FlexibleDeposit](docs/FlexibleDeposit.md)
 - [FlexibleLoan](docs/FlexibleLoan.md)
 - [FlexibleRepo](docs/FlexibleRepo.md)
 - [FlexibleRepoCashFlowEvent](docs/FlexibleRepoCashFlowEvent.md)
 - [FlexibleRepoCollateralEvent](docs/FlexibleRepoCollateralEvent.md)
 - [FlexibleRepoFullClosureEvent](docs/FlexibleRepoFullClosureEvent.md)
 - [FlexibleRepoInterestPaymentEvent](docs/FlexibleRepoInterestPaymentEvent.md)
 - [FlexibleRepoPartialClosureEvent](docs/FlexibleRepoPartialClosureEvent.md)
 - [FloatSchedule](docs/FloatSchedule.md)
 - [FloatingLeg](docs/FloatingLeg.md)
 - [FlowConventionName](docs/FlowConventionName.md)
 - [FlowConventions](docs/FlowConventions.md)
 - [ForwardRateAgreement](docs/ForwardRateAgreement.md)
 - [FromRecipe](docs/FromRecipe.md)
 - [Fund](docs/Fund.md)
 - [FundAmount](docs/FundAmount.md)
 - [FundCalendarEntry](docs/FundCalendarEntry.md)
 - [FundCalendarEntryType](docs/FundCalendarEntryType.md)
 - [FundConfiguration](docs/FundConfiguration.md)
 - [FundConfigurationProperties](docs/FundConfigurationProperties.md)
 - [FundConfigurationRequest](docs/FundConfigurationRequest.md)
 - [FundDefinitionRequest](docs/FundDefinitionRequest.md)
 - [FundDetails](docs/FundDetails.md)
 - [FundIdList](docs/FundIdList.md)
 - [FundJournalEntryLine](docs/FundJournalEntryLine.md)
 - [FundPnlBreakdown](docs/FundPnlBreakdown.md)
 - [FundPreviousNAV](docs/FundPreviousNAV.md)
 - [FundProperties](docs/FundProperties.md)
 - [FundRequest](docs/FundRequest.md)
 - [FundShareClass](docs/FundShareClass.md)
 - [FundValuationPointData](docs/FundValuationPointData.md)
 - [FundValuationRequest](docs/FundValuationRequest.md)
 - [FundValuationSchedule](docs/FundValuationSchedule.md)
 - [FundingLeg](docs/FundingLeg.md)
 - [FundingLegOptions](docs/FundingLegOptions.md)
 - [Future](docs/Future.md)
 - [FutureExpiryEvent](docs/FutureExpiryEvent.md)
 - [FutureMarkToMarketEvent](docs/FutureMarkToMarketEvent.md)
 - [FuturesContractDetails](docs/FuturesContractDetails.md)
 - [FxConventions](docs/FxConventions.md)
 - [FxDependency](docs/FxDependency.md)
 - [FxForward](docs/FxForward.md)
 - [FxForwardCurveByQuoteReference](docs/FxForwardCurveByQuoteReference.md)
 - [FxForwardCurveData](docs/FxForwardCurveData.md)
 - [FxForwardModelOptions](docs/FxForwardModelOptions.md)
 - [FxForwardPipsCurveData](docs/FxForwardPipsCurveData.md)
 - [FxForwardSettlementEvent](docs/FxForwardSettlementEvent.md)
 - [FxForwardTenorCurveData](docs/FxForwardTenorCurveData.md)
 - [FxForwardTenorPipsCurveData](docs/FxForwardTenorPipsCurveData.md)
 - [FxForwardsDependency](docs/FxForwardsDependency.md)
 - [FxLinkedNotionalSchedule](docs/FxLinkedNotionalSchedule.md)
 - [FxOption](docs/FxOption.md)
 - [FxRateSchedule](docs/FxRateSchedule.md)
 - [FxSwap](docs/FxSwap.md)
 - [FxTenorConvention](docs/FxTenorConvention.md)
 - [FxVolDependency](docs/FxVolDependency.md)
 - [FxVolSurfaceData](docs/FxVolSurfaceData.md)
 - [GeneralLedgerProfileMapping](docs/GeneralLedgerProfileMapping.md)
 - [GeneralLedgerProfileRequest](docs/GeneralLedgerProfileRequest.md)
 - [GeneralLedgerProfileResponse](docs/GeneralLedgerProfileResponse.md)
 - [GeneratedEventDiagnostics](docs/GeneratedEventDiagnostics.md)
 - [GetCdsFlowConventionsResponse](docs/GetCdsFlowConventionsResponse.md)
 - [GetComplexMarketDataResponse](docs/GetComplexMarketDataResponse.md)
 - [GetCounterpartyAgreementResponse](docs/GetCounterpartyAgreementResponse.md)
 - [GetCreditSupportAnnexResponse](docs/GetCreditSupportAnnexResponse.md)
 - [GetDataMapResponse](docs/GetDataMapResponse.md)
 - [GetFlowConventionsResponse](docs/GetFlowConventionsResponse.md)
 - [GetIndexConventionResponse](docs/GetIndexConventionResponse.md)
 - [GetInstrumentsResponse](docs/GetInstrumentsResponse.md)
 - [GetQuotesResponse](docs/GetQuotesResponse.md)
 - [GetRecipeComposerResponse](docs/GetRecipeComposerResponse.md)
 - [GetRecipeResponse](docs/GetRecipeResponse.md)
 - [GetReferencePortfolioConstituentsResponse](docs/GetReferencePortfolioConstituentsResponse.md)
 - [GetStructuredResultDataResponse](docs/GetStructuredResultDataResponse.md)
 - [GetVirtualDocumentResponse](docs/GetVirtualDocumentResponse.md)
 - [GroupBySelectorComplianceParameter](docs/GroupBySelectorComplianceParameter.md)
 - [GroupByStep](docs/GroupByStep.md)
 - [GroupByStepRequest](docs/GroupByStepRequest.md)
 - [GroupCalculationComplianceParameter](docs/GroupCalculationComplianceParameter.md)
 - [GroupFilterPredicateComplianceParameter](docs/GroupFilterPredicateComplianceParameter.md)
 - [GroupFilterStep](docs/GroupFilterStep.md)
 - [GroupFilterStepRequest](docs/GroupFilterStepRequest.md)
 - [GroupOfMarketDataKeyRules](docs/GroupOfMarketDataKeyRules.md)
 - [GroupReconciliationAggregateAttributeRule](docs/GroupReconciliationAggregateAttributeRule.md)
 - [GroupReconciliationAggregateAttributeValues](docs/GroupReconciliationAggregateAttributeValues.md)
 - [GroupReconciliationAggregateComparisonRuleOperand](docs/GroupReconciliationAggregateComparisonRuleOperand.md)
 - [GroupReconciliationComparisonResult](docs/GroupReconciliationComparisonResult.md)
 - [GroupReconciliationComparisonRuleStringValueMap](docs/GroupReconciliationComparisonRuleStringValueMap.md)
 - [GroupReconciliationComparisonRuleTolerance](docs/GroupReconciliationComparisonRuleTolerance.md)
 - [GroupReconciliationComparisonRuleset](docs/GroupReconciliationComparisonRuleset.md)
 - [GroupReconciliationCoreAttributeRule](docs/GroupReconciliationCoreAttributeRule.md)
 - [GroupReconciliationCoreAttributeValues](docs/GroupReconciliationCoreAttributeValues.md)
 - [GroupReconciliationCoreComparisonRuleOperand](docs/GroupReconciliationCoreComparisonRuleOperand.md)
 - [GroupReconciliationDatePair](docs/GroupReconciliationDatePair.md)
 - [GroupReconciliationDates](docs/GroupReconciliationDates.md)
 - [GroupReconciliationDefinition](docs/GroupReconciliationDefinition.md)
 - [GroupReconciliationDefinitionComparisonRulesetIds](docs/GroupReconciliationDefinitionComparisonRulesetIds.md)
 - [GroupReconciliationDefinitionCurrencies](docs/GroupReconciliationDefinitionCurrencies.md)
 - [GroupReconciliationDefinitionPortfolioEntityIds](docs/GroupReconciliationDefinitionPortfolioEntityIds.md)
 - [GroupReconciliationDefinitionRecipeIds](docs/GroupReconciliationDefinitionRecipeIds.md)
 - [GroupReconciliationInstanceId](docs/GroupReconciliationInstanceId.md)
 - [GroupReconciliationResultStatuses](docs/GroupReconciliationResultStatuses.md)
 - [GroupReconciliationResultTypes](docs/GroupReconciliationResultTypes.md)
 - [GroupReconciliationReviewStatuses](docs/GroupReconciliationReviewStatuses.md)
 - [GroupReconciliationRunDetails](docs/GroupReconciliationRunDetails.md)
 - [GroupReconciliationRunRequest](docs/GroupReconciliationRunRequest.md)
 - [GroupReconciliationRunResponse](docs/GroupReconciliationRunResponse.md)
 - [GroupReconciliationSummary](docs/GroupReconciliationSummary.md)
 - [GroupReconciliationUserReview](docs/GroupReconciliationUserReview.md)
 - [GroupReconciliationUserReviewAdd](docs/GroupReconciliationUserReviewAdd.md)
 - [GroupReconciliationUserReviewBreakCode](docs/GroupReconciliationUserReviewBreakCode.md)
 - [GroupReconciliationUserReviewComment](docs/GroupReconciliationUserReviewComment.md)
 - [GroupReconciliationUserReviewMatchKey](docs/GroupReconciliationUserReviewMatchKey.md)
 - [GroupReconciliationUserReviewRemove](docs/GroupReconciliationUserReviewRemove.md)
 - [GroupedResultOfAddressKey](docs/GroupedResultOfAddressKey.md)
 - [HoldingAdjustment](docs/HoldingAdjustment.md)
 - [HoldingAdjustmentWithDate](docs/HoldingAdjustmentWithDate.md)
 - [HoldingContext](docs/HoldingContext.md)
 - [HoldingContributor](docs/HoldingContributor.md)
 - [HoldingIdsRequest](docs/HoldingIdsRequest.md)
 - [HoldingPricingInfo](docs/HoldingPricingInfo.md)
 - [HoldingsAdjustment](docs/HoldingsAdjustment.md)
 - [HoldingsAdjustmentHeader](docs/HoldingsAdjustmentHeader.md)
 - [IUnitDefinitionDto](docs/IUnitDefinitionDto.md)
 - [IdSelectorDefinition](docs/IdSelectorDefinition.md)
 - [IdentifierDefinition](docs/IdentifierDefinition.md)
 - [IdentifierPartSchema](docs/IdentifierPartSchema.md)
 - [IndexConvention](docs/IndexConvention.md)
 - [IndexModelOptions](docs/IndexModelOptions.md)
 - [IndexProjectionDependency](docs/IndexProjectionDependency.md)
 - [IndustryClassifier](docs/IndustryClassifier.md)
 - [InflationFixingDependency](docs/InflationFixingDependency.md)
 - [InflationIndexConventions](docs/InflationIndexConventions.md)
 - [InflationLeg](docs/InflationLeg.md)
 - [InflationLinkedBond](docs/InflationLinkedBond.md)
 - [InflationSwap](docs/InflationSwap.md)
 - [InformationalErrorEvent](docs/InformationalErrorEvent.md)
 - [InformationalEvent](docs/InformationalEvent.md)
 - [InlineValuationRequest](docs/InlineValuationRequest.md)
 - [InlineValuationsReconciliationRequest](docs/InlineValuationsReconciliationRequest.md)
 - [InputTransition](docs/InputTransition.md)
 - [Instrument](docs/Instrument.md)
 - [InstrumentCapabilities](docs/InstrumentCapabilities.md)
 - [InstrumentCashFlow](docs/InstrumentCashFlow.md)
 - [InstrumentDefinition](docs/InstrumentDefinition.md)
 - [InstrumentDefinitionFormat](docs/InstrumentDefinitionFormat.md)
 - [InstrumentDeleteModes](docs/InstrumentDeleteModes.md)
 - [InstrumentEntity](docs/InstrumentEntity.md)
 - [InstrumentEvent](docs/InstrumentEvent.md)
 - [InstrumentEventConfiguration](docs/InstrumentEventConfiguration.md)
 - [InstrumentEventHolder](docs/InstrumentEventHolder.md)
 - [InstrumentEventInstruction](docs/InstrumentEventInstruction.md)
 - [InstrumentEventInstructionRequest](docs/InstrumentEventInstructionRequest.md)
 - [InstrumentEventInstructionsResponse](docs/InstrumentEventInstructionsResponse.md)
 - [InstrumentEventType](docs/InstrumentEventType.md)
 - [InstrumentIdTypeDescriptor](docs/InstrumentIdTypeDescriptor.md)
 - [InstrumentIdValue](docs/InstrumentIdValue.md)
 - [InstrumentLeg](docs/InstrumentLeg.md)
 - [InstrumentList](docs/InstrumentList.md)
 - [InstrumentListComplianceParameter](docs/InstrumentListComplianceParameter.md)
 - [InstrumentMatch](docs/InstrumentMatch.md)
 - [InstrumentModels](docs/InstrumentModels.md)
 - [InstrumentPaymentDiary](docs/InstrumentPaymentDiary.md)
 - [InstrumentPaymentDiaryLeg](docs/InstrumentPaymentDiaryLeg.md)
 - [InstrumentPaymentDiaryRow](docs/InstrumentPaymentDiaryRow.md)
 - [InstrumentProperties](docs/InstrumentProperties.md)
 - [InstrumentResolutionDetail](docs/InstrumentResolutionDetail.md)
 - [InstrumentSearchProperty](docs/InstrumentSearchProperty.md)
 - [InstrumentType](docs/InstrumentType.md)
 - [InterestRateSwap](docs/InterestRateSwap.md)
 - [InterestRateSwaption](docs/InterestRateSwaption.md)
 - [IntermediateComplianceStep](docs/IntermediateComplianceStep.md)
 - [IntermediateComplianceStepRequest](docs/IntermediateComplianceStepRequest.md)
 - [IntermediateSecuritiesDistributionEvent](docs/IntermediateSecuritiesDistributionEvent.md)
 - [InvestmentAccount](docs/InvestmentAccount.md)
 - [InvestmentPortfolio](docs/InvestmentPortfolio.md)
 - [InvestmentPortfolioIdentifier](docs/InvestmentPortfolioIdentifier.md)
 - [Investor](docs/Investor.md)
 - [InvestorIdentifier](docs/InvestorIdentifier.md)
 - [InvestorRecord](docs/InvestorRecord.md)
 - [IrVolCubeData](docs/IrVolCubeData.md)
 - [IrVolDependency](docs/IrVolDependency.md)
 - [IsBusinessDayResponse](docs/IsBusinessDayResponse.md)
 - [ItemAndWorkspace](docs/ItemAndWorkspace.md)
 - [JournalEntryLine](docs/JournalEntryLine.md)
 - [JournalEntryLineShareClassBreakdown](docs/JournalEntryLineShareClassBreakdown.md)
 - [JournalEntryLinesQueryParameters](docs/JournalEntryLinesQueryParameters.md)
 - [LabelValueSet](docs/LabelValueSet.md)
 - [LapseElection](docs/LapseElection.md)
 - [LegDefinition](docs/LegDefinition.md)
 - [LegalEntity](docs/LegalEntity.md)
 - [LevelStep](docs/LevelStep.md)
 - [LifeCycleEventLineage](docs/LifeCycleEventLineage.md)
 - [LifeCycleEventValue](docs/LifeCycleEventValue.md)
 - [LineageMember](docs/LineageMember.md)
 - [Link](docs/Link.md)
 - [ListAggregationReconciliation](docs/ListAggregationReconciliation.md)
 - [ListAggregationResponse](docs/ListAggregationResponse.md)
 - [ListComplexMarketDataWithMetaDataResponse](docs/ListComplexMarketDataWithMetaDataResponse.md)
 - [LoanFacility](docs/LoanFacility.md)
 - [LoanFacilityContractRolloverEvent](docs/LoanFacilityContractRolloverEvent.md)
 - [LoanInterestRepaymentEvent](docs/LoanInterestRepaymentEvent.md)
 - [LoanPeriod](docs/LoanPeriod.md)
 - [LoanPrincipalRepaymentEvent](docs/LoanPrincipalRepaymentEvent.md)
 - [LockPeriodDiaryEntryRequest](docs/LockPeriodDiaryEntryRequest.md)
 - [LusidEntityDataset](docs/LusidEntityDataset.md)
 - [LusidEntityResult](docs/LusidEntityResult.md)
 - [LusidInstrument](docs/LusidInstrument.md)
 - [LusidProblemDetails](docs/LusidProblemDetails.md)
 - [LusidTradeTicket](docs/LusidTradeTicket.md)
 - [LusidUniqueId](docs/LusidUniqueId.md)
 - [LusidValidationProblemDetails](docs/LusidValidationProblemDetails.md)
 - [MappedString](docs/MappedString.md)
 - [Mapping](docs/Mapping.md)
 - [MappingRule](docs/MappingRule.md)
 - [MarkToMarketConventions](docs/MarkToMarketConventions.md)
 - [MarketContext](docs/MarketContext.md)
 - [MarketContextSuppliers](docs/MarketContextSuppliers.md)
 - [MarketDataKeyRule](docs/MarketDataKeyRule.md)
 - [MarketDataOptions](docs/MarketDataOptions.md)
 - [MarketDataOptionsType](docs/MarketDataOptionsType.md)
 - [MarketDataOverrides](docs/MarketDataOverrides.md)
 - [MarketDataSpecificRule](docs/MarketDataSpecificRule.md)
 - [MarketDataType](docs/MarketDataType.md)
 - [MarketObservableType](docs/MarketObservableType.md)
 - [MarketOptions](docs/MarketOptions.md)
 - [MarketQuote](docs/MarketQuote.md)
 - [MasteredInstrument](docs/MasteredInstrument.md)
 - [MatchCriterion](docs/MatchCriterion.md)
 - [MaturityEvent](docs/MaturityEvent.md)
 - [MbsCouponEvent](docs/MbsCouponEvent.md)
 - [MbsInterestDeferralEvent](docs/MbsInterestDeferralEvent.md)
 - [MbsInterestShortfallEvent](docs/MbsInterestShortfallEvent.md)
 - [MbsPrincipalEvent](docs/MbsPrincipalEvent.md)
 - [MbsPrincipalWriteOffEvent](docs/MbsPrincipalWriteOffEvent.md)
 - [Membership](docs/Membership.md)
 - [MembershipAmendmentRequest](docs/MembershipAmendmentRequest.md)
 - [MembershipAmendmentResponse](docs/MembershipAmendmentResponse.md)
 - [MembershipAndStatus](docs/MembershipAndStatus.md)
 - [MergerEvent](docs/MergerEvent.md)
 - [MetricValue](docs/MetricValue.md)
 - [ModelOptions](docs/ModelOptions.md)
 - [ModelOptionsType](docs/ModelOptionsType.md)
 - [ModelProperty](docs/ModelProperty.md)
 - [ModelSchema](docs/ModelSchema.md)
 - [ModelSelection](docs/ModelSelection.md)
 - [MoveOrdersToDifferentBlocksRequest](docs/MoveOrdersToDifferentBlocksRequest.md)
 - [MovedOrderToDifferentBlockResponse](docs/MovedOrderToDifferentBlockResponse.md)
 - [MovementSettlementSummary](docs/MovementSettlementSummary.md)
 - [MovementType](docs/MovementType.md)
 - [MultiCurrencyAmounts](docs/MultiCurrencyAmounts.md)
 - [NavActivityAdjustment](docs/NavActivityAdjustment.md)
 - [NavActivityAdjustmentType](docs/NavActivityAdjustmentType.md)
 - [NavTypeDefinition](docs/NavTypeDefinition.md)
 - [NewInstrument](docs/NewInstrument.md)
 - [NextValueInSequenceResponse](docs/NextValueInSequenceResponse.md)
 - [NumericComparisonType](docs/NumericComparisonType.md)
 - [OpaqueDependency](docs/OpaqueDependency.md)
 - [OpaqueMarketData](docs/OpaqueMarketData.md)
 - [OpaqueModelOptions](docs/OpaqueModelOptions.md)
 - [OpenEvent](docs/OpenEvent.md)
 - [OperandType](docs/OperandType.md)
 - [Operation](docs/Operation.md)
 - [OperationType](docs/OperationType.md)
 - [Operator](docs/Operator.md)
 - [OptionEntry](docs/OptionEntry.md)
 - [OptionExerciseCashEvent](docs/OptionExerciseCashEvent.md)
 - [OptionExerciseElection](docs/OptionExerciseElection.md)
 - [OptionExercisePhysicalEvent](docs/OptionExercisePhysicalEvent.md)
 - [OptionalitySchedule](docs/OptionalitySchedule.md)
 - [Order](docs/Order.md)
 - [OrderBreachHistory](docs/OrderBreachHistory.md)
 - [OrderBySpec](docs/OrderBySpec.md)
 - [OrderFlowConfiguration](docs/OrderFlowConfiguration.md)
 - [OrderGraphBlock](docs/OrderGraphBlock.md)
 - [OrderGraphBlockAllocationDetail](docs/OrderGraphBlockAllocationDetail.md)
 - [OrderGraphBlockAllocationSynopsis](docs/OrderGraphBlockAllocationSynopsis.md)
 - [OrderGraphBlockExecutionDetail](docs/OrderGraphBlockExecutionDetail.md)
 - [OrderGraphBlockExecutionSynopsis](docs/OrderGraphBlockExecutionSynopsis.md)
 - [OrderGraphBlockOrderDetail](docs/OrderGraphBlockOrderDetail.md)
 - [OrderGraphBlockOrderSynopsis](docs/OrderGraphBlockOrderSynopsis.md)
 - [OrderGraphBlockPlacementDetail](docs/OrderGraphBlockPlacementDetail.md)
 - [OrderGraphBlockPlacementSynopsis](docs/OrderGraphBlockPlacementSynopsis.md)
 - [OrderGraphBlockTransactionDetail](docs/OrderGraphBlockTransactionDetail.md)
 - [OrderGraphBlockTransactionSynopsis](docs/OrderGraphBlockTransactionSynopsis.md)
 - [OrderGraphPlacement](docs/OrderGraphPlacement.md)
 - [OrderGraphPlacementAllocationDetail](docs/OrderGraphPlacementAllocationDetail.md)
 - [OrderGraphPlacementAllocationSynopsis](docs/OrderGraphPlacementAllocationSynopsis.md)
 - [OrderGraphPlacementChildPlacementDetail](docs/OrderGraphPlacementChildPlacementDetail.md)
 - [OrderGraphPlacementExecutionDetail](docs/OrderGraphPlacementExecutionDetail.md)
 - [OrderGraphPlacementExecutionSynopsis](docs/OrderGraphPlacementExecutionSynopsis.md)
 - [OrderGraphPlacementOrderDetail](docs/OrderGraphPlacementOrderDetail.md)
 - [OrderGraphPlacementOrderSynopsis](docs/OrderGraphPlacementOrderSynopsis.md)
 - [OrderGraphPlacementPlacementSynopsis](docs/OrderGraphPlacementPlacementSynopsis.md)
 - [OrderInstruction](docs/OrderInstruction.md)
 - [OrderInstructionRequest](docs/OrderInstructionRequest.md)
 - [OrderInstructionSetRequest](docs/OrderInstructionSetRequest.md)
 - [OrderRequest](docs/OrderRequest.md)
 - [OrderRuleBreach](docs/OrderRuleBreach.md)
 - [OrderSetRequest](docs/OrderSetRequest.md)
 - [OrderUpdateRequest](docs/OrderUpdateRequest.md)
 - [OtcConfirmation](docs/OtcConfirmation.md)
 - [OutputTransaction](docs/OutputTransaction.md)
 - [OutputTransition](docs/OutputTransition.md)
 - [Package](docs/Package.md)
 - [PackageRequest](docs/PackageRequest.md)
 - [PackageSetRequest](docs/PackageSetRequest.md)
 - [PagedResourceListOfAbor](docs/PagedResourceListOfAbor.md)
 - [PagedResourceListOfAborConfiguration](docs/PagedResourceListOfAborConfiguration.md)
 - [PagedResourceListOfAccount](docs/PagedResourceListOfAccount.md)
 - [PagedResourceListOfAddressKeyDefinition](docs/PagedResourceListOfAddressKeyDefinition.md)
 - [PagedResourceListOfAllocation](docs/PagedResourceListOfAllocation.md)
 - [PagedResourceListOfAmortisationRuleSet](docs/PagedResourceListOfAmortisationRuleSet.md)
 - [PagedResourceListOfBlock](docs/PagedResourceListOfBlock.md)
 - [PagedResourceListOfCalendar](docs/PagedResourceListOfCalendar.md)
 - [PagedResourceListOfChartOfAccounts](docs/PagedResourceListOfChartOfAccounts.md)
 - [PagedResourceListOfCheckDefinition](docs/PagedResourceListOfCheckDefinition.md)
 - [PagedResourceListOfCleardownModuleResponse](docs/PagedResourceListOfCleardownModuleResponse.md)
 - [PagedResourceListOfCleardownModuleRule](docs/PagedResourceListOfCleardownModuleRule.md)
 - [PagedResourceListOfClosedPeriod](docs/PagedResourceListOfClosedPeriod.md)
 - [PagedResourceListOfComplianceRuleResponse](docs/PagedResourceListOfComplianceRuleResponse.md)
 - [PagedResourceListOfComplianceRunInfoV2](docs/PagedResourceListOfComplianceRunInfoV2.md)
 - [PagedResourceListOfComplianceTemplate](docs/PagedResourceListOfComplianceTemplate.md)
 - [PagedResourceListOfCorporateActionSource](docs/PagedResourceListOfCorporateActionSource.md)
 - [PagedResourceListOfCustodianAccount](docs/PagedResourceListOfCustodianAccount.md)
 - [PagedResourceListOfCustomEntityDefinition](docs/PagedResourceListOfCustomEntityDefinition.md)
 - [PagedResourceListOfCustomEntityResponse](docs/PagedResourceListOfCustomEntityResponse.md)
 - [PagedResourceListOfCustomEntityType](docs/PagedResourceListOfCustomEntityType.md)
 - [PagedResourceListOfCutLabelDefinition](docs/PagedResourceListOfCutLabelDefinition.md)
 - [PagedResourceListOfDataTypeSummary](docs/PagedResourceListOfDataTypeSummary.md)
 - [PagedResourceListOfDialectId](docs/PagedResourceListOfDialectId.md)
 - [PagedResourceListOfDiaryEntry](docs/PagedResourceListOfDiaryEntry.md)
 - [PagedResourceListOfExecution](docs/PagedResourceListOfExecution.md)
 - [PagedResourceListOfFee](docs/PagedResourceListOfFee.md)
 - [PagedResourceListOfFeeType](docs/PagedResourceListOfFeeType.md)
 - [PagedResourceListOfFund](docs/PagedResourceListOfFund.md)
 - [PagedResourceListOfFundCalendarEntry](docs/PagedResourceListOfFundCalendarEntry.md)
 - [PagedResourceListOfFundConfiguration](docs/PagedResourceListOfFundConfiguration.md)
 - [PagedResourceListOfGeneralLedgerProfileResponse](docs/PagedResourceListOfGeneralLedgerProfileResponse.md)
 - [PagedResourceListOfGroupReconciliationComparisonResult](docs/PagedResourceListOfGroupReconciliationComparisonResult.md)
 - [PagedResourceListOfGroupReconciliationComparisonRuleset](docs/PagedResourceListOfGroupReconciliationComparisonRuleset.md)
 - [PagedResourceListOfGroupReconciliationDefinition](docs/PagedResourceListOfGroupReconciliationDefinition.md)
 - [PagedResourceListOfIdentifierDefinition](docs/PagedResourceListOfIdentifierDefinition.md)
 - [PagedResourceListOfInstrument](docs/PagedResourceListOfInstrument.md)
 - [PagedResourceListOfInstrumentEventHolder](docs/PagedResourceListOfInstrumentEventHolder.md)
 - [PagedResourceListOfInstrumentEventInstruction](docs/PagedResourceListOfInstrumentEventInstruction.md)
 - [PagedResourceListOfItemAndWorkspace](docs/PagedResourceListOfItemAndWorkspace.md)
 - [PagedResourceListOfLegalEntity](docs/PagedResourceListOfLegalEntity.md)
 - [PagedResourceListOfOrder](docs/PagedResourceListOfOrder.md)
 - [PagedResourceListOfOrderBreachHistory](docs/PagedResourceListOfOrderBreachHistory.md)
 - [PagedResourceListOfOrderGraphBlock](docs/PagedResourceListOfOrderGraphBlock.md)
 - [PagedResourceListOfOrderGraphPlacement](docs/PagedResourceListOfOrderGraphPlacement.md)
 - [PagedResourceListOfOrderInstruction](docs/PagedResourceListOfOrderInstruction.md)
 - [PagedResourceListOfPackage](docs/PagedResourceListOfPackage.md)
 - [PagedResourceListOfParticipation](docs/PagedResourceListOfParticipation.md)
 - [PagedResourceListOfPerson](docs/PagedResourceListOfPerson.md)
 - [PagedResourceListOfPlacement](docs/PagedResourceListOfPlacement.md)
 - [PagedResourceListOfPortfolioGroup](docs/PagedResourceListOfPortfolioGroup.md)
 - [PagedResourceListOfPortfolioGroupSearchResult](docs/PagedResourceListOfPortfolioGroupSearchResult.md)
 - [PagedResourceListOfPortfolioSearchResult](docs/PagedResourceListOfPortfolioSearchResult.md)
 - [PagedResourceListOfPostingModuleResponse](docs/PagedResourceListOfPostingModuleResponse.md)
 - [PagedResourceListOfPostingModuleRule](docs/PagedResourceListOfPostingModuleRule.md)
 - [PagedResourceListOfPropertyDefinition](docs/PagedResourceListOfPropertyDefinition.md)
 - [PagedResourceListOfPropertyDefinitionSearchResult](docs/PagedResourceListOfPropertyDefinitionSearchResult.md)
 - [PagedResourceListOfReconciliation](docs/PagedResourceListOfReconciliation.md)
 - [PagedResourceListOfReferenceListResponse](docs/PagedResourceListOfReferenceListResponse.md)
 - [PagedResourceListOfRelationalDataPointResponse](docs/PagedResourceListOfRelationalDataPointResponse.md)
 - [PagedResourceListOfRelationalDatasetDefinition](docs/PagedResourceListOfRelationalDatasetDefinition.md)
 - [PagedResourceListOfRelationshipDefinition](docs/PagedResourceListOfRelationshipDefinition.md)
 - [PagedResourceListOfSequenceDefinition](docs/PagedResourceListOfSequenceDefinition.md)
 - [PagedResourceListOfStagedModification](docs/PagedResourceListOfStagedModification.md)
 - [PagedResourceListOfStagedModificationsRequestedChangeInterval](docs/PagedResourceListOfStagedModificationsRequestedChangeInterval.md)
 - [PagedResourceListOfStagingRuleSet](docs/PagedResourceListOfStagingRuleSet.md)
 - [PagedResourceListOfTimeline](docs/PagedResourceListOfTimeline.md)
 - [PagedResourceListOfTransactionTemplate](docs/PagedResourceListOfTransactionTemplate.md)
 - [PagedResourceListOfTransactionTemplateSpecification](docs/PagedResourceListOfTransactionTemplateSpecification.md)
 - [PagedResourceListOfTranslationScriptId](docs/PagedResourceListOfTranslationScriptId.md)
 - [PagedResourceListOfValuationPointOverview](docs/PagedResourceListOfValuationPointOverview.md)
 - [PagedResourceListOfVirtualRow](docs/PagedResourceListOfVirtualRow.md)
 - [PagedResourceListOfWorkspace](docs/PagedResourceListOfWorkspace.md)
 - [PagedResourceListOfWorkspaceItem](docs/PagedResourceListOfWorkspaceItem.md)
 - [PartialClosureConstituent](docs/PartialClosureConstituent.md)
 - [Participation](docs/Participation.md)
 - [ParticipationRequest](docs/ParticipationRequest.md)
 - [ParticipationSetRequest](docs/ParticipationSetRequest.md)
 - [PercentCheckStep](docs/PercentCheckStep.md)
 - [PercentCheckStepRequest](docs/PercentCheckStepRequest.md)
 - [PerformanceReturn](docs/PerformanceReturn.md)
 - [PerformanceReturnsMetric](docs/PerformanceReturnsMetric.md)
 - [PeriodDiaryEntriesReopenedResponse](docs/PeriodDiaryEntriesReopenedResponse.md)
 - [PeriodType](docs/PeriodType.md)
 - [PerpetualEntityState](docs/PerpetualEntityState.md)
 - [PerpetualProperty](docs/PerpetualProperty.md)
 - [Person](docs/Person.md)
 - [PlaceBlocksRequest](docs/PlaceBlocksRequest.md)
 - [Placement](docs/Placement.md)
 - [PlacementRequest](docs/PlacementRequest.md)
 - [PlacementSetRequest](docs/PlacementSetRequest.md)
 - [PlacementUpdateRequest](docs/PlacementUpdateRequest.md)
 - [PnlJournalEntryLine](docs/PnlJournalEntryLine.md)
 - [Portfolio](docs/Portfolio.md)
 - [PortfolioCashFlow](docs/PortfolioCashFlow.md)
 - [PortfolioCashLadder](docs/PortfolioCashLadder.md)
 - [PortfolioDetails](docs/PortfolioDetails.md)
 - [PortfolioEntity](docs/PortfolioEntity.md)
 - [PortfolioEntityId](docs/PortfolioEntityId.md)
 - [PortfolioEntityIdWithDetails](docs/PortfolioEntityIdWithDetails.md)
 - [PortfolioGroup](docs/PortfolioGroup.md)
 - [PortfolioGroupIdComplianceParameter](docs/PortfolioGroupIdComplianceParameter.md)
 - [PortfolioGroupIdList](docs/PortfolioGroupIdList.md)
 - [PortfolioGroupIdListComplianceParameter](docs/PortfolioGroupIdListComplianceParameter.md)
 - [PortfolioGroupProperties](docs/PortfolioGroupProperties.md)
 - [PortfolioGroupSearchResult](docs/PortfolioGroupSearchResult.md)
 - [PortfolioHolding](docs/PortfolioHolding.md)
 - [PortfolioId](docs/PortfolioId.md)
 - [PortfolioIdComplianceParameter](docs/PortfolioIdComplianceParameter.md)
 - [PortfolioIdList](docs/PortfolioIdList.md)
 - [PortfolioIdListComplianceParameter](docs/PortfolioIdListComplianceParameter.md)
 - [PortfolioProperties](docs/PortfolioProperties.md)
 - [PortfolioReconciliationRequest](docs/PortfolioReconciliationRequest.md)
 - [PortfolioResultDataKeyRule](docs/PortfolioResultDataKeyRule.md)
 - [PortfolioReturnBreakdown](docs/PortfolioReturnBreakdown.md)
 - [PortfolioSearchResult](docs/PortfolioSearchResult.md)
 - [PortfolioSettlementConfiguration](docs/PortfolioSettlementConfiguration.md)
 - [PortfolioTradeTicket](docs/PortfolioTradeTicket.md)
 - [PortfolioTransaction](docs/PortfolioTransaction.md)
 - [PortfolioType](docs/PortfolioType.md)
 - [PortfolioWithoutHref](docs/PortfolioWithoutHref.md)
 - [PortfoliosReconciliationRequest](docs/PortfoliosReconciliationRequest.md)
 - [PostCloseActivitiesRequest](docs/PostCloseActivitiesRequest.md)
 - [PostCloseActivity](docs/PostCloseActivity.md)
 - [PostingModuleDetails](docs/PostingModuleDetails.md)
 - [PostingModuleRequest](docs/PostingModuleRequest.md)
 - [PostingModuleResponse](docs/PostingModuleResponse.md)
 - [PostingModuleRule](docs/PostingModuleRule.md)
 - [PostingModuleRulesUpdatedResponse](docs/PostingModuleRulesUpdatedResponse.md)
 - [PreTradeConfiguration](docs/PreTradeConfiguration.md)
 - [Premium](docs/Premium.md)
 - [PreviousFundCalendarEntry](docs/PreviousFundCalendarEntry.md)
 - [PreviousFundValuationPointData](docs/PreviousFundValuationPointData.md)
 - [PreviousNAV](docs/PreviousNAV.md)
 - [PreviousShareClassBreakdown](docs/PreviousShareClassBreakdown.md)
 - [PricingContext](docs/PricingContext.md)
 - [PricingModel](docs/PricingModel.md)
 - [PricingOptions](docs/PricingOptions.md)
 - [PrimarySchedule](docs/PrimarySchedule.md)
 - [ProcessedCommand](docs/ProcessedCommand.md)
 - [PropertyDefinition](docs/PropertyDefinition.md)
 - [PropertyDefinitionEntity](docs/PropertyDefinitionEntity.md)
 - [PropertyDefinitionSearchResult](docs/PropertyDefinitionSearchResult.md)
 - [PropertyDefinitionType](docs/PropertyDefinitionType.md)
 - [PropertyDomain](docs/PropertyDomain.md)
 - [PropertyFilter](docs/PropertyFilter.md)
 - [PropertyInterval](docs/PropertyInterval.md)
 - [PropertyKeyComplianceParameter](docs/PropertyKeyComplianceParameter.md)
 - [PropertyKeyListComplianceParameter](docs/PropertyKeyListComplianceParameter.md)
 - [PropertyLifeTime](docs/PropertyLifeTime.md)
 - [PropertyList](docs/PropertyList.md)
 - [PropertyListComplianceParameter](docs/PropertyListComplianceParameter.md)
 - [PropertyReferenceDataValue](docs/PropertyReferenceDataValue.md)
 - [PropertySchema](docs/PropertySchema.md)
 - [PropertyType](docs/PropertyType.md)
 - [PropertyValue](docs/PropertyValue.md)
 - [PropertyValueEquals](docs/PropertyValueEquals.md)
 - [PropertyValueIn](docs/PropertyValueIn.md)
 - [ProtectionPayoutCashFlowEvent](docs/ProtectionPayoutCashFlowEvent.md)
 - [QuantityInstructed](docs/QuantityInstructed.md)
 - [QueryApplicableInstrumentEventsRequest](docs/QueryApplicableInstrumentEventsRequest.md)
 - [QueryBucketedCashFlowsRequest](docs/QueryBucketedCashFlowsRequest.md)
 - [QueryCashFlowsRequest](docs/QueryCashFlowsRequest.md)
 - [QueryInstrumentEventsRequest](docs/QueryInstrumentEventsRequest.md)
 - [QueryRelationalDatasetRequest](docs/QueryRelationalDatasetRequest.md)
 - [QueryTradeTicketsRequest](docs/QueryTradeTicketsRequest.md)
 - [QueryableKey](docs/QueryableKey.md)
 - [Quote](docs/Quote.md)
 - [QuoteAccessMetadataRule](docs/QuoteAccessMetadataRule.md)
 - [QuoteAccessMetadataRuleId](docs/QuoteAccessMetadataRuleId.md)
 - [QuoteDependency](docs/QuoteDependency.md)
 - [QuoteId](docs/QuoteId.md)
 - [QuoteInstrumentIdType](docs/QuoteInstrumentIdType.md)
 - [QuoteSeriesId](docs/QuoteSeriesId.md)
 - [QuoteType](docs/QuoteType.md)
 - [RawVendorEvent](docs/RawVendorEvent.md)
 - [ReOpenPeriodDiaryEntryRequest](docs/ReOpenPeriodDiaryEntryRequest.md)
 - [RealisedGainLoss](docs/RealisedGainLoss.md)
 - [RecipeBlock](docs/RecipeBlock.md)
 - [RecipeComposer](docs/RecipeComposer.md)
 - [RecipeValue](docs/RecipeValue.md)
 - [RecombineStep](docs/RecombineStep.md)
 - [RecommendedSortBy](docs/RecommendedSortBy.md)
 - [ReconcileDateTimeRule](docs/ReconcileDateTimeRule.md)
 - [ReconcileNumericRule](docs/ReconcileNumericRule.md)
 - [ReconcileStringRule](docs/ReconcileStringRule.md)
 - [ReconciledTransaction](docs/ReconciledTransaction.md)
 - [Reconciliation](docs/Reconciliation.md)
 - [ReconciliationBreak](docs/ReconciliationBreak.md)
 - [ReconciliationConfiguration](docs/ReconciliationConfiguration.md)
 - [ReconciliationId](docs/ReconciliationId.md)
 - [ReconciliationLeftRightAddressKeyPair](docs/ReconciliationLeftRightAddressKeyPair.md)
 - [ReconciliationLine](docs/ReconciliationLine.md)
 - [ReconciliationRequest](docs/ReconciliationRequest.md)
 - [ReconciliationResponse](docs/ReconciliationResponse.md)
 - [ReconciliationRule](docs/ReconciliationRule.md)
 - [ReconciliationRuleType](docs/ReconciliationRuleType.md)
 - [ReconciliationSideConfiguration](docs/ReconciliationSideConfiguration.md)
 - [ReconciliationTransactions](docs/ReconciliationTransactions.md)
 - [ReferenceData](docs/ReferenceData.md)
 - [ReferenceInstrument](docs/ReferenceInstrument.md)
 - [ReferenceList](docs/ReferenceList.md)
 - [ReferenceListRequest](docs/ReferenceListRequest.md)
 - [ReferenceListResponse](docs/ReferenceListResponse.md)
 - [ReferenceListType](docs/ReferenceListType.md)
 - [ReferencePortfolioConstituent](docs/ReferencePortfolioConstituent.md)
 - [ReferencePortfolioConstituentRequest](docs/ReferencePortfolioConstituentRequest.md)
 - [ReferencePortfolioWeightType](docs/ReferencePortfolioWeightType.md)
 - [RelatedEntity](docs/RelatedEntity.md)
 - [Relation](docs/Relation.md)
 - [RelationDefinition](docs/RelationDefinition.md)
 - [RelationalDataPointFieldValueResponse](docs/RelationalDataPointFieldValueResponse.md)
 - [RelationalDataPointResponse](docs/RelationalDataPointResponse.md)
 - [RelationalDataSeriesResponse](docs/RelationalDataSeriesResponse.md)
 - [RelationalDatasetDefinition](docs/RelationalDatasetDefinition.md)
 - [RelationalDatasetFieldDefinition](docs/RelationalDatasetFieldDefinition.md)
 - [RelationalDatasetFieldsToAdd](docs/RelationalDatasetFieldsToAdd.md)
 - [RelationalDatasetFieldsToRemove](docs/RelationalDatasetFieldsToRemove.md)
 - [RelationalDatasetFieldsToUpdate](docs/RelationalDatasetFieldsToUpdate.md)
 - [Relationship](docs/Relationship.md)
 - [RelationshipDefinition](docs/RelationshipDefinition.md)
 - [RelativeDateOffset](docs/RelativeDateOffset.md)
 - [Repo](docs/Repo.md)
 - [RepoCashFlowEvent](docs/RepoCashFlowEvent.md)
 - [RepoPartialClosureEvent](docs/RepoPartialClosureEvent.md)
 - [RepurchaseOfferEvent](docs/RepurchaseOfferEvent.md)
 - [RequestedChanges](docs/RequestedChanges.md)
 - [ResetEvent](docs/ResetEvent.md)
 - [ResourceId](docs/ResourceId.md)
 - [ResourceListOfAccessControlledResource](docs/ResourceListOfAccessControlledResource.md)
 - [ResourceListOfAccessMetadataValueOf](docs/ResourceListOfAccessMetadataValueOf.md)
 - [ResourceListOfAddressKeyDefinition](docs/ResourceListOfAddressKeyDefinition.md)
 - [ResourceListOfAggregatedReturn](docs/ResourceListOfAggregatedReturn.md)
 - [ResourceListOfAggregationQuery](docs/ResourceListOfAggregationQuery.md)
 - [ResourceListOfAllocation](docs/ResourceListOfAllocation.md)
 - [ResourceListOfApplicableInstrumentEvent](docs/ResourceListOfApplicableInstrumentEvent.md)
 - [ResourceListOfBlock](docs/ResourceListOfBlock.md)
 - [ResourceListOfBlockAndOrders](docs/ResourceListOfBlockAndOrders.md)
 - [ResourceListOfCalendarDate](docs/ResourceListOfCalendarDate.md)
 - [ResourceListOfChange](docs/ResourceListOfChange.md)
 - [ResourceListOfChangeHistory](docs/ResourceListOfChangeHistory.md)
 - [ResourceListOfChangeInterval](docs/ResourceListOfChangeInterval.md)
 - [ResourceListOfChangeIntervalWithOrderManagementDetail](docs/ResourceListOfChangeIntervalWithOrderManagementDetail.md)
 - [ResourceListOfComplianceBreachedOrderInfo](docs/ResourceListOfComplianceBreachedOrderInfo.md)
 - [ResourceListOfComplianceRule](docs/ResourceListOfComplianceRule.md)
 - [ResourceListOfComplianceRuleResult](docs/ResourceListOfComplianceRuleResult.md)
 - [ResourceListOfComplianceRunInfo](docs/ResourceListOfComplianceRunInfo.md)
 - [ResourceListOfConstituentsAdjustmentHeader](docs/ResourceListOfConstituentsAdjustmentHeader.md)
 - [ResourceListOfCorporateAction](docs/ResourceListOfCorporateAction.md)
 - [ResourceListOfDataModelSummary](docs/ResourceListOfDataModelSummary.md)
 - [ResourceListOfDataType](docs/ResourceListOfDataType.md)
 - [ResourceListOfExecution](docs/ResourceListOfExecution.md)
 - [ResourceListOfFeeRule](docs/ResourceListOfFeeRule.md)
 - [ResourceListOfGetCdsFlowConventionsResponse](docs/ResourceListOfGetCdsFlowConventionsResponse.md)
 - [ResourceListOfGetCounterpartyAgreementResponse](docs/ResourceListOfGetCounterpartyAgreementResponse.md)
 - [ResourceListOfGetCreditSupportAnnexResponse](docs/ResourceListOfGetCreditSupportAnnexResponse.md)
 - [ResourceListOfGetFlowConventionsResponse](docs/ResourceListOfGetFlowConventionsResponse.md)
 - [ResourceListOfGetIndexConventionResponse](docs/ResourceListOfGetIndexConventionResponse.md)
 - [ResourceListOfGetRecipeComposerResponse](docs/ResourceListOfGetRecipeComposerResponse.md)
 - [ResourceListOfGetRecipeResponse](docs/ResourceListOfGetRecipeResponse.md)
 - [ResourceListOfHoldingsAdjustmentHeader](docs/ResourceListOfHoldingsAdjustmentHeader.md)
 - [ResourceListOfIUnitDefinitionDto](docs/ResourceListOfIUnitDefinitionDto.md)
 - [ResourceListOfInstrumentCashFlow](docs/ResourceListOfInstrumentCashFlow.md)
 - [ResourceListOfInstrumentEventHolder](docs/ResourceListOfInstrumentEventHolder.md)
 - [ResourceListOfInstrumentIdTypeDescriptor](docs/ResourceListOfInstrumentIdTypeDescriptor.md)
 - [ResourceListOfInvestmentAccount](docs/ResourceListOfInvestmentAccount.md)
 - [ResourceListOfInvestorRecord](docs/ResourceListOfInvestorRecord.md)
 - [ResourceListOfLegalEntity](docs/ResourceListOfLegalEntity.md)
 - [ResourceListOfListComplexMarketDataWithMetaDataResponse](docs/ResourceListOfListComplexMarketDataWithMetaDataResponse.md)
 - [ResourceListOfMapping](docs/ResourceListOfMapping.md)
 - [ResourceListOfMovedOrderToDifferentBlockResponse](docs/ResourceListOfMovedOrderToDifferentBlockResponse.md)
 - [ResourceListOfNavActivityAdjustment](docs/ResourceListOfNavActivityAdjustment.md)
 - [ResourceListOfOrder](docs/ResourceListOfOrder.md)
 - [ResourceListOfOrderInstruction](docs/ResourceListOfOrderInstruction.md)
 - [ResourceListOfOutputTransaction](docs/ResourceListOfOutputTransaction.md)
 - [ResourceListOfPackage](docs/ResourceListOfPackage.md)
 - [ResourceListOfParticipation](docs/ResourceListOfParticipation.md)
 - [ResourceListOfPerformanceReturn](docs/ResourceListOfPerformanceReturn.md)
 - [ResourceListOfPerson](docs/ResourceListOfPerson.md)
 - [ResourceListOfPlacement](docs/ResourceListOfPlacement.md)
 - [ResourceListOfPortfolio](docs/ResourceListOfPortfolio.md)
 - [ResourceListOfPortfolioCashFlow](docs/ResourceListOfPortfolioCashFlow.md)
 - [ResourceListOfPortfolioCashLadder](docs/ResourceListOfPortfolioCashLadder.md)
 - [ResourceListOfPortfolioTradeTicket](docs/ResourceListOfPortfolioTradeTicket.md)
 - [ResourceListOfProcessedCommand](docs/ResourceListOfProcessedCommand.md)
 - [ResourceListOfProperty](docs/ResourceListOfProperty.md)
 - [ResourceListOfPropertyDefinition](docs/ResourceListOfPropertyDefinition.md)
 - [ResourceListOfPropertyInterval](docs/ResourceListOfPropertyInterval.md)
 - [ResourceListOfQueryableKey](docs/ResourceListOfQueryableKey.md)
 - [ResourceListOfQuote](docs/ResourceListOfQuote.md)
 - [ResourceListOfQuoteAccessMetadataRule](docs/ResourceListOfQuoteAccessMetadataRule.md)
 - [ResourceListOfReconciliationBreak](docs/ResourceListOfReconciliationBreak.md)
 - [ResourceListOfRelation](docs/ResourceListOfRelation.md)
 - [ResourceListOfRelationship](docs/ResourceListOfRelationship.md)
 - [ResourceListOfReturnsEntity](docs/ResourceListOfReturnsEntity.md)
 - [ResourceListOfScopeDefinition](docs/ResourceListOfScopeDefinition.md)
 - [ResourceListOfSideDefinition](docs/ResourceListOfSideDefinition.md)
 - [ResourceListOfString](docs/ResourceListOfString.md)
 - [ResourceListOfTaxRuleSet](docs/ResourceListOfTaxRuleSet.md)
 - [ResourceListOfTransaction](docs/ResourceListOfTransaction.md)
 - [ResourceListOfTransactionSettlementInstruction](docs/ResourceListOfTransactionSettlementInstruction.md)
 - [ResourceListOfTransactionType](docs/ResourceListOfTransactionType.md)
 - [ResourceListOfValueType](docs/ResourceListOfValueType.md)
 - [ResponseMetaData](docs/ResponseMetaData.md)
 - [ResultDataKeyRule](docs/ResultDataKeyRule.md)
 - [ResultDataSchema](docs/ResultDataSchema.md)
 - [ResultKeyRule](docs/ResultKeyRule.md)
 - [ResultKeyRuleType](docs/ResultKeyRuleType.md)
 - [ResultValue](docs/ResultValue.md)
 - [ResultValue0D](docs/ResultValue0D.md)
 - [ResultValueBool](docs/ResultValueBool.md)
 - [ResultValueCurrency](docs/ResultValueCurrency.md)
 - [ResultValueDateTimeOffset](docs/ResultValueDateTimeOffset.md)
 - [ResultValueDecimal](docs/ResultValueDecimal.md)
 - [ResultValueDictionary](docs/ResultValueDictionary.md)
 - [ResultValueInt](docs/ResultValueInt.md)
 - [ResultValueString](docs/ResultValueString.md)
 - [ResultValueType](docs/ResultValueType.md)
 - [ReturnZeroPvOptions](docs/ReturnZeroPvOptions.md)
 - [ReturnsEntity](docs/ReturnsEntity.md)
 - [ReverseStockSplitEvent](docs/ReverseStockSplitEvent.md)
 - [RevertValuationPointDataRequest](docs/RevertValuationPointDataRequest.md)
 - [RollInterestUpdates](docs/RollInterestUpdates.md)
 - [RollPrincipalUpdates](docs/RollPrincipalUpdates.md)
 - [RolloverConstituent](docs/RolloverConstituent.md)
 - [RoundingConfiguration](docs/RoundingConfiguration.md)
 - [RoundingConfigurationComponent](docs/RoundingConfigurationComponent.md)
 - [RoundingConvention](docs/RoundingConvention.md)
 - [RulesInterval](docs/RulesInterval.md)
 - [RunCheckRequest](docs/RunCheckRequest.md)
 - [RunCheckResponse](docs/RunCheckResponse.md)
 - [ScalingMethodology](docs/ScalingMethodology.md)
 - [Schedule](docs/Schedule.md)
 - [ScheduleType](docs/ScheduleType.md)
 - [ScopeDefinition](docs/ScopeDefinition.md)
 - [ScripDividendEvent](docs/ScripDividendEvent.md)
 - [ScriptMapReference](docs/ScriptMapReference.md)
 - [SecurityElection](docs/SecurityElection.md)
 - [SecurityOfferElection](docs/SecurityOfferElection.md)
 - [SequenceDefinition](docs/SequenceDefinition.md)
 - [SetAmortisationRulesRequest](docs/SetAmortisationRulesRequest.md)
 - [SetLegalEntityIdentifiersRequest](docs/SetLegalEntityIdentifiersRequest.md)
 - [SetLegalEntityPropertiesRequest](docs/SetLegalEntityPropertiesRequest.md)
 - [SetPersonIdentifiersRequest](docs/SetPersonIdentifiersRequest.md)
 - [SetPersonPropertiesRequest](docs/SetPersonPropertiesRequest.md)
 - [SetShareClassInstrumentsRequest](docs/SetShareClassInstrumentsRequest.md)
 - [SetTransactionConfigurationAlias](docs/SetTransactionConfigurationAlias.md)
 - [SetTransactionConfigurationSourceRequest](docs/SetTransactionConfigurationSourceRequest.md)
 - [SettlementConfigurationCategory](docs/SettlementConfigurationCategory.md)
 - [SettlementCycle](docs/SettlementCycle.md)
 - [SettlementInLieu](docs/SettlementInLieu.md)
 - [SettlementInstructionQuery](docs/SettlementInstructionQuery.md)
 - [SettlementInstructionRequest](docs/SettlementInstructionRequest.md)
 - [SettlementInstructionWithTransaction](docs/SettlementInstructionWithTransaction.md)
 - [SettlementProblem](docs/SettlementProblem.md)
 - [SettlementSchedule](docs/SettlementSchedule.md)
 - [ShareClassAmount](docs/ShareClassAmount.md)
 - [ShareClassBreakdown](docs/ShareClassBreakdown.md)
 - [ShareClassData](docs/ShareClassData.md)
 - [ShareClassDealingBreakdown](docs/ShareClassDealingBreakdown.md)
 - [ShareClassDetails](docs/ShareClassDetails.md)
 - [ShareClassPnlBreakdown](docs/ShareClassPnlBreakdown.md)
 - [SideConfigurationData](docs/SideConfigurationData.md)
 - [SideConfigurationDataRequest](docs/SideConfigurationDataRequest.md)
 - [SideDefinition](docs/SideDefinition.md)
 - [SideDefinitionRequest](docs/SideDefinitionRequest.md)
 - [SidesDefinitionRequest](docs/SidesDefinitionRequest.md)
 - [SimpleCashFlowLoan](docs/SimpleCashFlowLoan.md)
 - [SimpleInstrument](docs/SimpleInstrument.md)
 - [SimpleRoundingConvention](docs/SimpleRoundingConvention.md)
 - [SingleValuationPointQueryParameters](docs/SingleValuationPointQueryParameters.md)
 - [SortOrder](docs/SortOrder.md)
 - [SpecificHoldingPricingInfo](docs/SpecificHoldingPricingInfo.md)
 - [SpinOffEvent](docs/SpinOffEvent.md)
 - [StagedModification](docs/StagedModification.md)
 - [StagedModificationDecision](docs/StagedModificationDecision.md)
 - [StagedModificationDecisionRequest](docs/StagedModificationDecisionRequest.md)
 - [StagedModificationEffectiveRange](docs/StagedModificationEffectiveRange.md)
 - [StagedModificationStagingRule](docs/StagedModificationStagingRule.md)
 - [StagedModificationsEntityHrefs](docs/StagedModificationsEntityHrefs.md)
 - [StagedModificationsInfo](docs/StagedModificationsInfo.md)
 - [StagedModificationsRequestedChangeInterval](docs/StagedModificationsRequestedChangeInterval.md)
 - [StagingRule](docs/StagingRule.md)
 - [StagingRuleApprovalCriteria](docs/StagingRuleApprovalCriteria.md)
 - [StagingRuleMatchCriteria](docs/StagingRuleMatchCriteria.md)
 - [StagingRuleSet](docs/StagingRuleSet.md)
 - [StepSchedule](docs/StepSchedule.md)
 - [StockDividendEvent](docs/StockDividendEvent.md)
 - [StockSplitEvent](docs/StockSplitEvent.md)
 - [Strategy](docs/Strategy.md)
 - [StringComparisonType](docs/StringComparisonType.md)
 - [StringComplianceParameter](docs/StringComplianceParameter.md)
 - [StringList](docs/StringList.md)
 - [StringListComplianceParameter](docs/StringListComplianceParameter.md)
 - [StructuredResultData](docs/StructuredResultData.md)
 - [StructuredResultDataId](docs/StructuredResultDataId.md)
 - [SubHoldingKeyValueEquals](docs/SubHoldingKeyValueEquals.md)
 - [SwapCashFlowEvent](docs/SwapCashFlowEvent.md)
 - [SwapPrincipalEvent](docs/SwapPrincipalEvent.md)
 - [SweepBlocksRequest](docs/SweepBlocksRequest.md)
 - [SweepBlocksResponse](docs/SweepBlocksResponse.md)
 - [TargetTaxLot](docs/TargetTaxLot.md)
 - [TargetTaxLotRequest](docs/TargetTaxLotRequest.md)
 - [TaxRule](docs/TaxRule.md)
 - [TaxRuleSet](docs/TaxRuleSet.md)
 - [TemplateField](docs/TemplateField.md)
 - [TenderEvent](docs/TenderEvent.md)
 - [TenderOfferElection](docs/TenderOfferElection.md)
 - [TermDeposit](docs/TermDeposit.md)
 - [TermDepositInterestEvent](docs/TermDepositInterestEvent.md)
 - [TermDepositPrincipalEvent](docs/TermDepositPrincipalEvent.md)
 - [TimeZoneConventions](docs/TimeZoneConventions.md)
 - [Timeline](docs/Timeline.md)
 - [TotalReturnSwap](docs/TotalReturnSwap.md)
 - [Touch](docs/Touch.md)
 - [TradeTicket](docs/TradeTicket.md)
 - [TradeTicketType](docs/TradeTicketType.md)
 - [TradingConventions](docs/TradingConventions.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionConfigurationData](docs/TransactionConfigurationData.md)
 - [TransactionConfigurationDataRequest](docs/TransactionConfigurationDataRequest.md)
 - [TransactionConfigurationMovementData](docs/TransactionConfigurationMovementData.md)
 - [TransactionConfigurationMovementDataRequest](docs/TransactionConfigurationMovementDataRequest.md)
 - [TransactionConfigurationTypeAlias](docs/TransactionConfigurationTypeAlias.md)
 - [TransactionCurrencyAndAmount](docs/TransactionCurrencyAndAmount.md)
 - [TransactionDateWindows](docs/TransactionDateWindows.md)
 - [TransactionDiagnostics](docs/TransactionDiagnostics.md)
 - [TransactionFieldMap](docs/TransactionFieldMap.md)
 - [TransactionMatchingAlternativeId](docs/TransactionMatchingAlternativeId.md)
 - [TransactionPrice](docs/TransactionPrice.md)
 - [TransactionPriceAndType](docs/TransactionPriceAndType.md)
 - [TransactionPriceType](docs/TransactionPriceType.md)
 - [TransactionPropertyMap](docs/TransactionPropertyMap.md)
 - [TransactionPropertyMapping](docs/TransactionPropertyMapping.md)
 - [TransactionPropertyMappingRequest](docs/TransactionPropertyMappingRequest.md)
 - [TransactionQueryMode](docs/TransactionQueryMode.md)
 - [TransactionQueryParameters](docs/TransactionQueryParameters.md)
 - [TransactionReconciliationRequest](docs/TransactionReconciliationRequest.md)
 - [TransactionReconciliationRequestV2](docs/TransactionReconciliationRequestV2.md)
 - [TransactionRequest](docs/TransactionRequest.md)
 - [TransactionRoles](docs/TransactionRoles.md)
 - [TransactionSetConfigurationData](docs/TransactionSetConfigurationData.md)
 - [TransactionSetConfigurationDataRequest](docs/TransactionSetConfigurationDataRequest.md)
 - [TransactionSettlementBucket](docs/TransactionSettlementBucket.md)
 - [TransactionSettlementInstruction](docs/TransactionSettlementInstruction.md)
 - [TransactionSettlementMovement](docs/TransactionSettlementMovement.md)
 - [TransactionSettlementStatus](docs/TransactionSettlementStatus.md)
 - [TransactionSettlementSummary](docs/TransactionSettlementSummary.md)
 - [TransactionStatus](docs/TransactionStatus.md)
 - [TransactionTemplate](docs/TransactionTemplate.md)
 - [TransactionTemplateRequest](docs/TransactionTemplateRequest.md)
 - [TransactionTemplateSpecification](docs/TransactionTemplateSpecification.md)
 - [TransactionType](docs/TransactionType.md)
 - [TransactionTypeAlias](docs/TransactionTypeAlias.md)
 - [TransactionTypeCalculation](docs/TransactionTypeCalculation.md)
 - [TransactionTypeDetails](docs/TransactionTypeDetails.md)
 - [TransactionTypeMovement](docs/TransactionTypeMovement.md)
 - [TransactionTypePropertyMapping](docs/TransactionTypePropertyMapping.md)
 - [TransactionTypeRequest](docs/TransactionTypeRequest.md)
 - [TransactionsReconciliationsResponse](docs/TransactionsReconciliationsResponse.md)
 - [TransferAgencyDates](docs/TransferAgencyDates.md)
 - [TransitionEvent](docs/TransitionEvent.md)
 - [TranslateEntitiesInlinedRequest](docs/TranslateEntitiesInlinedRequest.md)
 - [TranslateEntitiesRequest](docs/TranslateEntitiesRequest.md)
 - [TranslateEntitiesResponse](docs/TranslateEntitiesResponse.md)
 - [TranslateInstrumentDefinitionsRequest](docs/TranslateInstrumentDefinitionsRequest.md)
 - [TranslateInstrumentDefinitionsResponse](docs/TranslateInstrumentDefinitionsResponse.md)
 - [TranslateTradeTicketRequest](docs/TranslateTradeTicketRequest.md)
 - [TranslateTradeTicketsResponse](docs/TranslateTradeTicketsResponse.md)
 - [TranslationContext](docs/TranslationContext.md)
 - [TranslationInput](docs/TranslationInput.md)
 - [TranslationResult](docs/TranslationResult.md)
 - [TranslationScript](docs/TranslationScript.md)
 - [TranslationScriptId](docs/TranslationScriptId.md)
 - [TrialBalance](docs/TrialBalance.md)
 - [TrialBalanceQueryParameters](docs/TrialBalanceQueryParameters.md)
 - [TriggerEvent](docs/TriggerEvent.md)
 - [TypedResourceId](docs/TypedResourceId.md)
 - [UnitSchema](docs/UnitSchema.md)
 - [UnitisationData](docs/UnitisationData.md)
 - [UnitsRatio](docs/UnitsRatio.md)
 - [UnmatchedHoldingMethod](docs/UnmatchedHoldingMethod.md)
 - [UpdateAmortisationRuleSetDetailsRequest](docs/UpdateAmortisationRuleSetDetailsRequest.md)
 - [UpdateCalendarRequest](docs/UpdateCalendarRequest.md)
 - [UpdateCheckDefinitionRequest](docs/UpdateCheckDefinitionRequest.md)
 - [UpdateCheckDefinitionRuleSet](docs/UpdateCheckDefinitionRuleSet.md)
 - [UpdateComplianceTemplateRequest](docs/UpdateComplianceTemplateRequest.md)
 - [UpdateCustomDataModelRequest](docs/UpdateCustomDataModelRequest.md)
 - [UpdateCustomEntityDefinitionRequest](docs/UpdateCustomEntityDefinitionRequest.md)
 - [UpdateCustomEntityTypeRequest](docs/UpdateCustomEntityTypeRequest.md)
 - [UpdateCutLabelDefinitionRequest](docs/UpdateCutLabelDefinitionRequest.md)
 - [UpdateDataTypeRequest](docs/UpdateDataTypeRequest.md)
 - [UpdateDepositAmountEvent](docs/UpdateDepositAmountEvent.md)
 - [UpdateDerivedPropertyDefinitionRequest](docs/UpdateDerivedPropertyDefinitionRequest.md)
 - [UpdateFeeTypeRequest](docs/UpdateFeeTypeRequest.md)
 - [UpdateGroupReconciliationComparisonRulesetRequest](docs/UpdateGroupReconciliationComparisonRulesetRequest.md)
 - [UpdateGroupReconciliationDefinitionRequest](docs/UpdateGroupReconciliationDefinitionRequest.md)
 - [UpdateIdentifierDefinitionRequest](docs/UpdateIdentifierDefinitionRequest.md)
 - [UpdateInstrumentIdentifierRequest](docs/UpdateInstrumentIdentifierRequest.md)
 - [UpdateOrdersResponse](docs/UpdateOrdersResponse.md)
 - [UpdatePlacementsResponse](docs/UpdatePlacementsResponse.md)
 - [UpdatePortfolioGroupRequest](docs/UpdatePortfolioGroupRequest.md)
 - [UpdatePortfolioRequest](docs/UpdatePortfolioRequest.md)
 - [UpdatePropertyDefinitionRequest](docs/UpdatePropertyDefinitionRequest.md)
 - [UpdateReconciliationRequest](docs/UpdateReconciliationRequest.md)
 - [UpdateReferenceDataRequest](docs/UpdateReferenceDataRequest.md)
 - [UpdateRelationalDatasetDefinitionRequest](docs/UpdateRelationalDatasetDefinitionRequest.md)
 - [UpdateRelationalDatasetDetails](docs/UpdateRelationalDatasetDetails.md)
 - [UpdateRelationalDatasetFieldSchema](docs/UpdateRelationalDatasetFieldSchema.md)
 - [UpdateRelationshipDefinitionRequest](docs/UpdateRelationshipDefinitionRequest.md)
 - [UpdateSeriesIdentifierField](docs/UpdateSeriesIdentifierField.md)
 - [UpdateStagingRuleSetRequest](docs/UpdateStagingRuleSetRequest.md)
 - [UpdateTaxRuleSetRequest](docs/UpdateTaxRuleSetRequest.md)
 - [UpdateTimelineRequest](docs/UpdateTimelineRequest.md)
 - [UpdateUnitRequest](docs/UpdateUnitRequest.md)
 - [UpsertCdsFlowConventionsRequest](docs/UpsertCdsFlowConventionsRequest.md)
 - [UpsertComplexMarketDataRequest](docs/UpsertComplexMarketDataRequest.md)
 - [UpsertComplianceRuleRequest](docs/UpsertComplianceRuleRequest.md)
 - [UpsertComplianceRunSummaryRequest](docs/UpsertComplianceRunSummaryRequest.md)
 - [UpsertComplianceRunSummaryResult](docs/UpsertComplianceRunSummaryResult.md)
 - [UpsertCorporateActionRequest](docs/UpsertCorporateActionRequest.md)
 - [UpsertCorporateActionsResponse](docs/UpsertCorporateActionsResponse.md)
 - [UpsertCounterpartyAgreementRequest](docs/UpsertCounterpartyAgreementRequest.md)
 - [UpsertCreditSupportAnnexRequest](docs/UpsertCreditSupportAnnexRequest.md)
 - [UpsertCustomEntitiesResponse](docs/UpsertCustomEntitiesResponse.md)
 - [UpsertCustomEntityAccessMetadataRequest](docs/UpsertCustomEntityAccessMetadataRequest.md)
 - [UpsertDataQualityRule](docs/UpsertDataQualityRule.md)
 - [UpsertDialectRequest](docs/UpsertDialectRequest.md)
 - [UpsertFlowConventionsRequest](docs/UpsertFlowConventionsRequest.md)
 - [UpsertFundBookmarkRequest](docs/UpsertFundBookmarkRequest.md)
 - [UpsertIndexConventionRequest](docs/UpsertIndexConventionRequest.md)
 - [UpsertInstrumentEventRequest](docs/UpsertInstrumentEventRequest.md)
 - [UpsertInstrumentEventsResponse](docs/UpsertInstrumentEventsResponse.md)
 - [UpsertInstrumentPropertiesResponse](docs/UpsertInstrumentPropertiesResponse.md)
 - [UpsertInstrumentPropertyRequest](docs/UpsertInstrumentPropertyRequest.md)
 - [UpsertInstrumentsResponse](docs/UpsertInstrumentsResponse.md)
 - [UpsertInvestmentAccountRequest](docs/UpsertInvestmentAccountRequest.md)
 - [UpsertInvestmentAccountsResponse](docs/UpsertInvestmentAccountsResponse.md)
 - [UpsertInvestorRecordRequest](docs/UpsertInvestorRecordRequest.md)
 - [UpsertInvestorRecordsResponse](docs/UpsertInvestorRecordsResponse.md)
 - [UpsertLegalEntitiesResponse](docs/UpsertLegalEntitiesResponse.md)
 - [UpsertLegalEntityAccessMetadataRequest](docs/UpsertLegalEntityAccessMetadataRequest.md)
 - [UpsertLegalEntityRequest](docs/UpsertLegalEntityRequest.md)
 - [UpsertPersonAccessMetadataRequest](docs/UpsertPersonAccessMetadataRequest.md)
 - [UpsertPersonRequest](docs/UpsertPersonRequest.md)
 - [UpsertPersonsResponse](docs/UpsertPersonsResponse.md)
 - [UpsertPortfolioAccessMetadataRequest](docs/UpsertPortfolioAccessMetadataRequest.md)
 - [UpsertPortfolioGroupAccessMetadataRequest](docs/UpsertPortfolioGroupAccessMetadataRequest.md)
 - [UpsertPortfolioTransactionsResponse](docs/UpsertPortfolioTransactionsResponse.md)
 - [UpsertQuoteAccessMetadataRuleRequest](docs/UpsertQuoteAccessMetadataRuleRequest.md)
 - [UpsertQuoteRequest](docs/UpsertQuoteRequest.md)
 - [UpsertQuotesResponse](docs/UpsertQuotesResponse.md)
 - [UpsertRecipeComposerRequest](docs/UpsertRecipeComposerRequest.md)
 - [UpsertRecipeRequest](docs/UpsertRecipeRequest.md)
 - [UpsertReferencePortfolioConstituentPropertiesRequest](docs/UpsertReferencePortfolioConstituentPropertiesRequest.md)
 - [UpsertReferencePortfolioConstituentPropertiesResponse](docs/UpsertReferencePortfolioConstituentPropertiesResponse.md)
 - [UpsertReferencePortfolioConstituentsRequest](docs/UpsertReferencePortfolioConstituentsRequest.md)
 - [UpsertReferencePortfolioConstituentsResponse](docs/UpsertReferencePortfolioConstituentsResponse.md)
 - [UpsertRelationalDataPointRequest](docs/UpsertRelationalDataPointRequest.md)
 - [UpsertResultValuesDataRequest](docs/UpsertResultValuesDataRequest.md)
 - [UpsertReturnsResponse](docs/UpsertReturnsResponse.md)
 - [UpsertSingleStructuredDataResponse](docs/UpsertSingleStructuredDataResponse.md)
 - [UpsertStructuredDataResponse](docs/UpsertStructuredDataResponse.md)
 - [UpsertStructuredResultDataRequest](docs/UpsertStructuredResultDataRequest.md)
 - [UpsertTransactionPropertiesResponse](docs/UpsertTransactionPropertiesResponse.md)
 - [UpsertTranslationScriptRequest](docs/UpsertTranslationScriptRequest.md)
 - [UpsertValuationPointRequest](docs/UpsertValuationPointRequest.md)
 - [User](docs/User.md)
 - [ValuationPointDataQueryParameters](docs/ValuationPointDataQueryParameters.md)
 - [ValuationPointDataRequest](docs/ValuationPointDataRequest.md)
 - [ValuationPointDataResponse](docs/ValuationPointDataResponse.md)
 - [ValuationPointOverview](docs/ValuationPointOverview.md)
 - [ValuationPointResourceListOfAccountedTransaction](docs/ValuationPointResourceListOfAccountedTransaction.md)
 - [ValuationPointResourceListOfFundJournalEntryLine](docs/ValuationPointResourceListOfFundJournalEntryLine.md)
 - [ValuationPointResourceListOfPnlJournalEntryLine](docs/ValuationPointResourceListOfPnlJournalEntryLine.md)
 - [ValuationPointResourceListOfTrialBalance](docs/ValuationPointResourceListOfTrialBalance.md)
 - [ValuationRequest](docs/ValuationRequest.md)
 - [ValuationSchedule](docs/ValuationSchedule.md)
 - [ValuationsReconciliationRequest](docs/ValuationsReconciliationRequest.md)
 - [ValueType](docs/ValueType.md)
 - [VendorDependency](docs/VendorDependency.md)
 - [VendorLibrary](docs/VendorLibrary.md)
 - [VendorModelRule](docs/VendorModelRule.md)
 - [Version](docs/Version.md)
 - [VersionSummaryDto](docs/VersionSummaryDto.md)
 - [VersionedResourceListOfA2BDataRecord](docs/VersionedResourceListOfA2BDataRecord.md)
 - [VersionedResourceListOfA2BMovementRecord](docs/VersionedResourceListOfA2BMovementRecord.md)
 - [VersionedResourceListOfHoldingContributor](docs/VersionedResourceListOfHoldingContributor.md)
 - [VersionedResourceListOfJournalEntryLine](docs/VersionedResourceListOfJournalEntryLine.md)
 - [VersionedResourceListOfOutputTransaction](docs/VersionedResourceListOfOutputTransaction.md)
 - [VersionedResourceListOfPortfolioHolding](docs/VersionedResourceListOfPortfolioHolding.md)
 - [VersionedResourceListOfTransaction](docs/VersionedResourceListOfTransaction.md)
 - [VersionedResourceListOfTransactionSettlementInstruction](docs/VersionedResourceListOfTransactionSettlementInstruction.md)
 - [VersionedResourceListOfTrialBalance](docs/VersionedResourceListOfTrialBalance.md)
 - [VersionedResourceListWithPostBodiesOfSettlementInstructionWithTransactionToSettlementInstructionQuery](docs/VersionedResourceListWithPostBodiesOfSettlementInstructionWithTransactionToSettlementInstructionQuery.md)
 - [VersionedResourceListWithWarningsOfPortfolioHolding](docs/VersionedResourceListWithWarningsOfPortfolioHolding.md)
 - [VirtualDocument](docs/VirtualDocument.md)
 - [VirtualDocumentRow](docs/VirtualDocumentRow.md)
 - [VirtualRow](docs/VirtualRow.md)
 - [Warning](docs/Warning.md)
 - [WeekendMask](docs/WeekendMask.md)
 - [WeightedInstrument](docs/WeightedInstrument.md)
 - [WeightedInstrumentInLineLookupIdentifiers](docs/WeightedInstrumentInLineLookupIdentifiers.md)
 - [WeightedInstruments](docs/WeightedInstruments.md)
 - [Workspace](docs/Workspace.md)
 - [WorkspaceCreationRequest](docs/WorkspaceCreationRequest.md)
 - [WorkspaceItem](docs/WorkspaceItem.md)
 - [WorkspaceItemCreationRequest](docs/WorkspaceItemCreationRequest.md)
 - [WorkspaceItemUpdateRequest](docs/WorkspaceItemUpdateRequest.md)
 - [WorkspaceUpdateRequest](docs/WorkspaceUpdateRequest.md)
 - [WorkspaceVisibility](docs/WorkspaceVisibility.md)
 - [YearMonthDay](docs/YearMonthDay.md)
 - [YieldCurveData](docs/YieldCurveData.md)

