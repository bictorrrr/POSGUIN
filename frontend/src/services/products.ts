// frontend/src/services/products.ts
export type Producto = {
    referencia: string;
    nombre: string;
    proveedor: string;      // texto “plano” para la tabla
    activo: boolean;
    precio_venta: number;
    costo: number;
    categoria: string | null;
};

const API_BASE = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

type FetchOpts = {
    q?: string;
    activos?: boolean | null; // null → no filtrar; true/false → filtrar
    signal?: AbortSignal;
};

export async function fetchProductos({ q, activos, signal }: FetchOpts): Promise<Producto[]> {
    const qs = new URLSearchParams();
    if (q && q.trim()) qs.set("q", q.trim());
    if (typeof activos === "boolean") qs.set("activos", String(activos));

    // OJO: tu router es `@router.get("/")` con prefijo típico `"/api/productos"`
    const url = `${API_BASE}/products/?${qs.toString()}`;

    const res = await fetch(url, {
        method: "GET",
        signal,
        headers: { Accept: "application/json" },
    });

    if (!res.ok) {
        const text = await res.text().catch(() => "");
        throw new Error(`Error ${res.status} al obtener productos. ${text}`);
    }

    const data = (await res.json()) as any[];

    // Ajusta estos mapeos dependiendo de tu ProductRead
    return data.map((p) => ({
        referencia: p.referencia ?? p.id ?? "", // fallback si usas id como referencia
        nombre: p.nombre,
        proveedor:
            p.proveedor?.nombre ?? p.proveedor_nombre ?? p.proveedor ?? "N/D",
        activo: Boolean(p.activo),
        precio_venta: Number(p.precio_venta ?? 0),
        costo: Number(p.costo ?? 0),
        categoria: p.categoria ?? null,
    }));
}
