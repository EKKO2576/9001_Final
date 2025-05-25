# Virtual Pet System

This is a Python-based console application that simulates a virtual pet. The user interacts with the pet by issuing commands that affect its core attributes. The game is turn-based, and the pet's condition changes both through user actions and daily natural decay.

## Features

- Interactive command-line interface
- Daily cycle with action limits
- Four key attributes:
  - Cleanliness
  - Energy
  - Interaction
  - Appearance
- Pet state degrades over time if neglected
- Pet dies if in poor condition for too long
- Daily status report and feedback
- Modularized design using multiple `.py` files

## Commands

- `bathe` – Clean your pet and improve interaction
- `rest` – Restore your pet’s energy
- `decorate` – Improve appearance and interaction
- `talk` – Improve interaction gradually
- `status` – View the pet’s current state
- `end_day` – Ends the current day, applies natural decay
- `quit` – Exit the program

## How It Works

Each day, the player can take a limited number of actions (e.g., 3). After the day ends, the pet’s state decays naturally. If the pet’s energy and interaction are both at the lowest level for multiple consecutive days, the pet will eventually die.

The user must maintain all attributes through a balance of actions. The game encourages planning and attention to state management.

## Example Output

```text
Day 1 begins.

Choose an action: bathe / rest / decorate / talk / status / quit
>> bathe
Fluffy is now clean. (Clean -> high, Interaction -> medium)

>> status
Fluffy's current status:
  Cleanliness   : high
  Energy        : medium
  Interaction   : medium
  Appearance    : medium
Dependencies
Python 3.x

No external packages required

How to Run
bash
复制
编辑
python main.py
