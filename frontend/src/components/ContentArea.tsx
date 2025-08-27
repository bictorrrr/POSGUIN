import React from "react";
import { modules } from "./modules";
import HomeIcon from "./icons/HomeIcon";
import "./CSS/ContentArea.css";
import {InventarioProductosPage, InventarioCategoriasPage} from "../layouts/inventory";

interface ContentAreaProps {
    activeModule: string;
    activeSub: string | null;
}

const contentByModule: Record<string, Record<string, React.ReactNode>> = {
    inventario:{
        Productos: <InventarioProductosPage />,
        Categorias: <InventarioCategoriasPage/>,
    },
};

const ContentArea: React.FC<ContentAreaProps> = ({activeModule, activeSub}) =>{
    const module = modules[activeModule as keyof typeof modules]
    const Icon = (module?.icon || HomeIcon) as React.ComponentType<{ className?: string}>;
    const content = activeSub ? contentByModule[activeModule]?.[activeSub]: null;

    return (
        <main className="content-area">
            <div className="content-area__container">
                {content ? (
                    content
                ) : (
                    <>
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
                            {module?.subcategories.slice(0, 3).map((sub: string, i: number) => (
                                <div key={i} className="content-area__card">
                                    <h3 className="content-area__card-title">{sub}</h3>
                                    <p className="content-area__card-text">
                                        Contenido de {sub.toLowerCase()}
                                    </p>
                                </div>
                            ))}
                        </div>
                    </>
                )}
            </div>
        </main>
    );
};

export default ContentArea;
