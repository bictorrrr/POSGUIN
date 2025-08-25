// src/components/Button.tsx
import React from "react"
import "./CSS/Button.css"

interface ButtonProps {
    children: React.ReactNode
    onClick?: () => void
    type?: "button" | "submit" | "reset"
}

const Button: React.FC<ButtonProps> = ({ children, onClick, type = "button" }) => {
    return (
        <button className="def-button" onClick={onClick} type={type}>
            {children}
        </button>
    )
}

export default Button
