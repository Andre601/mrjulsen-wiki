# Train validation

The mod only takes valid trains into account. Here is an overview of the criteria that must be met for the navigator to accept a train.
- The train must be assembled
- The train needs it's own train schedule (with loop enabled) and should at least run one cycle
- The train is not manual driven
- The train is not derailed
- The train schedule is running

/// note
After the world/server is restarted, it takes some time before a train is displayed correctly again. Only then it can be ensured that every entry in the schedule and all of the navigator's systems have correctly recognized and processed the train.
///