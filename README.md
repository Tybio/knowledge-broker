# knowledge-broker
A daemon that watches folders and formats and sends data to a notes application (Obsidan)

Technical Specification: The Knowledge Broker (v1.0)
1. Project Overview
A Python-based daemon that automates the ingestion, transformation, and delivery of files. The system follows a Pipe-and-Filter architecture where data flows through discrete, modular plugins.

2. Core Requirements
Operating System: Primary target is Linux (systemd), with architectural compatibility for Windows (via pywin32).

Execution Model: Single-threaded, sequential loop (No concurrency required).

Discovery: Plugins are loaded dynamically from ./plugins/input/, ./plugins/transform/, and ./plugins/output/.

Persistence: A SQLite database (broker.db) must track file hashes to prevent re-processing.

3. The Data Handshake (The "Envelope")
All plugins must accept and return a DataEnvelope object. This ensures metadata and secondary files (artifacts) travel together.

Referenced Schema (schema.py):

4. Plugin Constraints
Every plugin must inherit from a base class to ensure method consistency.

Referenced Interface (base_plugin.py):

Input Plugins: Must implement fetch_new_items() -> List[DataEnvelope].

Transform Plugins: Must implement process(envelope: DataEnvelope) -> DataEnvelope.

Output Plugins: Must implement deliver(envelope: DataEnvelope) -> bool.

5. Configuration Logic
The daemon reads config.yaml to map inputs to specific transformation chains.

Validation: If a plugin listed in config.yaml is missing from the /plugins directory, the daemon should log an error and skip that pipeline.

6. Error Handling & Logging
Failed Transitions: If a transformation fails, the original file must be moved to a /failed directory.

Logging: Use the standard logging library. Every file processed must have an entry: [TIMESTAMP] SUCCESS: meeting_notes.docx -> obsidian_vault.

How to use this with your AI Engine
Phase 1 (The Foundation): Ask the AI to create the schema.py and base_plugin.py based on the code above.

Phase 2 (The Broker): Provide the Spec Document and ask it to write broker.py (the main loop). Tell it to: "Reference schema.py and base_plugin.py to ensure the core loop can handle any plugin that follows those interfaces."

Phase 3 (The Plugins): Ask for individual plugins: "Write an Input plugin for folder watching that returns a DataEnvelope as defined in schema.py."