from tools.digitify import digitify, get_tool
from langflow.main import configure, setup_app
from langflow.interface.tools import constants
from langflow.interface.tools.base import ToolCreator, tool_creator


def get_tools(arg, kwarg=None):
    tools = ["Tool"]
    return tools


def get_tool_signature(arg, kwarg=None):
    tools = {
        "name": "Tool",
        "func": digitify,
        "description": "useful for when you need to digit text string, the input should be one string",
        "base_classes": ["Tool", "BaseTool"],
        "params": {
            "name": "Digit",
            "func": [digitify],
            "description": "useful for when you need to digit text string, the input should be one string",
        },
        "template": {
            "_type": "Tool",
            "func": {
                "type": "function",
                "is_list": False,
                "show": True,
                "value": [digitify],
                "multiline": True,
            },
            "text": {
                "type": "str",
                "required": True,
                "is_list": False,
                "show": True,
                "multiline": True,
            },

        }
    }
    return tools


if __name__ == '__main__':
    tool_creator.tools_dict["Tool"] = {
        "name": "Tool",
        "fcn": get_tool,
        "base_classes": ["function"],
        "description": "useful for when you need to digit text string, the input should be one string",
        "params": {
            "name": "Digit",
            "description": "useful for when you need to digit text string, the input should be one string",
            "fcn": digitify,

        },
    }
    ToolCreator.to_list = get_tools
    ToolCreator.get_signature = get_tool_signature
    import uvicorn

    configure()
    constants.ALL_TOOLS_NAMES = None
    uvicorn.run(
        setup_app,
        host="127.0.0.1",
        port=7860,
        log_level="debug",
    )
    constants.ALL_TOOLS_NAMES = None
