# context_data.py
EXPORTS_CONTEXT = [
    {"name": "Button", "type": "component",
        "description": "A styled button from shadcn/ui."},
    {"name": "Input", "type": "component",
        "description": "A styled input component for text, password, and email fields."},
    {"name": "Checkbox", "type": "component",
        "description": "A styled checkbox component."},
    {"name": "Card", "type": "component",
        "description": "UI card container for login layout."},
    {"name": "CardHeader", "type": "component",
        "description": "Card header for titles and subtitles."},
    {"name": "CardContent", "type": "component",
        "description": "Card body content section."},
    {"name": "CardFooter", "type": "component",
        "description": "Card footer section for actions."},
    {"name": "Label", "type": "component",
        "description": "Label component for form fields."},
    {"name": "useAuth", "type": "hook",
        "description": "React hook that provides authentication state."},
    {"name": "useForm", "type": "hook",
        "description": "React hook for handling form state and validation."},
    {"name": "loginFunc", "type": "function",
        "description": "Function for logging in the user with email and password."},
    {"name": "RegisterFunc", "type": "function",
        "description": "Function for register in the user "},
    {"name": "registerFunc", "type": "function",
        "description": "Function for registering a new user."},
    {"name": "forgotPasswordFunc", "type": "function",
        "description": "Function to send password reset instructions."},
    {"name": "socialLoginFunc", "type": "function",
        "description": "Function for login using Google, GitHub, or Facebook."},
    {"name": "getUrl", "type": "function",
        "description": "Function that returns the URL for the brand image."},
    {"name": "AuthProvider", "type": "component",
        "description": "Provider component for authentication context."},
    {"name": "Loader", "type": "component",
        "description": "Loading spinner for async actions."},
    {"name": "Alert", "type": "component",
        "description": "Alert banner to display success or error messages."},
    {"name": "PasswordStrengthMeter", "type": "component",
        "description": "Component that shows password strength."},
    {"name": "validateEmail", "type": "function",
        "description": "Utility function to validate an email address."},
    {"name": "validatePassword", "type": "function",
        "description": "Utility function to validate a password."},
    {"name": "useToggle", "type": "hook",
        "description": "Custom hook to toggle boolean state (e.g., show/hide password)."},
    {"name": "ThemeToggle", "type": "component",
        "description": "Switch component for toggling between light and dark mode."},
    {"name": "Divider", "type": "component",
        "description": "Horizontal divider component for separating sections."},


]

All_SCHEMAS = [  {
        "name": "RegisterSchema",
        "type": "object",
        "description": "Schema for user registration form with validation rules.",
        "properties": {
            "username": {
                "type": "string",
                "description": "Unique username chosen by the user.",
                "minLength": 3,
                "maxLength": 20
            },
            "email": {
                "type": "string",
                "description": "Valid email address of the user.",
                "format": "email"
            },
            "password": {
                "type": "string",
                "description": "Secure password with at least 8 characters, one uppercase, one number, and one special character.",
                "minLength": 8,
                "pattern": "^(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]+$"
            },
            "confirmPassword": {
                "type": "string",
                "description": "Re-entered password for confirmation. Must match the password field.",
                "const": {"$data": "1/password"}
            },
            "phoneNumber": {
                "type": "string",
                "description": "User’s phone number in international format.",
                "pattern": "^\\+?[1-9]\\d{1,14}$"
            },
            "age": {
                "type": "integer",
                "description": "Age of the user (must be at least 18).",
                "minimum": 18
            }
        },
        "required": ["username", "email", "password"]
    },]


def format_exports_context(exports):
    return "\n".join([f"- {e['name']} ({e['type']}): {e['description']}" for e in exports])
# def format_schema_context(exports):
#     return "\n".join([f"- {e['name']} ({e['type']}): {e['description']} {e['properties']} {e['required']}" for e in exports])
def format_schema_context(exports):
    formatted = []
    for e in exports:
        parts = []
        for key, value in e.items():
            parts.append(f"{key}: {value}")
        formatted.append(" | ".join(parts))
    return "\n".join(formatted)

