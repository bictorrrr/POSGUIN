// Clock.tsx
import { useState, useEffect } from "react"

function Clock() {
    const [time, setTime] = useState(new Date())

    useEffect(() => {
        const interval = setInterval(() => setTime(new Date()), 1000)
        return () => clearInterval(interval)
    }, [])

    const dateStr = time.toLocaleDateString("es-MX", {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric"
    })

    const timeStr = time.toLocaleTimeString("es-MX", {
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit"
    })

    return (
        <div className="login-header">
            <span className="login-date">{dateStr}</span>
            <span className="login-time">{timeStr}</span>
        </div>
    )
}

export default Clock
