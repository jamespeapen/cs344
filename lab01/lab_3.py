from gps import gps

problem = {
    "start1": ["on cliff", "no parachute", "safe"],
    "finish1": ["safely landed"],

    "ops": [
        {
            "action": "jump off cliff",
            "preconds": ["on cliff"],
            "add": [
                "in air",
                "unsafe",
            ],
            "delete": [
                "on cliff"
            ]
        },
        {
            "action": "land",
            "preconds": [
                "in air"
            ],
            "add": [
                "off cliff",
                "landed",
                "unsafe"
            ],
            "delete": ["in air"]
        },
        {
            "action": "land safely",
            "preconds": [
                "parachute deployed",
                "in air"
            ],
            "add": [
                "safely landed"
            ],
            "delete": [
                "in air",
                "unsafe"
            ]
        },
        {
            "action": "deploy parachute",
            "preconds": [
                "in air",
                "has parachute"
            ],
            "add": [
                "parachute deployed",
            ],
            "delete": [
                "has parachute",
            ]
        },
        {
            "action": "get parachute",
            "preconds": [
                "on cliff",
                "no parachute"
            ],
            "add": [
                "has parachute",
            ],
            "delete": [
                "no parachute",
            ]
        }
    ]
}
#


def main():
    start = problem['start1']
    finish = problem['finish1']
    ops = problem['ops']
    actionSequence = gps(start, finish, ops)
    if actionSequence is None:
        print("plan failure...")
        return
    for action in actionSequence:
        print(action)


if __name__ == '__main__':
    main()
