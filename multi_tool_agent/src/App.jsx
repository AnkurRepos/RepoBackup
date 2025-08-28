import React, { useState } from 'react';
import { Button } from './components/ui/button';
import { registerFunc } from './utils/register';

export default function App() {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
        phoneNumber: '',
        age: '',
    });
    const [errors, setErrors] = useState({});
    const [successMessage, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const validateForm = () => {
        let isValid = true;
        const newErrors = {};

        // Username validation
        if (!formData.username) {
            newErrors.username = 'Username is required';
            isValid = false;
        } else if (formData.username.length < 3 || formData.username.length > 20) {
            newErrors.username = 'Username must be between 3 and 20 characters';
            isValid = false;
        }

        // Email validation
        if (!formData.email) {
            newErrors.email = 'Email is required';
            isValid = false;
        } else if (!/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(formData.email)) {
            newErrors.email = 'Invalid email format';
            isValid = false;
        }

        // Password validation
        if (!formData.password) {
            newErrors.password = 'Password is required';
            isValid = false;
        } else if (!/^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$/.test(formData.password)) {
            newErrors.password = 'Password must have at least 8 characters, one uppercase, one number, and one special character';
            isValid = false;
        } else if (formData.password.length < 8) {
            newErrors.password = 'Password must be at least 8 characters';
            isValid = false;
        }

        // Confirm Password validation
        if (formData.confirmPassword !== formData.password) {
            newErrors.confirmPassword = 'Passwords do not match';
            isValid = false;
        }

        // Phone Number validation
        if (formData.phoneNumber && !/^\+?[1-9]\d{1,14}$/.test(formData.phoneNumber)) {
            newErrors.phoneNumber = 'Invalid phone number format';
            isValid = false;
        }

        // Age validation
        if (formData.age && (isNaN(formData.age) || parseInt(formData.age) < 18)) {
            newErrors.age = 'Age must be a number and at least 18';
            isValid = false;
        }

        setErrors(newErrors);
        return isValid;
    };

    const handleSubmit = async () => {
        if (validateForm()) {
            try {
                await registerFunc(formData);
                setSuccessMessage('Registration successful!');
                setErrorMessage('');
                // Optionally, redirect to login page or clear the form
                setFormData({
                    username: '',
                    email: '',
                    password: '',
                    confirmPassword: '',
                    phoneNumber: '',
                    age: '',
                });
                setErrors({});
            } catch (error) {
                setErrorMessage(error.message || 'Registration failed');
                setSuccessMessage('');
            }
        }
    };

    return (
        <div>
            <h1>Registration Page</h1>

            {successMessage && <div style={{ color: 'green' }}>{successMessage}</div>}
            {errorMessage && <div style={{ color: 'red' }}>{errorMessage}</div>}

            <label>Username:</label>
            <input type="text" name="username" value={formData.username} onChange={handleChange} /><br />
            {errors.username && <div style={{ color: 'red' }}>{errors.username}</div>}

            <label>Email:</label>
            <input type="email" name="email" value={formData.email} onChange={handleChange} /><br />
            {errors.email && <div style={{ color: 'red' }}>{errors.email}</div>}

            <label>Password:</label>
            <input type="password" name="password" value={formData.password} onChange={handleChange} /><br />
            {errors.password && <div style={{ color: 'red' }}>{errors.password}</div>}

            <label>Confirm Password:</label>
            <input type="password" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} /><br />
            {errors.confirmPassword && <div style={{ color: 'red' }}>{errors.confirmPassword}</div>}

            <label>Phone Number:</label>
            <input type="tel" name="phoneNumber" value={formData.phoneNumber} onChange={handleChange} /><br />
            {errors.phoneNumber && <div style={{ color: 'red' }}>{errors.phoneNumber}</div>}

            <label>Age:</label>
            <input type="number" name="age" value={formData.age} onChange={handleChange} /><br />
            {errors.age && <div style={{ color: 'red' }}>{errors.age}</div>}

            <Button onClick={handleSubmit}>Register</Button>
        </div>
    );
}