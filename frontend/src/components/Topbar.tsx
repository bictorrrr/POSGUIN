import React from "react";
import { modules } from "./modules";
import "./CSS/Topbar.css";

interface TopbarProps {
    activeModule: string;
    activeSub: string | null;
    onSubSelected: (name: string) =>  void;
}

const Topbar: React.FC<TopbarProps> = ({ activeModule, activeSub, onSubSelected }) => {
    const module = modules[activeModule as keyof typeof modules];

    return (
        <header className="topbar">
            <div className="topbar-content">
                <h1 className="topbar-title">{module?.name || "Dashboard"}</h1>
                <div className="topbar-divider"></div>

                <nav className="topbar-nav">
                    {module?.subcategories.map((sub: string, i: number) => (
                        <button
                            key = {i}
                            onClick={() => onSubSelected(sub)}
                            className={`topbar-link ${activeSub === sub ? "active" : ""}`}
                        >
                            {sub}
                        </button>
                    ))}
                </nav>
            </div>
        </header>
    );
};

export default Topbar;
