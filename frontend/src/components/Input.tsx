import React from "react"
import "./CSS/Input.css"

type InputProps = React.InputHTMLAttributes<HTMLInputElement> & {
    variant?: "default" | "modal" | "highlight"
}

const Input: React.FC<InputProps> = ({ variant = "default", ...props }) => {
    return (
        <input
            {...props}
            className={`input ${variant}`}
        />
    )
}

export default Input
