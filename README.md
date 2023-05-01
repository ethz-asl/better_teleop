# Better Teleop

This package provides the `better_teleop.py` script which allows sending velocity commands to a robot using the keyboard's arrow keys without a terminal window being in focus.

The package utilizes the `pynput` Python package. The dependency can be installed using:

```bash
pip install .
```

The node is launched via

```bash
roslaunch better_teleop better_teleop.launch
```

The launch file also contains the parameters of the script which are the topic onto which to publish velocity commands (`cmd_topic`), as well as the rates to use when computing the command to send, i.e. `forward_rate, backward_rate, rotation_rate`.
