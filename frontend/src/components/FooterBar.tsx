import React, {useState, useEffect} from "react";
import UserIcon from "./icons/UserIcon";
import ClockIcon from "./icons/ClockIcon";
import CalendarIcon from "./icons/CalendarIcon";
import BellIcon from "./icons/BellIcon";
import "./CSS/Footerbar.css";

interface FooterbarProps {
    currentTime?: Date,
    notifications?: number
}

const formatTime = (date: Date) =>
    date.toLocaleTimeString("es-ES", {
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
    });

const formatDate = (date: Date) =>
    date.toLocaleDateString("es-ES", {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
    });

const Footerbar: React.FC<FooterbarProps> = () => {
    const [currentTime, setCurrentTime] = useState(new Date());
    const [notifications] = useState(3);

    // Actualiza hora cada segundo
    useEffect(() => {
        const timer = setInterval(() => setCurrentTime(new Date()), 1000);
        return () => clearInterval(timer);
    }, []);

    return (
        <footer className="footerbar">
            <div className="footerbar-content">
                {/* --- Usuario --- */}
                <div className="footerbar-section footerbar-user">
                    <div className="user-avatar">
                        <UserIcon/>
                    </div>
                    <div className="user-info">
                        <p className="user-name">Juan Pérez</p>
                        <p className="user-role">Administrador</p>
                    </div>
                    <div className="footerbar-divider"></div>
                    <div className="work-hours">
                        <ClockIcon/>
                        <span>Horario: 9:00 - 18:00</span>
                    </div>
                </div>

                {/* --- Fecha y hora --- */}
                <div className="footerbar-section footerbar-datetime">
                    <div className="footerbar-date">
                        <CalendarIcon/>
                        <span>{formatDate(currentTime)}</span>
                    </div>
                    <div className="footerbar-time">
                        <ClockIcon/>
                        <span>{formatTime(currentTime)}</span>
                    </div>
                </div>

                {/* --- Notificaciones y estado --- */}
                <div className="footerbar-section footerbar-status">
                    <div className="notifications">
                        <div className="bell-icon">
                            <BellIcon/>
                            {notifications > 0 && (
                                <span className="badge">{notifications}</span>
                            )}
                        </div>
                        <span>{notifications} notificaciones</span>
                    </div>
                    <div className="footerbar-divider"></div>
                    <div className="system-status">
                        <span className="status-dot"></span>
                        <span>Sistema Online</span>
                    </div>
                </div>
            </div>
        </footer>
    );
};

export default Footerbar;
