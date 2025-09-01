// components/Button.tsx
import React from "react";
import "./CSS/Button.css";

interface ButtonProps {
    children: React.ReactNode;
    onClick?: () => void;
    type?: "button" | "submit" | "reset";
    variant?: "def-button" | "add" | "search";
    icon?: React.ReactNode;
    iconPosition?: "left" | "right";
}

const Button: React.FC<ButtonProps> = ({
                                           children,
                                           onClick,
                                           type = "button",
                                           variant = "def-button",
                                           icon,
                                           iconPosition = "left",
                                       }) => {
    return (
        <button className={`btn ${variant}`} onClick={onClick} type={type}>
            {icon && iconPosition === "left" && <span className="btn__icon">{icon}</span>}
            <span className="btn__label">{children}</span>
            {icon && iconPosition === "right" && <span className="btn__icon">{icon}</span>}
        </button>
    );
};

export default Button;
