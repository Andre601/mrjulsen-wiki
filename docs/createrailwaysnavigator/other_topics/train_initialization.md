---
categories:
  - Create Railways Navigator
---

# Train Initialization

## World/Server restart
After the world/server has been restarted, trains may not be displayed immediately. To avoid calculation errors, each train must reach its next scheduled stop before CRN can display and use it. Depending on the size of the train network, this may take a few minutes.

## New trains
Trains that have been newly assembled, have received a new schedule or were invalid, are not immediately suggested or displayed by CRN. It takes at least one cycle (the complete train schedule from start to end plus 1 more station) before CRN can show these trains. This is because in this phase CRN has to measure and store the route of the train, its travel times and some other information so that it can then navigate based on these information.