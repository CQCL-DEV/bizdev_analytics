# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## [1.2.1] - 2023-03-09

### Changed
- Documentation will force light mode for now (for legible circuit/dataframe rendering).
### Added
- Additional logging when new teams or experiments are created.
- A warning when a circuit is retrieved by name with multiple matches.
- A warning when a refresh token will expire in the next 12 hours.
- A `full_login` method on the `Myqos` object to directly reauthenticate (if needed).
- InQuanto guide and notebook to the documentation.

## [1.2.0] - 2023-02-28
### Fixed
- Example notebooks now include `user_group` when creating a configuration for the quantinuum backend.

### Added
- Moved the `available_devices` method to the `Myqos` object (but remains available as a class method on `MyqosBackend`).

### Changed
- Always re-upload circuit when submitting CompileJobs and ProcessJobs (instead of relying on `CircuitID`).

### Internal

- `Myqos` methods to retrieve teams now return a `MyqosTeam` object.
- `MyqosExperiment` now uses a team's display name (with correct capitalisation).
- Remove navbar injection from pytket-myqos docs.
- Publish `pytket-myqos` to Cloudsmith in release workflow.

## [1.1.2] - 2023-01-24
### Added
- Updated support for custom compiler flags to be passed as part of `QuantinuumConfig`.

### Changed
- When creating a local BraketBackend the region is now set and obtained from the provider
  using the `provider_regions()` hard-coded values.
- Increased the minimum supported `myqos-dataclasses` version to 1.1.4.

### Fixed
- A bug where circuit with boxes containing UUIDs could not be serialized back to pytket circuits.


## [1.1.1] - 2023-01-24
### Added
- Method to retrieve the `JobStatus` of a `CompileJobItem`.

### Fixed
- Use correct URL for getting the status of a `ProcessJobItem`.


## [1.1.0] - 2023-01-24
### Changed
- Now supported only for Python versions 3.9, 3.10 (3.11 support coming soon).
- Use default pytket-myqos logger for the websocket connection.

### Fixed
- Fixed authentication logic for websocket connection when checking job status.


## [1.0.0] - 2023-01-13
### Added
- MyqosExperiment method to request a list of unfinished jobs of specific types.
- Method to retrieve JobStatuses for a Job's JobItems.

### Changed
- The backend_info attribute in `MyqosResult` now contains the `BackendInfo` at time of running.
- Refactored custom exceptions. These are now documented in our API docs.
- Add favicon to docs.
- Randomly generated names for jobs and experiments now use a sequence of random mycological words 
  and will retry in the case of conflicts.
- Job submissions via the MyqosExperiment object now require a unique name to be provided by the user.
- Loading API keys will be attempted by default, but will fail silently and then prompt for SSO credentials. 

### Fixed
- Errors during remote compilation are now correctly raised in `MyqosBackend.get_compiled_circuits()`.
- Fixed a bug where remote compilation would hang on completion.

### Removed
- Legacy `ResultHandle`s can now only be used to obtain results via the `MyqosExperiment` object.
- Removed most references to `keyring` from the docs as it is no longer used for now.

## [1.0.0a1] - 2022-11-29
### Added
- New classes `ProcessJob`, `CompileJob`, `ProcessJobItem` and `CompileJobItem`.
- Added methods to create, list and retrieve Myqos Jobs.
- Support for authenticating via the new Myqos Single Sign On (SSO) and multi-factor authentication (MFA).
- String representations for Jobs.

### Changed
- `get_circuit` can now retrieve a circuit by name.
- `remote=True` is now the default in MyqosBackend for compilation and getting backend_info.
- The Myqos ResultHandle format has changed to ResultHandle(JobID, JobItemID).
- Moved MyqosCircuit and MyqosResult to `/pytket_myqos_types`.
- MyqosBackend now uses Jobs behind the scenes for circuit processing and compilation.
- Changed base url from `myqos.com/api` to `myqos.com` in MyqosConfig.
- An attempt will be made to use API tokens via Keyring, with a fall back to attempting SSO. This behaviour
  is configurable.
- Job submissions use existing circuit ids when available, avoiding duplicate uploads.

### Removed
- Remove the deprecated `cost_estimate`, which has been replaced by `cost`. 
- Remove the handle member of MyqosResult.
- Deprecated `get_job_info`.
- Dropped support for the legacy ResultHandle(ResultID,).

