import React from "react";
import { modules } from "./modules";
import "./CSS/Topbar.css";

interface TopbarProps {
    activeModule: string;
}

const Topbar: React.FC<TopbarProps> = ({ activeModule }) => {
    const module = modules[activeModule];

    return (
        <header className="topbar">
            <div className="topbar-content">
                <h1 className="topbar-title">{module?.name || "Dashboard"}</h1>
                <div className="topbar-divider"></div>

                <nav className="topbar-nav">
                    {module?.subcategories.map((sub, i) => (
                        <button key={i} className="topbar-link">
                            {sub}
                        </button>
                    ))}
                </nav>
            </div>
        </header>
    );
};

export default Topbar;
