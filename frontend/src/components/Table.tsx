// src/components/Table.tsx
import React from "react";
import "./CSS/Table.css";

export type Column<T> = {
    key: keyof T | string;
    header: string;
    align?: "left" | "center" | "right";
    render?: (row: T) => React.ReactNode; //celdas custom
};

interface TableProps<T> {
    columns: Column<T>[];
    data: T[];
}

function Table<T extends Record<string, any>>({ columns, data }: TableProps<T>) {
    return (
        <div className="card-glass">
            <table className="pg-table">
                <thead>
                <tr>
                    {columns.map((c) => (
                        <th key={String(c.key)} style={{ textAlign: c.align || "left" }}>
                            {c.header}
                        </th>
                    ))}
                </tr>
                </thead>
                <tbody>
                {data.map((row, i) => (
                    <tr key={i}>
                        {columns.map((c) => (
                            <td key={String(c.key)} style={{ textAlign: c.align || "left" }}>
                                {c.render ? c.render(row) : String(row[c.key as keyof T] ?? "")}
                            </td>
                        ))}
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
}

export default Table;