### Internal
- Removed unused client methods for processing and compiling via the v5 API.

## [0.24.3] - 2022-10-27

### Added
- `get_credentials` method in Myqos will retrieve the names for backends that the user has credentials for.

### Changed
- `available_devices` now gets BackendInfos for all backends available to the user if none are specified.
- Plotting histograms for results with many counts will now warn the user.
- Probability digits in histograms now truncated to 3 decimal points.

### Fixed
- Circuits containing certain boxes failing to serialise when fetched from the remote backend.

## [0.24.2] - 2022-10-24

### Internal
- Use new group syntax for poetry dev and docs dependencies.

## [0.24.1] - 2022-10-21

### Internal
- Issue with dependencies when building documentation.

## [0.24.0] - 2022-10-21

### Added
- Additional logic for handling CryptFileKeyring.
- MyqosBackend method for retrieving ResultHandles for circuits in an internal Myqos priority queue.
- Optional user-provided ResultHandle when uploading a non-Myqos result.
- `Myqos` method to get the names of backends that the user has credentials for.

### Changed
- Moved the import path for `set_keyring_credentials` to `pytket.extensions.myqos`.
- Reduced the default verbosity of logging when using websockets.

### Internal
- Avoid Python 3.10.7 for type checking in the CI due to known bug (see: https://github.com/pandas-dev/pandas-stubs/issues/296#issuecomment-1245527765)
- Updates all remaining endpoints to use v5 API (`cancel` and `get_team_by_name`).
- Add pytest-icdiff as a dev dependency, for clearer diffs in test failures.
- Client method for retrieving the contents of a device's priority queue.
- Validate experiment_id in `get_experiment_by_id.`

## [0.23.2] - 2022-09-07
### Changed
- Reverted ZZPhase pytket-quantinuum hotfix

### Internal
- Reverted to test against last 5 versions of pytket in the CI.

## [0.23.1] - 2022-09-06
### Added
- Additional documentation on JupyterHub.
- Deprecation warning for `cost_estimate` and `get_job_info`.
### Fixed 
- Some metadata in MyqosResult and MyqosCircuit are no longer unneccesarily nested in Tuples.

## [0.23.0] - 2022-09-02
### Added
- Added MyqosExperiment methods to upload pytket `Circuit`s and `BackendResult`s to the Myqos database.
- `process_circuit(s)` now accepts the `valid_check` parameter for toggling backend validity checks.

### Changed
- All Myqos API interactions (bar `cancel`, `get_team_by_name` and `job_info`) now use Myqos' v5 API.
- Now stores hostname/keyring configuration using the Pytket config file (defaults to ~/.config/pytket/config.json).
- Now checks for credentials via keyring and `.netrc` before raising an Exception.
- `create_team` now returns a TeamRecord instead of only the TeamID.

### Internal
- `get_result` and `get_compiled_circuits` (with remote=True) now poll the API using websockets.
- Allow for nested asyncio event loops using `nest_asyncio` (required for Jupyter notebooks)
- Use hotfix version of pytket-quantinuum for the current quantinuum gateset (pytket-quantinuum-myqos)
- Current hotfix limits working pytket versions to (>=1.4.1), reflect this in the testing CI to only test against last 2 versions. 

## [0.22.1] - 2022-08-02
### Added
- Support for pytket 1.4.

## [0.22.0] - 2022-07-29
### Added
- Static backend properties (e.g. supports_state, supports_unitary, supports_counts)
- Added 'name' filter parameter when retrieving circuits with `get_circuits`.
- Support for ProjectQ pytket backend.

### Changed
- The `backend_info` method now uses the v5 API.
- Simplified `get_job_info` to return a JSON string.
- The `cost` method now uses the v5 API.

## [0.21.2] - 2022-07-06
### Internal
- Upgraded the pytket version back to 1.* to stay compatible with the current Inquanto, and to download the latest pytket v1 release.

### Changed
- `Client` class is now a singleton object to reduce repeated keyring interactions.

## [0.21.1] - 2022-07-01
### Removed
- Removed `cost_code` fields from experiment and circuit records, and from requests
  to process circuits.

### Internal
- Reverted the pytket version back to 1.1 to stay compatible with the current Inquanto.

## [0.21.0] - 2022-06-28
### Added
- The MyqosResult and MyqosCircuit types.
- Myqos Assistant to help optionally print user help messages as logs.
- The MyqosExperiment class.
- `get_handles` method to the MyqosBackend class.
- MyqosBackend can alternatively be initialised with an `experiment_name`.
- Documentation notebooks outlining example usage with `BraketConfig` and `QulacsConfig`.
### Changed
- Methods that previously returned Iterators now return Lists.
- Experiments can be retrieved by name alone.
- `new_experiment()` now autogenerates a name if none is provided.
- Added additional customization for results plotting.
- The Myqos class now handles administrative tasks (team/experiment management).
- Moved `get_job_info` for Quantinuum jobs to the MyqosBackend.

### Removed
- Removed the deprecated `compile_circuit` method in `MyqosBackend`.

### Internal
- Added fixtures for commonly used test data.
- Set 'WARNING' as default log level for library loggers to reduce noise.
- Fixed incorrect field name for NewDeviceRecord in compilation_handler.
- Updated  `myqos_dataclasses`

## [0.20.2] - 2022-05-27
### Changed
- Updated the required pytket version to 1.1, rather than 1.0.x.
- Consolidated Myqos documentation with updated styling.
- Development packages are now tagged as pre-releases instead of post-releases.

## [0.20.1] - 2022-04-27
### Added
- Warning message when keyring isn't able to find API credentials.
### Changed
- Updated to reference new Quantinuum device names.
- Update to use latest mushroom-dataclasses with a different default for
  QuantinuumConfig.user_group.

## [0.20.0] - 2022-03-30
### Added
- Additional documentation on getting set up.
- Added `cost_estimate` for backends with QuantinuumConfigs.
### Changed
- Updated pytket version to 1.0.
- Changed references from 'Honeywell' to 'Quantinuum'.
- Renamed methods that return iterators to reference this.
- Renamed `Myqos.get_result` to `Myqos.get_result_record`.
- Replaced use of ResultID in the Myqos class with ResultHandle.
- `MyqosBackend.process_circuits` now allows `n_shots` to be a list of shot numbers
  (to allow for different circuits to use different n_shots). This is now in line with other
  pytket backends.
- Changed base URL from cloud.cambridgequantum.com to myqos.com.
- Reduced network calls during compilation, reducing compilation time.

### Removed
- Dropped support for pytket-oqc, until a version is released for pytket 1.0.
- Deprecated `compile_circuit`, use `get_compiled_circuit(s)` going forward.

### Internal
- Changed CI to test against pytket versions greater than 1.0, this will mean new versions
of pytket-myqos will not support older versions of pytket or mushroom-dataclasses.
- Added dependabot for package version updates.

## [0.19.1] - 2022-03-04
### Internal
- Introduce a backoff when checking circuit status with get_results. 
- Upgrade mushroom-dataclasses to v0.44.1 to support submitting groups

## [0.19.0] - 2022-02-22
### Added
- HoneywellConfig can now be used to submit circuits to HQS-LT (the Honeywell machine
  family queue).
- When submitting circuits to be processed in Myqos, HoneywellConfig now has a default
  `device_name` of "HQS-LT" if no device name is specified.

## Changed
- Renamed 'Group' to 'Team'.

## [0.18.0] - 2022-02-14
### Added
- Parameter to Myqos.get_experiments() to retrieve only experiments with a particular
  cost code.

### Changed
- Added support for pytket 0.19.
- Dropped support for python 3.7.

## [0.17.0] - 2022-01-18
### Added
- Added automated testing for support for `pytket` versions 0.15.0 through 0.18.0.
- Added methods to `Myqos` to interact with experiment access-control list (ACL).
- Added FAQ and troubleshooting pages to the pytket-myqos documentation website.
- Added `patch_experiment` to support changing the group ownership of an experiment.
- Added optional `cost_code` field when creating new experiments and processing circuits.

### Changed
- pytket version constraints are now relaxed to tolerate pytket versions 0.14.0 through 0.18.0.
- Updated mushroom-dataclasses dependency to 0.39.0.

## [0.16.0] - 2021-11-29
### Added
- Re-exported `Myqos` from `pytket.extensions.myqos.myqos` in `pytket.extensions.myqos`.
- Added an argument to `MyqosBackend` to set default value for remote compilation toggle.

### Changed
- Flexible version contraints for the pytket-extensions.
- `backend_info` can now be toggled to collect information remotely or locally from the global flag.
- `backend_info` can now be optional when returned by pytket-myqos.

## [0.15.0] - 2021-11-23
## Added
- Added docs page listing backend_configs.
- Added support for pytket-qulacs.

## [0.14.0] - 2021-11-17
### Changed
- pytket-myqos now requests BackendInfo from the vendors via mushroom.
- Updated dependencies: pytket;^0.14.0, mushroom-dataclasses;0.32, pytket-braket;^0.11.0, pytket-oqc;^0.3.3, 
pytket-honeywell;^0.15.0, pytket-qiskit;^0.17.0.

### Added
- `group_name`, `user_name`, and `name` filters to `Client.list_experiments`.
- `get_remotely_compiled_circuit_with_pass` and `get_compiled_circuit_with_pass` methods to `compilation_handler`.
- `compile_with_custom_pass` example.
- `submittedAfter`, `submittedBefore`, and `name` filters to `list_circuits`.
- Added Myqos class as a Client wrapper and member attribute of MyqosBackend.
- Added visualisation helper script for plotting results using `matplotlib`.

### Internal
- Notebooks moved to `docs/source/example_notebooks` folder. 
- README updated for developer reference.
- Created github workflow to build docs using Sphinx.
- `MyqosValidatorConfig` has replaced `MushroomValidatorConfig`.

## [0.13.0] - 2021-09-23
### Changed
- pytket-myqos no longer generates QASM for circuits.
- Experiments can be created per-user and Experiment models have been updated to reflect this.
- Update pytket-honeywell to v0.14.
- Update mushroom-dataclasses dependency to v0.31.

## [0.12.0] - 2021-09-09
### Added
- `get_compiled_circuit` and `get_compiled_circuits` methods.

### Changed
- `Backend.new_experiment` now takes basic types as arguments rather than `NewExperiment`.
- Client and tests to use new group API endpoints.
- `HoneywellBackend` no longer overrides `machine_debug` setting in config in favor of `login`
- Check the users keyring for credentials before looking in the `~/.netrc` file.
- Client now uses Spore v4 API.
- Client handles the new JSON structure for paginated list endpoints.
- Group ID is now optional when creating experiments.

### Removed
- `DevicesMixin`.

## [0.11.2] - 2021-08-02
### Changed
- Update mushroom-dataclasses dependency to v0.22.2.

## [0.11.1] - 2021-08-02
### Changed
- Update pytket-oqc dependency to v0.3.2.
- Use `from_pytket_circuit` of NewCircuitRecord.
- Support `page_size` and `page_number` arguments for results.

### Removed
- Ineffectual `examples` flag removed.

## [0.11.0] - 2021-07-29
### Added
- `new_group` method for creating groups.
- Local support for `IBMQEmulatorBackend`.
- Re-export Config dataclasses from mushroom_dataclasses to make imports easier.
- New client methods for most myqos API endpoints.
- Support for listing and getting information about groups via the API.
- Added `honeywell` and `qiskit` feature flags for installing relevant extensions.
- `oqc` feature flag for installing `pytket-oqc`.
- Braket support through the `braket` feature flag.
- Added `supported_configs()` method to list the configs we support.

### Changed
- `Client` has been refactored into a new module.
- `Client.get_result` has been renamed `Client.get_backendresult` and internal usage
   of the method has been updated.
- Update pytket dependency to v0.13.0.
- Update mushroom-dataclasses dependency to v0.22.0.
- Update pytket-oqc dependency to v0.3.0.

## [0.10.0] - 2021-06-08
### Added
- `remote` flag to remotely compile circuits with `CQCBackend.compile_circuit()`.
- `process_circuit` and `process_circuits` now use the new batch submission
   endpoint which does not compile circuits automatically.

### Changed
- Update pytket dependency to v0.11.0.
- Rename project to pytket-myqos

## [0.9.0] - 2021-05-10
### Added
- `OQCBackend` support.
- `IBMQEmulatorBackend` support.

## [0.8.1] - 2021-05-04
### Added
- Changelog file for pytket-cqc.

### Changed
- The poetry.lock dependency file for pytket-cqc is now included by default, to make
  third-party libraries less able to cause breaking changes to pytket-cqc in testing.

### Fixed
- Bug where there was a type-checking error in one of the pytket-cqc tests. The type
  check is now correct.

## [0.8.0] - 2021-04-16
### Added
- `CQCBackend.device` property, which returns the `.device` property of the pytket
  backend that Mushroom is actually using (e.g. HoneywellBackend, IBMQBackend).

### Changed
- Configure the HTTP session that CQCBackend uses to call Mushroom so that it will
  retry requests if the Mushroom server is temporarily unavailable.

## [0.7.2] - 2021-04-13
### Added
- Support for Aer simulators via `AerConfig`, `AerStateConfig` and `AerUnitaryConfig`.

## [0.7.1] - 2021-04-12
### Fixed
- Bug where `CQCBackend.__init__` compared a backend config instance to a set of
  backend config class types, and would always evaluate as `False`.

## [0.7.0] - 2021-04-09
### Changed
- Use full `CircuitStatus` in `Client.get_circuit_status`, rather than only parsing
  some possible status strings.

## [0.6.0] - 2021-04-09
### Changed
- Update pytket dependency to v0.9.
- Update pytket-honeywell dependency to v0.8.0.

## [0.5.0] - 2021-04-05
### Added
- `MushroomValidatorConfig` as a valid backend config class. This can be used to
  test that Mushroom is running commands correctly without using resources on a
  remote provider.

## [0.4.0] - 2021-03-25
### Added
- Instrumentation to save (to Spore) the compilation passes and the circuits that
  they generate. This is automatically used in `CQCBackend.compile_circuit()`.
- Dependency on pytket-honeywell v0.7.0.

### Changed
- CQCBackend now takes a backend config class to choose which remote provider to use,
  rather than just a string with the name. It also uses this configuration data to
  decide (for example) which IBMQ or Honeywell machine to use, rather than hardcoding
  the machine details.
- Update README to reflect use of backend config classes.
- Update mushroom-dataclasses dependency to v0.7.0.

## [0.3.0] - 2021-03-23
### Added
- `CQCBackend.get_third_party_handle()` method to get the ResultHandle from the
  remote provider (such as IBMQ or Honeywell) if we have a ResultHandle from
  Mushroom.

### Changed
- Update mushroom-dataclasses dependency to v0.5.0.

### Fixed
- `CQCBackend.get_result()` now waits for the result to be completed, rather than
  raising an error if the result was not completed the first time it checked.

## [0.2.1] - 2021-03-09
### Changed
- Updated mushroom-dataclasses dependency to v0.4.0.

## [0.2.0] - 2021-03-09
### Added
- First version of `CQCBackend`, a backend class for Pytket that can connect to remote
  providers via Mushroom, and save circuits and results to a Mushroom account.
- Tests for the new CQCBackend.
- `Client` class for CQCBackend to communicate with Mushroom.

[0.2.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.2.0
[0.2.1]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.2.1
[0.3.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.3.0
[0.4.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.4.0
[0.5.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.5.0
[0.6.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.6.0
[0.7.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.7.0
[0.7.1]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.7.1
[0.7.2]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.7.2
[0.8.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.8.0
[0.8.1]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.8.1
[0.9.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.9.0
[0.10.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.10.0
[0.11.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.11.0
[0.12.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.12.0
[0.13.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.13.0
[0.14.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.14.0
[0.15.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.15.0
[0.16.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.16.0
[0.17.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.17.0
[0.18.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.18.0
[0.19.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.19.0
[0.19.1]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.19.1
[0.20.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.20.0
[0.20.1]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.20.1
[0.20.2]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.20.2
[0.21.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.21.0
[0.21.1]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.21.1
[0.21.2]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.21.2
[0.22.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.22.0
[0.22.1]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.22.1
[0.23.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.23.0
[0.23.1]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.23.1
[0.23.2]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.23.2
[0.24.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.24.0
[0.24.1]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.24.1
[0.24.2]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.24.2
[0.24.3]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v0.24.3
[1.0.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v1.0.0
[1.1.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v1.1.0
[1.1.1]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v1.1.1
[1.1.2]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v1.1.2
[1.2.0]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v1.2.0
[1.2.1]: https://github.com/CQCL-DEV/pytket-myqos/releases/tag/v1.2.1
