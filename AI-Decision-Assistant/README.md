# AI Decision-Making for Commuting Assistant

This project simulates an AI-based decision-making system to suggest the best commuting option based on various conditions such as weather, traffic, and strikes. It uses propositional logic to represent conditions, define commuting options, and create a knowledge base for making decisions.

## Project Tasks

### 1. Represent the Conditions
Conditions influencing the decision-making are represented as symbols:
- **Rain**: Indicates whether it is raining.
- **HeavyTraffic**: Indicates if traffic is heavy.
- **EarlyMeeting**: Indicates if there is an early meeting.
- **Strike**: Indicates if there is a public transport strike.
- **Appointment**: Indicates a doctor's appointment in the afternoon.
- **RoadConstruction**: Indicates road construction.

### 2. Define the Commuting Options
The commuting options are:
- **WFH**: Work from home.
- **Drive**: Drive to work.
- **PublicTransport**: Use public transport.

### 3. Create the Knowledge Base
The knowledge base includes rules:
- If it’s raining or there’s an early meeting, work from home.
- If it’s not raining and there’s no heavy traffic, drive.
- If there’s no strike and it’s not raining, use public transport.
- If there’s a doctor’s appointment, drive.
- If there’s road construction, avoid driving.

### 4. Define Queries
The system checks:
- Should you work from home?
- Should you drive?
- Should you use public transport?

### 5. Perform Model Checking
Scenarios are evaluated using the `model_check` function to verify if the knowledge base suggests the correct commuting option.

### 6. Modify the Conditions
The conditions in different scenarios are modified, and the assistant's decisions are reevaluated.

## How to Run the Code

1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   cd AI-Decision-Assistant
   ```
2. Ensure Python 3.x is installed on your machine.
3. Run the Python script:
```bash
python3 logic.py
```
4. Observe the output in the terminal, which includes the AI assistant’s decisions for each scenario.

## Expected Output
Scenarios
Scenario 1: It’s raining, and there’s heavy traffic.
Output:
```bash
WFH: True
Drive: False
PublicTransport: False
```

Scenario 2: There’s a public transport strike, and it’s not raining.
Output:
```bash
WFH: False
Drive: True
PublicTransport: False
```

Scenario 3: There’s no rain, traffic is light, and there’s no strike.
Output:
```bash
WFH: False
Drive: True
PublicTransport: True
```

Scenario 4: No rain, heavy traffic, early meeting, doctor’s appointment, and road construction.
Output:
```bash
WFH: True
Drive: False
PublicTransport: False
```