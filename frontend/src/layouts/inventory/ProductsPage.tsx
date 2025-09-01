// src/pages/inventario/ProductosPage.tsx
import React, { useMemo, useState } from "react";
import "./CSS/ProductsPage.css";
import Input from "../../components/Input";
import Button from "../../components/Button";
import Table, { type Column } from "../../components/Table";
import { Plus, Search } from "lucide-react";
import { useProductos } from "../../hooks/useProductos";
import type { Producto } from "../../services/products";

const formatMoney = (n: number) =>
    new Intl.NumberFormat("es-MX", { style: "currency", currency: "MXN", minimumFractionDigits: 2 }).format(n);

const InventarioProductosPage: React.FC = () => {
    const [busqueda, setBusqueda] = useState("");
    const [soloActivos, setSoloActivos] = useState<boolean>(true); // default: mostrar activos

    // soloActivos ? true : null para “no filtrar” cuando esté desmarcado
    const { data: productos, loading, error } = useProductos(busqueda, soloActivos ? true : null);

    const columns: Column<Producto>[] = useMemo(
        () => [
            { key: "referencia", header: "Referencia", align: "left" },
            { key: "nombre", header: "Nombre", align: "left" },
            { key: "proveedor", header: "Proveedor", align: "left", render: (p) => p.proveedor ?? "N/D" },
            {
                key: "activo",
                header: "Estado",
                align: "center",
                render: (p) => (
                    <span
                        style={{
                            padding: "2px 8px",
                            borderRadius: 12,
                            fontSize: 12,
                            border: `1px solid ${p.activo ? "rgba(16,185,129,.5)" : "rgba(239,68,68,.5)"}`,
                            background: p.activo ? "rgba(16,185,129,.1)" : "rgba(239,68,68,.1)",
                        }}
                    >
            {p.activo ? "Activo" : "Inactivo"}
          </span>
                ),
            },
            { key: "precio_venta", header: "Precio Venta", align: "right", render: (p) => formatMoney(p.precio_venta) },
            { key: "costo", header: "Costo", align: "right", render: (p) => formatMoney(p.costo) },
            { key: "categoria", header: "Categoría", align: "left", render: (p) => p.categoria ?? "—" },
            {
                key: "acciones",
                header: "Acciones",
                align: "right",
                render: (p) => (
                    <div style={{ display: "inline-flex", gap: 8 }}>
                        <Button variant="def-button" onClick={() => console.log("Editar", p.referencia)}>Editar</Button>
                        <Button variant="def-button" onClick={() => console.log("Ver", p.referencia)}>Ver</Button>
                    </div>
                ),
            },
        ],
        []
    );

    return (
        <div className="products-contain">
            <h2 className="title">PRODUCTOS</h2>

            <div className="main-bar">
                <Input
                    type="text"
                    variant="search"
                    placeholder="Buscar producto..."
                    value={busqueda}
                    onChange={(e) => setBusqueda(e.target.value)}
                />
                <Button variant="search" icon={<Search size={18} strokeWidth={3} />}>
                    Buscar
                </Button>
                <label className="checkbox-inline" style={{ display: "inline-flex", alignItems: "center", gap: 8, marginLeft: 12 }}>
                    <input
                        type="checkbox"
                        checked={soloActivos}
                        onChange={(e) => setSoloActivos(e.target.checked)}
                    />
                    Solo activos
                </label>
                <hr className="divider" />
                <Button variant="add" icon={<Plus size={18} strokeWidth={3} />}>
                    Añadir producto
                </Button>
            </div>

            <hr className="vertical-divider" />

            {error && (
                <div className="error-box">
                    <strong>Ocurrió un error:</strong> {error}
                </div>
            )}

            {loading ? <div className="loading">Cargando productos…</div> : <Table columns={columns} data={productos} />}
        </div>
    );
};

export default InventarioProductosPage;
