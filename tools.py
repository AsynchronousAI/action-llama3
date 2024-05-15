import pyautogui

def calculate(term):
    try:
        result = eval(term[0])
        return result
    except:
        return "Invalid expression."

def moveMouse(arg):
    try:
        pyautogui.moveTo(arg[0], arg[1])
        return "Mouse moved to the specified coordinates."
    except:
        return "Invalid coordinates."

def clickMouse(arg):
    try:
        pyautogui.click(arg[0], arg[1])
        return "Mouse clicked at the specified coordinates."
    except:
        return "Invalid coordinates."
    
def writeText(arg):
    try:
        pyautogui.write(arg[0])
        return "Text written."
    except:
        return "Invalid text."
    
def pressKey(arg):
    try:
        pyautogui.press(arg[0])
        return "Key pressed."
    except:
        return "Invalid key."


screenres = pyautogui.size()
functions = {
    "pyexpression": calculate,
    "movemouse": moveMouse,
    "clickmouse": clickMouse,
    "writetext": writeText,
    "presskey": pressKey,
}
tool = [
        {
            "name": "pyexpression",
            "description": "Use pyexpression to run Python expressions such as operators to validate your response. This should not effect your verbosity.",
            "arguments": [
                {
                    "type": "string", 
                    "description": "Mathematical expression to calculate.",
                }
            ],

            "examples": [
                "{'name': 'pyexpression', 'arguments': ['2 + 2']}",
                ]
        },
        {
            "name": "movemouse",
            "description": "Use movemouse to move the mouse to the specified coordinates.",
            "arguments": [
                {
                    "type": "integer", 
                    "description": "X coordinate to move the mouse to. This strictly requires an integer not an expression.",
                },
                {
                    "type": "integer", 
                    "description": "Y coordinate to move the mouse to. This strictly requires an integer not an expression.",
                }
            ],

            "example": [
                "{'name': 'movemouse', 'arguments': [100, 100]}",
                "{'name': 'movemouse', 'arguments': [860, 540]}",
            ]
        },
        {
            "name": "clickmouse",
            "description": "Use clickmouse to click the mouse at the specified coordinates.",
            "arguments": [
                {
                    "type": "integer", 
                    "description": "X coordinate to click the mouse at. This strictly requires an integer not an expression.",
                },
                {
                    "type": "integer", 
                    "description": "Y coordinate to click the mouse at. This strictly requires an integer not an expression.",
                }
            ],

            "example": [
                "{'name': 'clickmouse', 'arguments': [100, 100]}",
                "{'name': 'clickmouse', 'arguments': [860, 540]}",
            ]
        },
        {
            "name": "writetext",
            "description": "Use writetext to write the specified text.",
            "arguments": [
                {
                    "type": "string", 
                    "description": "Text to write.",
                }
            ],

            "example": [
                "{'name': 'writetext', 'arguments': ['Hello, World!']}",
                "{'name': 'writetext', 'arguments': ['This is a test.']}",
            ]
        },
        {
            "name": "presskey",
            "description": "Use presskey to press the specified key.",
            "arguments": [
                {
                    "type": "string", 
                    "description": "Key to press.",
                }
            ],

            "example": [
                "{'name': 'presskey', 'arguments': ['enter']}",
                "{'name': 'presskey', 'arguments': ['ctrl']}",
            ]
        },
]
