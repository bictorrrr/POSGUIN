import React from "react";
import { modules } from "./modules";
import HomeIcon from "./icons/HomeIcon";
import "./CSS/ContentArea.css";


interface ContentAreaProps {
    activeModule: string;
}

const ContentArea: React.FC<ContentAreaProps> = ({ activeModule }) => {
    const module = modules[activeModule];
    const Icon = module?.icon || HomeIcon;

    return (
        <main className="content-area">
            <div className="content-area__container">
                <div className="content-area__header">
                    <div className="content-area__icon-wrapper">
                        <Icon className="content-area__icon" />
                    </div>
                    <h2 className="content-area__title">
                        Bienvenido al {module?.name || "Dashboard"} 🚀
                    </h2>
                    <p className="content-area__subtitle">
                        Aquí aparecerá el contenido del módulo seleccionado
                    </p>
                </div>

                <div className="content-area__cards">
                    {module?.subcategories.slice(0,3).map((sub, i) => (
                        <div key={i} className="content-area__card">
                            <h3 className="content-area__card-title">{sub}</h3>
                            <p className="content-area__card-text">Contenido de {sub.toLowerCase()}</p>
                        </div>
                    ))}
                </div>
            </div>
        </main>
    );
};

export default ContentArea;
