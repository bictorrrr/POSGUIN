import { useState, useEffect } from "react";
import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";
import ContentArea from "../components/ContentArea";
import FooterBar from "../components/FooterBar";
import "./CSS/DashboardPage.css"

function DashboardPage() {
    const [sidebarExpanded, setSidebarExpanded] = useState(true);
    const [activeModule, setActiveModule] = useState("dashboard");
    const [currentTime, setCurrentTime] = useState(new Date());
    const [notifications] = useState(3);

    useEffect(() => {
        const timer = setInterval(() => setCurrentTime(new Date()), 1000);
        return () => clearInterval(timer);
    }, []);

    return (
        <div className="Dash">
            <Sidebar
                expanded={sidebarExpanded}
                activeModule={activeModule}
                onToggle={() => setSidebarExpanded(!sidebarExpanded)}
                onSelect={setActiveModule}
            />
            <div className="Dashcontent">
                <Topbar activeModule={activeModule} />
                <ContentArea activeModule={activeModule} />
                <FooterBar currentTime={currentTime} notifications={notifications} />
            </div>
        </div>
    );
}


export default DashboardPage;
