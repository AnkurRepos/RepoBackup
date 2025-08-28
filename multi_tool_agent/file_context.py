# file_context.py
EXISTING_FILE_CODE = {
    "src/App.jsx": """
import React from 'react';
import { Button } from './components/ui/button';
import { loginFunc } from './utils/login';

export default function App() {
    const handleLogin = async () => {
        try {
            console.log("hello")
            await loginFunc();
        } catch (error) {
            console.error("Login failed", error);
        }
    };

    return (
        <div>
            <h1>Login Page</h1>
            <Button onClick={handleLogin}>Login</Button>
        </div>
    );
}
"""
}


def file_context_str(file_code):
    file_context_str = "\n".join(
        [f"File: {path}\n{code}" for path, code in file_code.items()]
    )
    return file_context_str
