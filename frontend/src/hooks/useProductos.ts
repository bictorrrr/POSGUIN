// src/hooks/useProductos.ts
import { useEffect, useRef, useState } from "react";
import { fetchProductos, type Producto } from "../services/products";

export function useProductos(q: string, activos: boolean | null) {
    const [data, setData] = useState<Producto[]>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<null | string>(null);

    const dq = useDebounce(q, 300);

    useEffect(() => {
        const ac = new AbortController();
        setLoading(true);
        setError(null);

        fetchProductos({ q: dq, activos, signal: ac.signal })
            .then(setData)
            .catch((e) => {
                if (e.name !== "AbortError") setError(e.message ?? "Error desconocido");
            })
            .finally(() => setLoading(false));

        return () => ac.abort();
    }, [dq, activos]);

    return { data, loading, error };
}

function useDebounce<T>(value: T, delay = 300) {
    const [v, setV] = useState(value);
    const t = useRef<number | null>(null);

    useEffect(() => {
        if (t.current) window.clearTimeout(t.current);
        t.current = window.setTimeout(() => setV(value), delay);
        return () => {
            if (t.current) window.clearTimeout(t.current);
        };
    }, [value, delay]);

    return v;
}
