import React from "react";
import MenuIcon from "./icons/MenuIcon";
import XIcon from "./icons/XIcon";
import ChevronRightIcon from "./icons/ChevronRightIcon";
import { modules } from "./modules";
import "./CSS/Sidebar.css";

interface SidebarProps {
    expanded: boolean;
    activeModule: string;
    onToggle: () => void;
    onSelect: (key: string) => void;
}

const Sidebar: React.FC<SidebarProps> = ({ expanded, activeModule, onToggle, onSelect }) => {
    return (
        <div className={`sidebar ${expanded ? "expanded" : "collapsed"}`}>

            {/* Header */}
            <div className="sidebar-header">
                {expanded && <h2 className="sidebar-title">ERP Sistema</h2>}
                <button onClick={onToggle} className="sidebar-toggle">
                    {expanded ? <XIcon /> : <MenuIcon />}
                </button>
            </div>

            {/* Módulos */}
            <nav className="sidebar-nav">
                {Object.entries(modules).map(([key, module]) => {
                    const Icon = module.icon;
                    const isActive = activeModule === key;

                    return (
                        <button
                            key={key}
                            onClick={() => onSelect(key)}
                            className={`sidebar-item ${isActive ? "active" : ""}`}
                        >
                            <Icon />
                            {expanded && (
                                <>
                                    <span className="sidebar-label">{module.name}</span>
                                    <div className={`chevron ${isActive ? "rotated" : ""}`}>
                                        <ChevronRightIcon />
                                    </div>
                                </>
                            )}
                        </button>
                    );
                })}
            </nav>
        </div>
    );
};

export default Sidebar;
